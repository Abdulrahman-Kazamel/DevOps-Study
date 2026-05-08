### A- Requests & Limits

Requests: Minimum guaranteed / started resources.
Limits : Maximum allowed resources. 

```
resources: 
  requests:
    cpu: 300m
    memory: 128Mi
  limits:
    cpu: 600m
    memory: 256Mi
```

### Enforcement Behavior

- **Exceeding CPU Limits:** The container is **throttled**, meaning its execution slows down, but it is not typically terminated.
- **Exceeding Memory Limits:** The container will likely be terminated with an **OOMKilled** (Out Of Memory) error.  



### Management Strategies

- **LimitRange:** Use a [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/) to set default, minimum, and maximum resource constraints for all containers within a specific namespace.
- **ResourceQuota:** Use a [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) to limit the _total_ aggregate resources (sum of all requests/limits) that can be consumed by a namespace.
- **Quality of Service (QoS):** Kubernetes assigns [QoS classes](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/) (Guaranteed, Burstable, or BestEffort) based on how you set requests and limits. Pods with `requests == limits` for all containers are "Guaranteed" and are the last to be evicted during resource pressure.
- **In-Place Resize:** In newer versions (v1.27+), you can sometimes resize resources for running Pods without a restart using the [in-place resize feature](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/).




### B- Quata


```bash

kubectl create quota demo-quota --hard=cpu=2,memory=2Gi
kubectl create quota demo-quota --hard=pods=10,services=5


kubectl create namespace prod


kubectl create quota demo-quota --hard=requests.cpu="700m",requests.memory=1Gi,limits.cpu="900m",limits.memory=2Gi,pods=5 --dry-run=client -o yaml -n prod > quo.yaml


kubectl get resoursequotas -n testquota 
kubectl get events -n resourseName 


kubectl delete resourcequotas demo-quota -n prod
```



