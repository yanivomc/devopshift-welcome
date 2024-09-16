#!/bin/bash

# Function to validate installation of tools by checking their command availability
validate_tool_installation() {
    if ! command -v "$1" &> /dev/null; then
        echo "Error: $2 installation failed."
        exit 1
    else
        echo "$2 installation was successful."
    fi
}

# Function to install Azure CLI
install_azure_cli() {
    echo "Installing Azure CLI..."
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    validate_tool_installation "az" "Azure CLI"
}

# Function to install AWS CLI
install_aws_cli() {
    echo "Installing AWS CLI..."
    sudo apt-get update
    sudo apt-get install -y awscli
    validate_tool_installation "aws" "AWS CLI"
}

# Function to install the latest Terraform version
install_latest_terraform() {
    echo "Installing latest Terraform version..."
    wget -qO- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    sudo apt update && sudo apt install terraform
    validate_tool_installation "terraform" "Terraform"
}

# Function to install all the tools
install_all_tools() {
    install_azure_cli
    install_aws_cli
    install_latest_terraform
}

# Function to display the main menu
display_main_menu() {
    echo "Select an option:"
    echo "1. Install Azure CLI"
    echo "2. Install AWS CLI"
    echo "3. Install latest Terraform"
    echo "4. Install all tools"
    echo "5. Exit"
}

# Function to display a welcome message
display_welcome_msg() {
    echo "Welcome to the DevOps tool installation script!"
    echo "This script will help you install Azure CLI, AWS CLI, and Terraform."
    echo "It is designed to run on Ubuntu and other Debian-based systems."
    echo "Please select an option from the menu below:"
}

# Function to handle user input and process menu options
read_user_input() {
    display_welcome_msg
    display_main_menu

    while read -p "Enter your choice: " choice; do
        case "$choice" in
            1) install_azure_cli; break ;;
            2) install_aws_cli; break ;;
            3) install_latest_terraform; break ;;
            4) install_all_tools; break ;;
            5) echo "Exiting..."; exit ;;
            *) echo "Invalid choice. Please try again." ;;
        esac
        display_main_menu
    done
}

# Start the script
read_user_input
