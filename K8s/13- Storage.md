# Why Storage

Containers are ephemeral.

Means: - if Pod dies -> data inside container is LOST

Example: mysql pod deleted ---> database files deleted


# Storage Components

| Component                   | Purpose                      |
| --------------------------- | ---------------------------- |
| Volume                      | Temporary storage inside Pod |
| PersistentVolume (PV)       | Real storage in cluster      |
| PersistentVolumeClaim (PVC) | Request storage              |
| StorageClass                | Dynamic storage provisioning |


# EmptyDir Volume

temporary storage shared between containers inside same Pod.
====> Deleted when Pod deleted.


```
apiVersion: v1
kind: Pod

metadata:
  name: emptydir-demo

spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - mountPath: /cache
          name: cache-volume

  volumes:
    - name: cache-volume
      emptyDir: {}
```


### Persistent Volume (PV)

actual storage resource.
==> Example: - EBS - NFS - Azure Disk - Local SSD

### Persistent Volume Claim (PVC)
application requests storage from PV.
Pod  --> PVC --> PV --> Real Disk


### PVC Example

```
apiVersion: v1
kind: PersistentVolumeClaim

metadata:
  name: nginx-pvc

spec:
  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 1Gi

```
---
### Using PVC Inside Pod

```
apiVersion: v1
kind: Pod

metadata:
  name: nginx-storage

spec:
  containers:
    - name: nginx
      image: nginx

      volumeMounts:
        - mountPath: /usr/share/nginx/html
          name: web-storage

  volumes:
    - name: web-storage
      persistentVolumeClaim:
        claimName: nginx-pvc
```

----
# StorageClass

automatically creates storage dynamically.

Without StorageClass: - admin manually creates PV
With StorageClass: - Kubernetes creates PV automatically


# Access Modes

|Mode|Meaning|
|---|---|
|ReadWriteOnce|one node write|
|ReadOnlyMany|many nodes read|
|ReadWriteMany|many nodes write|
