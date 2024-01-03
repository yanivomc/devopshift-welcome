pipelineJob('Generic Project') {
    def repo = 'https://github.com/yanivomc/devopshift-welcome.git'

    triggers { // Configure when to check for changes
        scm('H/5 * * * *')
    }
    definition {
        cpsScm {
            scm {
                git {
                    remote { url(repo) }
                    branches('elbit/jenkinsdec26')
                    scriptPath('students/ron/Jenkinsfile')
                    extensions {}
                }
            }
        }
    }
}

pipelineJob('Project1') {
    def repo = 'https://github.com/yanivomc/devopshift-welcome.git'

    triggers { // Configure when to check for changes
        scm('H/5 * * * *')
    }
    definition {
        cpsScm {
            scm {
                git {
                    remote { url(repo) }
                    branches('elbit/jenkinsdec26')
                    scriptPath('students/ron/projects/project1/Jenkinsfile')
                    extensions {}
                }
            }
        }
    }
}
