## Important Rule

Labels go under: metedata


```

metadata:
  name: nginx-deployment
  labels:
    app: nginx-app

spec:
  selector:
    matchLabels:
      app: nginx-app

  template:
    metadata:
      labels:
        app: nginx-app
        type: frontend


```

what is the difference between 

```
metadata:
  labels:
    app: nginx-app
    
    and
spec:
  selector:
    matchLabels:
      app: nginx-app
      
      and 
      
  template:
    metadata:
      labels:
        app: nginx-app
        type: frontend
```




labels: error: resource mapping not found for name: "pod-nginx"