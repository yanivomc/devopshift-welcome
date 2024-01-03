pipelineJob('my-pipeline') { // Job NAME
  definition {
    cps {
      script(readFileFromWorkspace('tudents/Terkel/jenkinsFile101/jenkinsfile'))
      sandbox()     
    }
  }
}