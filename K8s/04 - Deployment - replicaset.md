
## Why Do We Need Deployment?

Without Deployment:

- Pods run independently
- No self-healing
- No rolling updates
- No scaling management

Deployment provides:

- Replica management
- Rolling updates
- Rollback
- Self-healing

---

###  ReplicaSet

## What is ReplicaSet?

ReplicaSet ensures a fixed number of Pods are always running.

Example: ===> Desired: `replicas: 4`

If one Pod dies: ReplicaSet creates another Pod

---

### ReplicaSet Example

```
apiVersion: apps/v1
kind: ReplicaSet

metadata:
  name: nginx-replicaset
  labels:
    app: nginx-app
    type: frontend

spec:
  replicas: 4

  selector:
    matchLabels:
      app: nginx-app

  template:
    metadata:
      labels:
        app: nginx-app
        type: frontend

    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
```

---

### Deployment Example


```
apiVersion: apps/v1
kind: Deployment

metadata:
  name: traffic-deployment
  labels:
    app: traffic
    tier: proxy

spec:
  replicas: 2

  selector:
    matchLabels:
      app: traffic

  template:
    metadata:
      labels:
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
 

### or
```
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx-deployment
  labels:
    app: nginx-app

spec:
  selector:
    matchLabels:
      app: nginx-app

  template:
    metadata:
      labels:
        app: nginx-app
        type: frontend

    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
          ports:
            - containerPort: 80
              name: http
              protocol: TCP

```
### task
here is the task : The Nautilus DevOps team is gearing up to deploy applications on a Kubernetes cluster for migration purposes. A team member has been tasked with creating a ReplicaSet outlined below: Create a ReplicaSet using nginx image with latest tag (ensure to specify as nginx:latest) and name it nginx-replicaset. Apply labels: app as nginx_app, type as front-end. Name the container nginx-container. Ensure the replica count is 4.


```bash
cat replicaset.yaml 
 
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
  labels:
    app: nginx_app
    type: front-end
spec:
  replicas: 4 
  selector:
    matchLabels:
      app: nginx_app
      type: front-end 
  template:
    metadata:
      labels:
        app: nginx_app
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx:latest
        ports:
        - containerPort: 80
```