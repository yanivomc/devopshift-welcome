job('NodeJS example') { // Job NAME
    scm { // Configure Source control management 
        
         git('https://github.com/yanivomc/devopshift-welcome.git') { node ->
            node / elbit/jenkinsdec26 << '*/feature' // Specify the branch here

            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
    wrappers {
        nodejs('nodejs') // this is the name of the NodeJS installation in 
                         // Manage Jenkins -> Configure Tools -> NodeJS Installations -> Name
    }
    steps { // what steps to take 
        shell("echo “Test 1
               echo install packages
               npm install
               echo Running unit tests")
    }
}