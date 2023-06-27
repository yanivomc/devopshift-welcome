{{- define "deployment.beer.labels" -}}
app: {{ .Values.labels.app }}
type: {{ .Values.labels.type }}
{{- end }}

