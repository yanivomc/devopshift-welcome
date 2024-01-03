job('NodeJS example') { // Job NAME
    scm { // Configure Source control management 
        git('git://github.com/yanivomc/docker-demo.git') {  node -> // is hudson.plugins.git.GitSCM
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
        shell("npm install")
    }
}

pipelineJob('projectx') { // Job NAME
    definition {
        cpsScm {
            scm {
                git('git://github.com/yanivomc/devopshift-welcome.git') { // Your repository
                    branches('elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
                    // extensions {
                    //     // relativeTargetDirectory('docker-demo') // Optional: Check out to a sub-directory
                    //     // cleanBeforeCheckout() // Optional: Clean the workspace before checkout
                    // }
                    userRemoteConfigs {
                        userRemoteConfig {
                            name('Yaniv')
                            email('yaniv@domain.com')
                        }
                    }
                }
            }
            scriptPath('./students/yaniv/repo/projectx/jenkinsfile') // Path to the Jenkinsfile in the repository
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
}
