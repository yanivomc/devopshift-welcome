{{- define "configmap-data" -}}
dbname: {{ .Values.dbname }}
dbtable: {{ .Values.databases.dbtable | upper | trunc 2}}
type: {{ .Values.databases.type }}
{{- end}}