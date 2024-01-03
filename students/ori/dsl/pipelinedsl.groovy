pipelineJob('projectx') { // Job NAME
   definition {
       cpsScm {
           scm {
               git('https://github.com/yanivomc/devopshift-welcome.git') { 
                   branches('elbit/jenkinsdec26')
                   userRemoteConfigs {
                       userRemoteConfig {
                           name('DSL User')
                           email('jenkins-dsl@domain.com')
                       }
                   }
               }
           }
           scriptPath('students/ori/pipelines/day030124/jenkinsfile') // Path to the Jenkinsfile in the repository
       }
   }
   triggers { // Configure when to check for changes
       scm('H/5 * * * *')
   }
}
