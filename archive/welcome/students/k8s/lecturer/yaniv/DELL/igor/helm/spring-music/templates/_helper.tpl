{{ define "labels" }}
generator: helm
app-name: {{ .Chart.Name }}
date: {{ now | date "2006-01-02T15:04:05" }}
version: {{ .Chart.Version }}
{{ end }}