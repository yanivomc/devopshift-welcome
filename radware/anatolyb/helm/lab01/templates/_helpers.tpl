{{- define "deployment.labels" -}}
app: {{.Values.labels.app}}
type: {{.Values.labels.type}}
{{- end }}