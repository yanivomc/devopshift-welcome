pipelineJob('my-pipeline-broken') { // broken branch config
  def myrepo = 'https://github.com/yanivomc/devopshift-welcome.git'
  def myname = 'Terkel'
  def mymail = 'terkmail@gmail.com'
  triggers {
    scm('H/5 * * * *')
  }
  description("My Pipeline")

  definition {
    cpsScm {
      scm {
        git(myrepo) { // Your repository
            branches('elbit/jenkinsdec26') // this is not fine
            userRemoteConfigs {
                userRemoteConfig {
                    name(myname)
                    email(mymail)
                }
            }
    }
      }
      scriptPath('students/Terkel/jenkinsFile101/jenkinsfile') 
    }
  }
}

pipelineJob('my-pipeline') { // ok
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
          scriptPath('students/Terkel/jenkinsFile101/jenkinsfile')
          extensions { }  // required as otherwise it may try to tag the repo, which you may not want
        }
      }
    }
  }
}