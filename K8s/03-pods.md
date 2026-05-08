## What is a Pod?

A Pod is the SMALLEST deployable unit in Kubernetes.

A Pod can contain:
- One container
- Multiple containers

```
apiVersion: v1
kind: Pod

metadata:
  name: pod-nginx
  labels:
    app: nginx-app

spec:
  containers:
    - name: nginx-container
      image: nginx:latest

    - name: mysql-container
      image: mysql:latest
```

Pod Lifecycle  ==> Pending -> (ContainerCreating) -> Running
pending state --> (startup - live - readiness) probes ----> running

Probes help determine health:

|Probe|Purpose|
|---|---|
|Startup Probe|App startup|
|Liveness Probe|Is app alive?|
|Readiness Probe|Ready for traffic?|


```
apiVersion: v1
kind: Pod

metadata:
  name: nginx
  labels:
    app: nginx
    tier: frontend

spec:
  containers:
  - image: nginx
    name: nginxcontainer
    ports:
    - containerPort: 80
      name: http
      protocol: TCP
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: OnFailure
status: {}
```