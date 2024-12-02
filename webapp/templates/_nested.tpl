{{- define "example.nested" -}}
nestedValue: {{ .nestedContext.nestedKey }}
globalValue: {{ .globalKey }}
{{- end -}}