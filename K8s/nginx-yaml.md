```yaml
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
    name: nginx_container
    ports:
	  - containerPort: 80
	    name: http
	    protocol: TCP
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}


```