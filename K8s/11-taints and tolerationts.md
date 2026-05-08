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