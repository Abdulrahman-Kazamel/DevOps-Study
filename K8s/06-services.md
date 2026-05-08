
#### Why Service?
----> Pods are temporary, When Pod IP changes: -> Users lose access

Service gives:
- Stable networking
- Stable DNS
- Load balancing

#### Service Types

## ClusterIP (Default)

Internal communication ONLY.

Used between:

- Pods
- Deployments
- Internal microservices

====>  there is no isolation  between clusterip and the other ..
====> it's preferred to create clusterip to each deployment  

### external 

## A- NodePort

Exposes application externally using:

```
NodeIP:Port
```

## B- LoadBalancer

Used in cloud providers.

Creates external cloud load balancer.


#### important note
====> the service opens access to pods inside the  cluster, and if the pod has no service , it will access the other services but no pod will access it.