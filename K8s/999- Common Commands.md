
```

minikube start
kubectl status
kubectl get pods
kubectl get services
kubectl get svc
kubectl cluser-info
kubectl describe serviceName
kubectl describe pod nginx
kubectl get ns
kubectl get deployments
kubectl get pod nginx -o yaml
kubectl get nodes -o json | jq '.items[].status.nodeInfo'

kubectl port-forward pod/pod-name 8080:80



kubectl create deployment testdeploy --image httpd --replicas 4 -o yaml --dry-run=client>httpd.yml


kubectl apply -f httpd.yml

auto schaduler --> filitering , scoring, binding 

in manual schaduler --nodeName above containers word


kubectl create deployment killer0eploy --image nginx --replicas 3 -o yaml --dry-run=client>nginx.yaml


kubectl run pod-nginx --image=nginx:latest --restart=Never --labels="app=nginx_app" --dry-run=client -o yaml > pod-nginx.yaml


or 

kubectl run pod-nginx \
  --image=nginx:latest \
  --restart=Never \
  --labels="app=nginx_app" \
  --dry-run=client -o yaml > pod-nginx.yaml
  
  
  ### Labels Placement

- Labels go under **metadata**, NOT inside spec

✔️ Correct:

metadata:  
  labels:  
    app: nginx_app

❌ Wrong:

spec:  
  labels:
  
  
  
  
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




```
