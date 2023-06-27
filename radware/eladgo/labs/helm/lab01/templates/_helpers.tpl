{{- define "animal.data" -}}
app: {{ .Values.Animal.Labels.app }}
type: {{ .Values.Animal.Labels.type }}
{{- end }}