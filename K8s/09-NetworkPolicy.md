# ingress - egress / inbound - outbound

Controls traffic between Pods.

Without NetworkPolicy: - all Pods communicate freely
With NetworkPolicy: - restrict communication

```bash
# allow frontend to backend only:

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy

metadata:
  name: backend-policy

spec:
  podSelector:
    matchLabels:
      app: backend

  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
```



Ingress manages: inbound traffic

- External HTTP/HTTPS traffic
- Routing
- TLS
- Host-based routing

Example:

```
app.company.com → frontend service
api.company.com → backend service
```


# Ingress Controller

Ingress itself is just rules, Needs controller to work.

Popular controllers:

|Controller|Notes|
|---|---|
|NGINX Ingress|most common|
|Traefik|simple|
|HAProxy|fast|