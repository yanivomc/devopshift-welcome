import jenkins.model.*
import hudson.security.*
import org.jenkinsci.plugins.matrixauth.PermissionEntry
import org.jenkinsci.plugins.matrixauth.AuthorizationType

def env = System.getenv()

def jenkins = Jenkins.getInstance()

// Only set security realm if not already configured (CasC might have done it)
// Using class name check to avoid IllegalAccessError on protected inner class SecurityRealm.None
if (jenkins.getSecurityRealm().getClass().getName().contains("None")) {
    jenkins.setSecurityRealm(new HudsonPrivateSecurityRealm(false))
    def user = jenkins.getSecurityRealm().createAccount(env.JENKINS_USER, env.JENKINS_PASS)
    user.save()
}

// Only add admin permission if the strategy matches our expectation
// and avoid calling setAuthorizationStrategy(new ...) which wipes CasC settings
def authStrategy = jenkins.getAuthorizationStrategy()
if (authStrategy instanceof GlobalMatrixAuthorizationStrategy) {
    def adminUserId = env.JENKINS_USER
    def adminEntry = PermissionEntry.user(adminUserId)
    
    // Use the modern PermissionEntry API to avoid legacy warnings
    authStrategy.add(Jenkins.ADMINISTER, adminEntry)
    authStrategy.add(Jenkins.READ, adminEntry)
}

jenkins.save()
