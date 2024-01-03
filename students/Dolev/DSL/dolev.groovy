job('NodeJS example') { // Job NAME
    scm { // Configure Source control management 
        git('https://github.com/yanivomc/devopshift-welcome.git') {  node -> // is hudson.plugins.git.GitSCM
            // Specify the branches to examine for changes and to build.
            //https://jenkinsci.github.io/job-dsl-plugin/#method/javaposse.jobdsl.dsl.jobs.FreeStyleJob.scm
            branch('elbit/jenkinsdec26')
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
    wrappers {
        nodejs('NodeJS21.5') // this is the name of the NodeJS installation in 
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
                git('https://github.com/yanivomc/devopshift-welcome.git') { // Your repository
                    branches('elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
                    userRemoteConfigs {
                        userRemoteConfig {
                            name('Dolev')
                            email('Dolev@domain.com')
                        }
                    }
                }
            }
            scriptPath('students/Dolev/repo/projectx/jenkinsfile') // Path to the Jenkinsfile in the repository
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
}