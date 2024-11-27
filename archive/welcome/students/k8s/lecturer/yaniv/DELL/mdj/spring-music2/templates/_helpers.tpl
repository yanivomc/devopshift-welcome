{{ define "spring.labels" }}
generator: helm
app-name: {{ .Chart.Name }}
date: {{ now | date "2006-02-08" }}
version: {{ .Chart.Version }}
{{ end }}
