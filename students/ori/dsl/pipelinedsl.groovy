pipelineJob('My Generated Job') { // Job NAME
   definition {
       cpsScm {
           scm {
                git {
                    remote { url('https://github.com/yanivomc/devopshift-welcome.git') }
                    branches('elbit/jenkinsdec26') // this is fine
                    scriptPath('students/yaniv/repo/projectx/jenkinsfile')
                    extensions { }  // required as otherwise it may try to tag the repo, which you may not want
                }  
           }
           //scriptPath('students/ori/pipelines/day030124/jenkinsfile') // Path to the Jenkinsfile in the repository
       }
   }
   triggers { // Configure when to check for changes
       scm('H/5 * * * *')
   }
}
