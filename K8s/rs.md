
### here is the task

here is the task : The Nautilus DevOps team is gearing up to deploy applications on a Kubernetes cluster for migration purposes. A team member has been tasked with creating a ReplicaSet outlined below: Create a ReplicaSet using nginx image with latest tag (ensure to specify as nginx:latest) and name it nginx-replicaset. Apply labels: app as nginx_app, type as front-end. Name the container nginx-container. Ensure the replica count is 4.


```yaml
thor@jump-host ~$ cat replicaset.yaml 
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