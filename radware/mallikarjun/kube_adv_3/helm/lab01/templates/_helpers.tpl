{{- define "deployment.bear" -}}
app: {{ .Values.bear.label.app }}
type: {{ .Values.bear.label.type }}
{{- end }}


{{- define "deployment.moose" -}}
app: {{ .Values.moose.label.app }}
type: {{ .Values.moose.label.type }}
{{- end }}