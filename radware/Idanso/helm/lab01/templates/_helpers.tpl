{{- define "bear.labels"  }}
app: {{ .Values.apps.bear.name }}
type: animals
{{- end }}
{{- define "moose.labels"  }}
app: {{ .Values.apps.moose.name }}
type: animals
{{- end }}