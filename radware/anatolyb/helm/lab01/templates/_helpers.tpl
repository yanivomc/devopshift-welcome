{{- define "deployment.bear.labels" -}}
app: {{.Values.bear.labels.app}}
type: {{.Values.bear.labels.type}}
{{- end }}
{{- define "deployment.moose.labels" -}}
app: {{.Values.moose.labels.app}}
type: {{.Values.moose.labels.type}}
{{- end }}