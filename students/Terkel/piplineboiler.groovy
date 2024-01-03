pipelineJob('my-pipeline') { // Job NAME
    definition {
    cps {
      script('logic-here')
      sandbox()
    }
  }
}
