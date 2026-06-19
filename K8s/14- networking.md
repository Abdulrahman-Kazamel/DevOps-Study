# Kubernetes Networking Rules

Kubernetes networking follows:

1. Every Pod gets IP
2. Pods communicate directly
3. No NAT between Pods
4. Services provide stable access

---
## What is CNI?

Container Network Interface, Responsible for Pod networking.

Popular CNI plugins:

|Plugin|Notes|
|---|---|
|Calico|most popular|
|Flannel|simple|
|Cilium|eBPF|
|Weave|older|

---
# kube-proxy

Handles Service networking.
Responsible for:

- iptables rules
- forwarding traffic
- load balancing

---
### DNS in Kubernetes

CoreDNS provides DNS service.
Example: myservice.default.svc.cluster.local

====> Pods use service names instead of IPs.


---

