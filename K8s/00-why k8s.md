scaling (auto)
self healing
k8 always compares the Current state with desired state stored in etcd


kubectl command talks to the api server and start checking the the current state and the desired state inside or etcd (key: value) database then tell the scheduler start talking to the deployment manger to create a rs which responsible to to keep the the desired state as the current state , for that the rs starts to to talk to the nodes ( kubelet ) to start creating the node runtime to create the container and get back with container (pod) state and node to save them on the controler etcd .


### Scheduler

- Watches for newly created Pods that have no assigned node.
- Selects the best Worker Node for a Pod based on resource requirements, policy constraints, and hardware/software limits.


### why did we need the deployment?
===> without it we will run each pod stand alone , if dropped / failure ,no self healing will happen.


what are three main component of the yaml file.

1-apiVersion, metaData, spec



### does the pod contain only one container?
no, it could contain multipul containers 


```

apiVersion: v1
kind: Pod
metadata:
  name: pod-nginx
  labels:
    app: nginx_app
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      
    - name: mysql-container
      image: mysql:latest

---
apiVersion: v1
kind: Deployment
metedata:
  name: traffic-deployment
  labels:
    app: traffic
    tier: proxy
    
spec:
  selectors:
    matchLabeles:
	   app:traffic
  replicas:2
  template:
	metedata:
	  lablels:
	    app: traffic
	    
    spec:
      containers: 
        - name: proxy
          image: traefik:v2.9
          ports:
            - containerPort: 80
            - containerPort: 443
            - containerPort: 8080
          args: 
            - --api.insecure=true
      
  

```

--- to write multipul configrations on yaml file (---)
if we have a running pod and want to make a port forward

`kubectl port-forward pod/podNAME hostport:podPort`



```
# -oyaml get the configration stored on etcd 
kubectl get pods -l app=nginx -oyaml
```


how user access the pod?

first reaches the ingress then the svc the the dep/app