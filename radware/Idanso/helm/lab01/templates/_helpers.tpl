# bear
{{- define "bear.labels"  -}}
app: {{ .Values.apps.bear.name }}
type: animals
{{- end }}
{{- define "bear.image"  -}}
{{ .Values.apps.bear.repo }}/{{ .Values.apps.bear.image }}:{{ .Values.apps.bear.tag }}
{{- end }}

# moose
{{- define "moose.labels"  -}}
app: {{ .Values.apps.moose.name }}
type: animals
{{- end }}
{{- define "moose.image"  -}}
{{ .Values.apps.moose.repo }}/{{ .Values.apps.moose.image }}:{{ .Values.apps.moose.tag }}
{{- end }}