

requests: minim start for each pod 
limits : max for each pod 


```
resources: 
  requests:
    cpu: 300m
    memory: 128Mi
  limits:
    cpu: 600m
    memory: 256Mi
```

if the pod exceeded the limit its run out of memory or throttled cpu and will get into pending state, it creates new pods on different node as per your strategy  


### scalling

```
kubectl scale deployment deploymentsName --replicas 4 
```


