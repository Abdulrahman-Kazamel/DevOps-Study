
# Why Secrets?

Never hardcode: the (- passwords - API keys - tokens) inside YAML.



---

# Secret Types

|Type|Purpose|
|---|---|
|Opaque|generic|
|docker-registry|registry auth|
|tls|certificates|

---
```bash
# Create Secret


kubectl create secret generic db-secret --from-literal=username=admin --from-literal=password=123456

# View Secrets

kubectl get secrets

# Use Secret in Pod

env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password
```

---

#### Important

---> Secrets are Base64 encoded. NOT encrypted by default.