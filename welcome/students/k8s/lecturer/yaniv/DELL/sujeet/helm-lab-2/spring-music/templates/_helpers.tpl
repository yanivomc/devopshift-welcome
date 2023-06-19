{{/* This is a comment - Generate basic labels */}}
{{- define "spring-music.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "spring.labels" -}}
generator: helm
date: {{ now | htmlDate }}
app-name: {{ .Chart.Name }}
version:  {{ .Chart.Version }}
{{- end -}}

{{- define "jobcommand" -}}
  - /bin/sh
  - -c
  - date; echo "hello world"
{{- end -}}
