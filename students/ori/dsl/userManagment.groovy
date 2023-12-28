import jenkins.model.*
import hudson.security.*

def hudsonInstance = Jenkins.getInstance()

// Create or get the user
def user = hudsonInstance.securityRealm.createAccount('ori', '098098')

// Optionally set the full name
user.setFullName('Ori Jenkins')

// Save the user details
user.save()

