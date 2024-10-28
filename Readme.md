## Terraform workshop
# Installing terraform:
~
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
~



az network nic ip-config update --name internal-yanivc-1 --nic-name nic-yanivc-1 --resource-group rg-yanivc --remove publicIpAddress
az network nic ip-config update --name internal-yanivc-2 --nic-name nic-yanivc-2 --resource-group rg-yanivc --remove publicIpAddress
