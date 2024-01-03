job('SCM-Test') { // Job NAME
    scm { // Configure Source control management 
        git('https://github.com/yanivomc/devopshift-welcome.git') {  node -> // is hudson.plugins.git.GitSCM
        branch('elbit/jenkinsdec26') 
        scriptPath('students/Roy/pipeline/projectX/Jenkinsfile')    
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
}
