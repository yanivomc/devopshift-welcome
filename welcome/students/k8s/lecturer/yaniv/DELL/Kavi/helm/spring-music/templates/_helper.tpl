{{ define "spring.labels"}}
generator: helm
app-name : {{.Chart.Name}}
date: {{ now | htmlDate }}
name: {{ .Release.Name }}
{{end}}

