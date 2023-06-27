{{- define "labels.data" -}}
app: {{ .name }}
type: {{ .type }}
{{- end }}