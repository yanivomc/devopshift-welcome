job('NodeJS example') {
    scm {
        git('git://github.com/yanivomc/docker-demo.git') { node ->
            node / branches << '*/elbit/jenkinsdec26' // Specify the branch here
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers {
        scm('H/5 * * * *') // Poll SCM every 5 minutes
    }
    wrappers {
        nodejs('nodejs') // Use the NodeJS installation configured in Jenkins
    }
    steps {
        shell("npm install") // Run npm install as a build step
    }
}
