
rolling works only if something related to pod templeate but if related to replica set as scalling up or down , it's not affected

rolling update ----> takes two option , up one and delete one
rolling recreate ---> takes all ns down , then up the new ns


```
kubectl create deployment rolling-demo --image nginx:1.23 --replicas 4 -o yaml --dry-run=client 
```

![[Pasted image 20260429191052.png]]


```bash
 kubectl create deployment rolling-revions --image nginx:1.24 --replicas 15 --dry-run=client -o yaml >> myrolling.yaml


 cat myrolling.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rolling-revions
  labels:
    app: rolling-revions

spec:
  replicas: 15
  selector:
    matchLabels:
      app: rolling-revions
  strategy: 
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      labels:
        app: rolling-revions
    spec:
      containers:
      - image: nginx:1.24
        name: nginx
        resources: {}
status: {}
root@controlplane:~$ kubectl set image deployments/rolling-revions nginx:1.25
error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'
root@controlplane:~$ kubectl set image deployments/rolling-revions nginx=nginx:1.25
deployment.apps/rolling-revions image updated




```
grep -A10 
### rolling recreate


```bash
kubectl create deployment rolling-revions --image nginx:1.24 --replicas 15 --dry-run=client -o yaml >> rollingrecreate.yaml

cat rollingrecreate.yaml 
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: rolling-revions
  name: rolling-revions
spec:
  replicas: 15
  selector:
    matchLabels:
      app: rolling-revions
  strategy: 
    type: Recreate
  template:
    metadata:
      labels:
        app: rolling-revions
    spec:
      containers:
      - image: nginx:1.24
        name: nginx
        resources: {}
status: {}



```