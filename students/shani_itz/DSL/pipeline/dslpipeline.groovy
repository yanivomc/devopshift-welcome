pipelineJob('projectx') { // Job NAME
   definition {
       cpsScm {
           scm {
               git('https://github.com/yanivomc/devopshift-welcome.git') { // Your repository
                   branches(' elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
                //    extensions {
                //        relativeTargetDirectory('docker-demo') // Optional: Check out to a sub-directory
                //        cleanBeforeCheckout() // Optional: Clean the workspace before checkout
                //    }
                   userRemoteConfigs {
                       userRemoteConfig {
                           name('shani')
                           email('shani@gmail.com')
                       }
                   }
               }
           }
           scriptPath('students/shani_itz/DSL/pipeline/JenkinsFile') // Path to the Jenkinsfile in the repository
       }
   }
   triggers { // Configure when to check for changes
       scm('H/5 * * * *')
   }
}
