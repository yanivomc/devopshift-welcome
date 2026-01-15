import org.jenkinsci.plugins.scriptsecurity.scripts.ScriptApproval

def sa = ScriptApproval.get()

def signatures = [
    // Methods
        'method hudson.model.Cause$UpstreamCause getUpstreamBuild',
        'method hudson.model.Cause$UpstreamCause getUpstreamProject',
        'method hudson.model.Cause$UpstreamCause getUpstreamRun',
        'method hudson.model.Item getFullName',
        'method hudson.model.Run getCause java.lang.Class',
        'method hudson.model.Run getCauses',
        'method hudson.model.Run getParent',
        'method jenkins.model.FullyNamed getFullName',
        'method org.jenkinsci.plugins.workflow.support.steps.build.RunWrapper getRawBuild',
        'staticMethod groovy.json.JsonOutput toJson java.lang.Object',
        'staticMethod java.lang.System getenv java.lang.String',

        // Static methods
        'staticMethod groovy.json.JsonOutput toJson java.lang.Object'
]

// Approve all signatures
signatures.each { sig ->
    println "Approving: ${sig}"
    sa.approveSignature(sig)
}

sa.save()
println "Done."
