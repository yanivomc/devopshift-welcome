{{/* This is a comment - Generate basic labels */}}
{{- define "spring.labels" }}
  generator: helm
  app: {{ .Chart.Name }}
  date: {{ now | htmlDate }}
  version: {{ .Chart.Version }}
{{- end }}


{{- define "cron_job_command" }}
- /bin/sh
- -c
- date; echo {{ .Values.release.cron_job_command_name }} from the Kubernetes cluster
{{- end }}



