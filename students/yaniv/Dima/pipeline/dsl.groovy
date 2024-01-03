job('Pipeline example') { // Job NAME
    scm { // Configure Source control management 
        git('https://github.com/yanivomc/devopshift-welcome.git') {  node -> // is hudson.plugins.git.GitSCM
            node / gitConfigName('DSL User')
            node / gitConfigEmail('jenkins-dsl@domain.com')
        }
    }
    triggers { // Configure when to check for changes 
        scm('H/5 * * * *')
    }
    wrappers {
        nodejs('MyNodeJs') // this is the name of the NodeJS installation in 
                         // Manage Jenkins -> Configure Tools -> NodeJS Installations -> Name
    }
    steps { // what steps to take 
        shell("npm install")
    }
}

//pipelineJob('projectx') { // Job NAME
//   definition {
//       cpsScm {
//           scm {
//              git('https://github.com/yanivomc/devopshift-welcome.git') { // Your repository
//                   branches('elbit/jenkinsdec26') // Branch to build, replace with your branch if needed
//                   
//                   userRemoteConfigs {
//                       userRemoteConfig {
//                           name('DSL User')
//                           email('jenkins-dsl@domain.com')
//                       }
//                   }
//               }
//           }
//           scriptPath('./students/yaniv/Dima/Jenkinsfile/Jenkinsfile') // Path to the Jenkinsfile in the repository
//       }
//   }
//   triggers { // Configure when to check for changes
//       scm('H/5 * * * *')
//   }
//}

pipelineJob('my-pipeline2') { // broken branch config
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
         scriptPath('./students/yaniv/Dima/Jenkinsfile/Jenkinsfile')
         extensions { }  // required as otherwise it may try to tag the repo, which you may not want
       }
     }
   }
 }
}


