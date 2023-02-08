{{- define "spring.labels" }}
  labels:
    generator: helm
    date: {{ now | htmlDate }}
    app-name: {{ .Chart.Name}}
    version:  {{ .Chart.Version }}
{{- end }}

