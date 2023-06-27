{{- define "configmap.data" -}}
dbname: {{ .Values.dbname }}
dbtable: {{ .Values.databases.dbtable }}
type: {{ .Values.databases.type }}
{{- end }}
