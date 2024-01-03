pipelineJob('my-pipeline') { // Job NAME
  definition {
    cps {
      script(readFileFromWorkspace('students/Terkel/jenkinsFile101/jenkinsfile'))
      sandbox()     
    }
  }
}