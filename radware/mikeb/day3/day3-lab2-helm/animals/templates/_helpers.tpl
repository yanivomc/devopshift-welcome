{{- define "bear-labels.data" -}}
app: {{ .Values.Bear.app }}
type: {{ .Values.Bear.type }}
{{- end }}

{{- define "bear-image" -}}
{{ .Values.image.repo }}/{{ .Values.Bear.Image.Name }}:{{ .Values.Bear.Image.Tag }}
{{- end }}

{{- define "moose-labels.data" -}}
app: {{ .Values.Moose.app }}
type: {{ .Values.Moose.type }}
{{- end }}

{{- define "moose-image" -}}
{{ .Values.image.repo }}/{{ .Values.image.name }}:{{ .Values.image.tagmoose }}
{{- end }}
