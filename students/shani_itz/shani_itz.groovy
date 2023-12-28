job('Groovy example') { // Job NAME
    scm { // Configure Source control management 
        git('git:https://github.com/yanivomc/devopshift-welcome.git' 'branch:elbit/jenkinsdec26') {  node -> // is hudson.plugins.git.GitSCM
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/2 * * * *')
    }
    wrappers {
        nodejs('NodeJS') // this is the name of the NodeJS installation in 
                         // Manage Jenkins -> Configure Tools -> NodeJS Installations -> Name
    }
    steps { // what steps to take 
        shell("echo "Test 1"")
        shell("echo "install packages"")
        shell("npm install")
        shell("echo "Running unit tests"")
    }
}
