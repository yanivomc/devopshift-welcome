pipelineJob('קובץ dsa') { // broken branch config
 def repo = 'https://github.com/yanivomc/devopshift-welcome.git'


 triggers {
   scm('H/5 * * * *')
 }
 description("My Pipeline 2")


 definition {
   cpsScm {
     scm {
       git {
         remote { url(repo) }
         branches('elbit/jenkinsdec26') // this is fine
         scriptPath('students/matan/enkinsfile')
         extensions { }  // required as otherwise it may try to tag the repo, which you may not want
       }
     }
   }
 }
}
