# create function to validate each tool installation by allowing it to run the passed command to it and check the exit status
validate_tool_installation() {
    command -v $1 > /dev/null
    if [ $? -ne 0 ]; then
        echo "Error: $2 installation failed."
        exit 1
    fi
}

# Create function to install Azure CLI
function install_azure_cli() {
    echo "Installing Azure CLI..."
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    # Validate Azure CLI installation
    validate_tool_installation "az" "Azure CLI"
}

# Create function to install AWS CLI
function install_aws_cli() {
    echo "Installing AWS CLI..."
    sudo apt-get update
    sudo apt-get install -y awscli
    # Validate AWS CLI installation
    validate_tool_installation "aws" "AWS CLI"
}

# Create function to install latest terraform version using the following commands:
install_latest_terraform() {
    echo "Installing latest Terraform version..."
    wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install terraform
    # Validate Terraform installation
    validate_tool_installation "terraform" "Terraform"
}

# Create function to install all above tools
install_all_tools() {
    install_azure_cli
    install_aws_cli
    install_latest_terraform
}

# Create function to display the main menu
display_main_menu() {
    echo "Select an option:"
    echo "1. Install Azure CLI"
    echo "2. Install AWS CLI"
    echo "3. Install latest Terraform version"
    echo "4. Install all tools"
    echo "5. Exit"
}
# Add a welcome message to the script and let the user know what the script does and what to expect along with the OS compatibility
display_welcome_msg() {
echo "Welcome to the DevOps tool installation script!"
echo "This script will help you install the following tools:"
echo "- Azure CLI"
echo "- AWS CLI"
echo "- Terraform"
echo "This script is compatible with Ubuntu and Debian based systems."
echo "Please select an option from the menu below:"
}

# Create function to read user input
read_user_input() {
    # show the welcome message
    display_welcome_msg

    read -p "Enter your choice: " choice
    case $choice in
        1) install_azure_cli ;;
        2) install_aws_cli ;;
        3) install_latest_terraform ;;
        4) install_all_tools ;;
        5) exit ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
}
