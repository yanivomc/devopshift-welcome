#!/bin/bash

HOMEREPO="/home/ubuntu/workarea"

# Function to validate repository URL
validate_repo() {
  git ls-remote $1 &> /dev/null
  if [ $? -ne 0 ]; then
    echo "Error: Invalid repository URL or you don't have access."
    exit 1
  fi
}

# Function to generate SSH key
generate_ssh_key() {
  mkdir -p $HOMEREPO/repo/keys
  ssh-keygen -t rsa -b 4096 -f $HOMEREPO/repo/keys/deploy_key -N ""
  echo "SSH key generated at $HOMEREPO/repo/keys/deploy_key"
  echo "Please add the following SSH key to your repository's deploy keys:"
  cat $HOMEREPO/repo/keys/deploy_key.pub
  echo
  echo "Go to your repository settings, add a new deploy key, and paste the key above."
  echo "Once done, type 'continue' to proceed."
  read -p "Type 'continue' to proceed: " confirm
  while [ "$confirm" != "continue" ]; do
    read -p "Type 'continue' to proceed: " confirm
  done
}

# Function to add SSH key to ssh-agent
add_ssh_key_to_agent() {
  eval "$(ssh-agent -s)"
  ssh-add $HOMEREPO/repo/keys/deploy_key
}

# Function to configure SSH config
configure_ssh_config() {
  ssh_config_path="$HOME/.ssh/config"
  echo -e "Host github.com-repo-0\n\tHostname github.com\n\tIdentityFile=$HOMEREPO/repo/keys/deploy_key" >> $ssh_config_path
  echo "SSH config updated."
}

# Function to validate SSH connection
validate_ssh_connection() {
  ssh -T git@github.com
  if [ $? -ne 1 ]; then
    echo "Error: SSH connection failed."
    exit 1
  fi
  echo "SSH connection validated."
}

# Function to validate write permission
validate_write_permission() {
  touch test_file
  git add test_file
  git commit -m "Test commit"
  git push origin $branch
  if [ $? -ne 0 ]; then
    echo "Error: Write permission validation failed."
    exit 1
  fi
  git rm test_file
  git commit -m "Remove test file"
  git push origin $branch
  echo "Write permission validated."
}

# Function to get EC2 public IP
get_public_ip() {
  PUBIP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)
  echo $PUBIP
}

# Main script
read -p "Is this the first run? (yes/no): " first_run
if [ "$first_run" == "yes" ]; then
  read -p "Enter your repository URL: " repo_url
  validate_repo $repo_url
  
  read -p "Enter the branch to clone (default: main): " branch
  branch=${branch:-main}
  
  mkdir -p $HOMEREPO
  git clone --branch $branch $repo_url $HOMEREPO/repo
  if [ $? -ne 0 ]; then
    echo "Error: Cloning the repository failed."
    exit 1
  fi
  cd $HOMEREPO/repo
  generate_ssh_key
  add_ssh_key_to_agent
  configure_ssh_config
  validate_ssh_connection
  validate_write_permission
  echo "Setup completed successfully."
else
  read -p "Enter your repository URL: " repo_url
  validate_repo $repo_url
  
  read -p "Enter the branch to clone (default: main): " branch
  branch=${branch:-main}
  
  if [ -d "$HOMEREPO/repo" ]; then
    cd $HOMEREPO/repo
    git remote set-url origin $repo_url
    git fetch origin $branch
    if [ $? -ne 0 ]; then
      echo "Error: Fetching changes failed. Please fix the issue and retry."
      exit 1
    fi
    git reset --hard origin/$branch
  else
    mkdir -p $HOMEREPO
    git clone --branch $branch $repo_url $HOMEREPO/repo
    if [ $? -ne 0 ]; then
      echo "Error: Cloning the repository failed."
      exit 1
    fi
    cd $HOMEREPO/repo
  fi
  
  if [ ! -f "./keys/deploy_key" ]; then
    echo "SSH key not found in ./keys/"
    read -p "Do you want to generate a new key? (yes/no): " generate_new_key
    if [ "$generate_new_key" == "yes" ]; then
      generate_ssh_key
    else
      echo "No key to use for SSH. Exiting."
      exit 1
    fi
  else
    add_ssh_key_to_agent
    configure_ssh_config
    validate_ssh_connection
    validate_write_permission
    echo "Setup completed successfully using existing key."
  fi
fi

PUBIP=$(get_public_ip)
echo "Setup completed. Please open the following URL in your browser to switch to your VSCode workspace:"
echo "http://$PUBIP:5001/?folder=$HOMEREPO/repo/"
