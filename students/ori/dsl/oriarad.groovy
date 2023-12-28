job('MyJobOri') { // Job NAME
    scm { // Configure Source control management 
        git('http://github.com/yanivomc/devopshift-welcome.git', '*/elbit/jenkinsdec26') {  node -> // is hudson.plugins.git.GitSCM
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
    wrappers {
        nodejs('nodejs') // this is the name of the NodeJS installation in 
                         // Manage Jenkins -> Configure Tools -> NodeJS Installations -> Name
    }
    steps { // what steps to take
        shell('echo "Hello!"')
        shell("npm install")
    }
}
