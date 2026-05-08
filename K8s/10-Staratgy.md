
### A- RollingUpdate Strategy

Updates Pods gradually.

Example:

- Create 1 new Pod
- Delete 1 old Pod

-----------> Zero downtime.
## takes two Parameters

| Parameter      | Meaning                            |
| -------------- | ---------------------------------- |
| maxSurge       | Extra Pods allowed to be created   |
| maxUnavailable | Max unavailable Pods to be deleted |


rolling works only if something related to pod template but if related to replica set as scaling up or down , it's not affected



### B- Rolling Recreate 
---> from its name ===> takes all ns down (All old Pods are terminated FIRST.)
 then up the new ns (Then new Pods start) and This causes downtime..




#### Rollout Commands
```bash
### for example 
kubectl create deployment rolling-demo --image nginx:1.23 --replicas 4 -o yaml --dry-run=client 

## rollout 
kubectl set image deployment/nginx-deployment nginx-container=nginx:1.19

## Check Rollout Status
kubectl rollout status deployment/nginx-deployment

### Rollback
kubectl rollout undo deployment/nginx-deployment

```

```bash
###example


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



kubectl set image deployments/rolling-revions nginx:1.25

#error: there is no need to specify a resource type as a separate argument when passing arguments in resource/name form (e.g. 'kubectl get resource/<resource_name>' instead of 'kubectl get resource resource/<resource_name>'

 kubectl set image deployments/rolling-revions nginx=nginx:1.25
deployment.apps/rolling-revions image updated


```
### rolling recreate example


```bash
  strategy: 
    type: Recreate
    
 
```

### scenario

An application currently running on the Kubernetes cluster employs the nginx web server. The Nautilus application development team has introduced some recent changes that need deployment. They've crafted an image `nginx:1.19` with the latest updates.

  

Execute a rolling update for this application, integrating the `nginx:1.19` image. The deployment is named `nginx-deployment`.

Ensure all pods are operational post-update.

`Note:` The `kubectl` utility on the `jump-host` has been configured to work with the Kubernetes cluster.



```bash
kubectl set image deployment/nginx-deployment nginx-container=ngi
nx:1.19
deployment.apps/nginx-deployment image updated
thor@jump-host ~$ kubectl rollout status deployment/nginx-deployment 
deployment "nginx-depl"


#View details of a specific revision
kubectl rollout history deployment/<deployment-name> --revision=<number>


#Revert to a specific revision
kubectl rollout undo deployment/<deployment-name> --to-revision=<number>

#check the rollout status
kubectl rollout status deployment/

```