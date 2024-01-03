pipelineJob('my-pipeline') {
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
        // git {
        //   remote { url(repo) }
        //   branches('elbit/jenkinsdec26')
        //   scriptPath('students/Terkel/jenkinsFile101/jenkinsfile')
        //   extensions { }  // required as otherwise it may try to tag the repo, which you may not want
        // }
        git(myrepo) { // Your repository
            branches('elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
            userRemoteConfigs {
                userRemoteConfig {
                    name(myname)
                    email(mymail)
                }
            }
    }
      }
    }
  }
}

pipelineJob('my-pipeline2') {
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
          branches('elbit/jenkinsdec26')
          scriptPath('students/Terkel/jenkinsFile101/jenkinsfile')
          extensions { }  // required as otherwise it may try to tag the repo, which you may not want
        }
      }
    }
  }
}