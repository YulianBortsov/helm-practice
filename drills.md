DRILL-01: Create Chart
- helm create mychart
- cd mychart
- delete contents of templates/ (keep _helpers.tpl)
- edit Chart.yaml: change version and description

DRILL-02: Basic Pod
- create templates/pod.yaml
- define single nginx pod
- helm template . 
- fix any errors

DRILL-03: Values
- edit values.yaml: add image=nginx, tag=latest
- update pod.yaml to use values
- helm template .
- change values, test again

DRILL-04: Simple Deployment
- create templates/deployment.yaml
- add replicas=3 to values.yaml
- helm template .
- helm lint

DRILL-05: Service
- create templates/service.yaml
- add service port to values.yaml
- helm template .
- change service type ClusterIP/NodePort

DRILL-06: Labels
- add common labels to _helpers.tpl
- use labels in all resources
- helm template .

DRILL-07: ConfigMap
- create templates/configmap.yaml
- add some config data in values.yaml
- reference in deployment
- helm template .

DRILL-08: Simple Conditional
- add enabled: true/false to values.yaml
- wrap resource in if statement
- test both conditions

DRILL-09: Environment Variables
- add env vars to values.yaml
- update deployment to use them
- helm template .

DRILL-10: Resource Limits
- add CPU/memory limits to values.yaml
- update deployment
- helm template .

DRILL-11: Probes
- add readiness probe to deployment
- add liveness probe
- helm template .

DRILL-12: Multiple Containers
- update deployment with sidecar
- add sidecar values
- helm template .

DRILL-13: Package
- helm package .
- helm install --dry-run
- helm uninstall

DRILL-14: Ingress
- create templates/ingress.yaml
- add ingress values
- test with different hosts

DRILL-15: Secrets
- create templates/secret.yaml
- add secret values
- reference in deployment
- helm template .

DRILL-16: Volume Mounts
- add persistent volume claim
- add volume mount to deployment
- helm template .

DRILL-17: Named Templates
- create reusable template in _helpers.tpl
- use in multiple resources
- helm template .

DRILL-18: Chart Dependencies
- add dependency in Chart.yaml
- helm dependency update
- helm dependency list

DRILL-19: Multiple Values Files
- create prod-values.yaml
- create dev-values.yaml
- test with different files

DRILL-20: Debug
- helm lint
- helm template --debug
- intentionally break something
- fix it
