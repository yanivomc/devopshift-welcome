{{- define "configmap.data" -}}
dbname: {{ .Values.dbname }}
dbtable: {{ .Values.databases.dbtable | upper | trunc 2}}
type: {{ .Values.databases.type }}
{{- end }}


{{- define "bear-image" -}}
{{ .Values.image.repository}}/{{ .Values.image.name}}:{{ .Values.image.tagbear}}
{{- end }}

{{- define "moose-image" -}}
{{ .Values.image.repository}}/{{ .Values.image.name}}:{{ .Values.image.tagmoose}}
{{- end }}




{{- define "labels-bear" -}}
app: bear
type: bear
{{- end }}

{{- define "labels-moose" -}}
app: moose
type: moose
{{- end }}