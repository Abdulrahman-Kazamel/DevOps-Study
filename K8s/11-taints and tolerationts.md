---> Control WHICH Pods can run on WHICH Nodes.
# Taint Effects

| Effect           | Meaning                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| NoSchedule       | Prevent new Pods and keep old pods                                                                     |
| PreferNoSchedule | Avoid if possible, used with master node, to avoid putting new pods and only accept in case mandatory. |
| NoExecute        | deletes the old and keep the new with keys                                                             |


```bash
#add taint
kubectl taint nodes node01 app=skywolf:NoSchedule

#remove taint
kubectl taint nodes node01 app=skywolf:NoSchedule-


### yaml configration under the spec 
tolerations:
  - key: "app"
	opertaor: "Equal"
	value: "blue"
	effect: "noSchadule"

## another example

apiVersion: v1
kind: Pod
metadata:
  labels:
    run: nginx-container
  name: nginx-container
spec:
  tolerations:
  - key: "app"
    operator: "Equal"
    value: "test"
    effect: "NoSchedule"
  containers:
  - image: nginx:latest
    name: nginx-container
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```




```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx-deployment
  name: nginx-deployment
  namespace: dev

spec:
  replicas: 4

  selector:
    matchLabels:
      app: nginx-deployment

  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1

  template:
    metadata:
      labels:
        app: nginx-deployment

    spec:
      tolerations:
      - key: "dedicated"
        operator: "Equal"
        value: "dev"
        effect: "NoSchedule"

      containers:
      - name: nginx
        image: nginx:1.20

        ports:
        - containerPort: 80

        resources: {}
```