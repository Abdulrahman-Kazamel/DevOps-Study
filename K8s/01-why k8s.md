
## What is Kubernetes?

Kubernetes is a container orchestration platform used to:

- Deploy containers
- Scale applications
- Self-heal failed workloads
- Manage networking
- Automate rollouts and updates

It mainly manages containers running through runtimes like:

- containerd
- CRI-O
- Docker (older environments)
---
# 02 - Why Do We Need Kubernetes?

Without Kubernetes:

- Containers are manually managed
- No automatic recovery
- Scaling is manual
- Hard to manage many servers

---
## Core Benefits

### 1. Auto Scaling

Kubernetes can increase or decrease Pods automatically based on:

- CPU usage
- Memory usage
- Custom metrics

Example:

- Traffic increases → create more Pods
- Traffic decreases → remove unused Pods

---
### 2. Self-Healing

If a Pod crashes:

- Kubernetes detects failure
- Creates a new Pod automatically

This happens because Kubernetes always (compares) tries to match:
#### Desired State vs Current State stored in etcd

---
# 03 - Desired State vs Current State

This is one of the MOST important Kubernetes concepts.

Kubernetes continuously compares:

|Type|Meaning|
|---|---|
|Desired State|What SHOULD exist|
|Current State|What ACTUALLY exists|

Example:

Desired:
```
replicas: 3
```
Current:
```
Only 2 Pods are running
```
**Kubernetes notices the mismatch and creates another Pod.**

---

#  04 - What is etcd?

etcd is the Kubernetes database, It stores cluster information as key-value data.

Examples stored inside etcd:
- Deployments
- Services
- Secrets
- ConfigMaps
- Cluster state
- Desired configuration
---
# 05 - Kubernetes Architecture

## A- Control Plane Components

The Control Plane manages the cluster.

Main components:

|Component|Responsibility|
|---|---|
|API Server|Entry point to Kubernetes|
|etcd|Stores cluster data|
|Scheduler|Chooses worker node|
|Controller Manager|Maintains desired state|
## B- Worker Node Components

| Component         | Responsibility         |
| ----------------- | ---------------------- |
| kubelet           | Talks to Control Plane |
| Container Runtime | Runs containers        |
| kube-proxy        | Handles networking     |
|                   |                        |

---
# 06 - How Kubernetes Works Internally

Flow Example  


When you run:

```
kubectl apply -f app.yaml
```

The flow is:

1. `kubectl` sends request to API Server
2. API Server validates request
3. Desired state stored in etcd
4. Scheduler selects best node
5. Controller Manager (or deployment??) creates ReplicaSet
6. ReplicaSet creates Pods
7. kubelet on worker node starts containers
8. kubelet reports Pod status back
9. API Server updates etcd

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