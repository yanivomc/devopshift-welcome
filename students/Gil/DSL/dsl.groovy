job('Gil-Job example') { // Job NAME
    scm { // Configure Source control management 
        git('git://github.com/yanivomc/docker-demo.git','elbit/jenkinsdec26') {  node -> // is hudson.plugins.git.GitSCM
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
               git('git://github.com/yanivomc/docker-demo.git') { // Your repository
                   branches('*/main') // Branch to build, replace with your branch if needed
                   extensions {
                       relativeTargetDirectory('docker-demo') // Optional: Check out to a sub-directory
                       cleanBeforeCheckout() // Optional: Clean the workspace before checkout
                   }
                   userRemoteConfigs {
                       userRemoteConfig {
                           name('DSL User')
                           email('jenkins-dsl@domain.com')
                       }
                   }
               }
           }
           scriptPath('Jenkinsfile') // Path to the Jenkinsfile in the repository
       }
   }
   triggers { // Configure when to check for changes
       scm('H/5 * * * *')
   }
}
