{{- define "deployment.bear" -}}
app: {{ .Values.bear.label.app }}
type: {{ .Values.bear.label.type }}
{{- end }}


{{- define "deployment.bear" -}}
app: {{ .Values.moose.label.app }}
type: {{ .Values.moose.label.type }}
{{- end }}