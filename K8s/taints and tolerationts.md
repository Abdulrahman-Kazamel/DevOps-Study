

noSchdule  ==> keep the old 
noExcute  ===> deletes the old and keep the new with keys
prefernoschdule ==> for the master node, to avoid putting new pods and only accept in case mandatory. 


kubectl taint nodes node01 app=skywolf:noschdule 
kubectl taint nodes node01 app=skywolf:noschdule- 


```
tolerations:
	key: "app"
	opertaor: "Equal"
	value: "blue"
	effect: "noSchadule"

```

effect wrote on pod container specs for matching 




example


```
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