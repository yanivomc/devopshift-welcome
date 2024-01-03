pipelineJob('pipeline-ci') {
    definition {
        cps {
            script(readFileFromWorkspace('students/ron/Jenkinsfile'))
            sandbox()
        }
    }
}