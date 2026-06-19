
Deployment is good for stateless apps.

Examples:
- frontend
- APIs

But databases need:

- stable identity
- stable storage
- ordered startup

So we use StatefulSet.

---

# Stateful Apps Examples

|App|Why Stateful|
|---|---|
|MySQL|stores data|
|PostgreSQL|persistent DB|
|MongoDB|replication|
|Kafka|broker identity|

---

# StatefulSet Features

|Feature|Meaning|
|---|---|
|Stable hostname|fixed Pod names|
|Persistent storage|PVC per Pod|
|Ordered startup|sequential|
|Ordered deletion|safe shutdown|

---

# Pod Naming

```
mysql-0
mysql-1
mysql-2
```

-----> Names never change.

---

# StatefulSet Example

```
apiVersion: apps/v1
kind: StatefulSet

metadata:
  name: mysql

spec:
  serviceName: mysql-service
  replicas: 3

  selector:
    matchLabels:
      app: mysql

  template:
    metadata:
      labels:
        app: mysql

    spec:
      containers:
        - name: mysql
          image: mysql:8
```

---

# Headless Service

StatefulSets usually use:

```
clusterIP: None
```

This creates direct Pod DNS.