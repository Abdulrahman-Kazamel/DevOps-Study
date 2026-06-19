

# Kubernetes Security Layers

|Layer|Example|
|---|---|
|Cluster|RBAC|
|Pod|SecurityContext|
|Network|NetworkPolicy|
|Secrets|sensitive data|
|Images|image scanning|

---

# SecurityContext

Controls container permissions.
Example:
```
securityContext: 
  runAsUser: 1000
  runAsNonRoot: true
```

---

# Pod Security Risks

Bad practice:

```
privileged: true
```

This gives container root-like host access.