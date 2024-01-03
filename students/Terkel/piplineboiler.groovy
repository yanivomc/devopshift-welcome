pipelineJob('my-pipeline') {
  def repo = 'https://github.com/yanivomc/devopshift-welcome.git'

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
        git(url(repo)) { // Your repository
            branches('elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
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