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
