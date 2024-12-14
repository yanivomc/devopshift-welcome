#!/bin/bash
#Global Vars
workingfolder=~/workarea/jb/
devopshiftfolder=~/workarea/devopshift/
user_info_file="${devopshiftfolder}user_info.txt"
#!/bin/bash
#Global Vars
workingfolder=~/workarea/jb/
user_info_file="${workingfolder}user_info.txt"
# Function to ask for user information
gather_user_info() {
    if [[ -f "$user_info_file" ]]; then
        source "$user_info_file"
        echo -e "\e[34mUsing existing information:\e[0m"
        echo -e "Branch: $GITBRANCH"
        echo -e "Repository URL: $GITURL"
        echo -e "Git Username: $GITUSERNAME"
    else
        echo -e "\e[33mPlease provide the following information:\e[0m"
        read -p "Branch provided by instructor: " GITBRANCH
        read -p "Your forked repo URL (without https://): " GITURL
        read -p "Your Git username: " GITUSERNAME
    fi
    read -p "Your Git token: " GITTOKEN
}

# Function to confirm the information provided
confirm_user_info() {
    echo -e "\n\e[34mYou have provided the following information:\e[0m"
    echo "Branch: $GITBRANCH"
    echo "Repository URL: $GITURL"
    echo "Git Username: $GITUSERNAME"
    read -p "Is this information correct? (yes/no): " CONFIRMATION
}

# Function to get EC2 public IP
get_public_ip() {

      PUBIP=$(TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") \
      && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4)
      echo $PUBIP
}

# Function to handle the git operations
git_operations() {
    echo -e "\e[32mCreating Folder $workingfolder\e[0m"
    rm -rf "$workingfolder"
    mkdir -p "$workingfolder" && cd "$workingfolder" || {
        echo -e "\e[31mError: Failed to create or navigate to working folder.\e[0m" >&2
        exit 1
    }

    # Clone the repository
    echo -e "\e[32mRunning clone as follows:\e[0m"
    git clone -b "$GITBRANCH" "https://$GITURL" ./ || {
        echo -e "\e[31mError: Failed to clone repository. Please check your branch or repo URL.\e[0m" >&2
        exit 1
    }

    # Set remote URL with authentication token
    GITSETTOKEN="https://$GITUSERNAME:$GITTOKEN@$GITURL"
    echo -e "\e[32mSetting git Token in remote URL:\e[0m"
    echo "debug: $GITSETTOKEN "
    echo "debug: $GITTOKEN "
    git remote set-url origin "$GITSETTOKEN" || {
        echo -e "\e[31mError: Failed to set remote URL.\e[0m" >&2
        exit 1
    }

    # Test commit and push
    echo -e "\e[32mTesting commit and push\e[0m"
    local current_time=$(date +"%H:%M:%S")
    echo "Current time: $current_time"
    echo "testing commit $current_time" > test.txt
    git add test.txt || {
        echo -e "\e[31mError: Failed to add files.\e[0m" >&2
        exit 1
    }
    git commit -m "test" || {
        echo -e "\e[31mError: Failed to commit changes.\e[0m" >&2
        exit 1
    }
    git push || {
        echo -e "\e[31mError: Failed to push changes. Please check your Git credentials and permissions.\e[0m" >&2
        exit 1
    }

    echo -e "\n\e[32mGit operations completed successfully.\e[0m"

    # Save user information without GITTOKEN
    echo "GITBRANCH=$GITBRANCH" > "$user_info_file"
    echo "GITURL=$GITURL" >> "$user_info_file"
    echo "GITUSERNAME=$GITUSERNAME" >> "$user_info_file"
    echo -e "\n\e[32mPlease keep the following information for next run/use of this script:\e[0m"
    cat "$user_info_file"

    echo -e "\n\e[32mRead here how to use it again: https://bit.ly/4fLqwbd \e[0m"

    # Providing the new endpoint for the user repo
    PUBIP=$(get_public_ip)
    echo -e "\n\e[32m*****************************************************************\e[0m"
    echo -e "\n\e[32mSetup completed. Please open the following URL in your browser to switch to your VSCode workspace REPO:\e[0m"
    echo -e "\nhttp://$PUBIP:5001/?folder=$workingfolder"
}

# Main script loop
MAX_RETRIES=3
RETRY_COUNT=0

while true; do
    gather_user_info
    confirm_user_info

    if [[ "$CONFIRMATION" == "yes" ]]; then
        read -p "Are you sure you want to proceed with the Git operations? (yes/no): " PROCEED
        if [[ "$PROCEED" == "yes" ]]; then
            git_operations
            break
        else
            echo -e "\e[33mOperation canceled. Exiting...\e[0m"
            exit 0
        fi
    else
        echo -e "\n\e[33mLet's try again.\e[0m"
        RETRY_COUNT=$((RETRY_COUNT+1))
        if [[ $RETRY_COUNT -ge $MAX_RETRIES ]]; then
            echo -e "\e[31mMaximum retries reached. Exiting.\e[0m"
            exit 1
        fi
    fi
done

exit 0
