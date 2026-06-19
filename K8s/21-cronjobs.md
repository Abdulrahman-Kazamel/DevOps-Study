
1. Create a cronjob named `datacenter`.   
2. Set Its schedule to something like `*/8 * * * *`. You can set any schedule for now.  
3. Name the container `cron-datacenter`.  
4. Utilize the `nginx` image with `latest tag` (specify as `nginx:latest`).  
5. Execute the dummy command `echo Welcome to xfusioncorp!`.   
6. Ensure the restart policy is `OnFailure`.


```bash
cat datacentercronjob.yaml 
apiVersion: batch/v1
kind: CronJob
metadata:
  name: datacenter
spec:
  schedule: "*/8 * * * *" 
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: cron-datacenter
            image: nginx:latest
            command:
            - /bin/sh
            - -c
            - echo "Welcome to xfusioncorp!"
          restartPolicy: OnFailure
          
          
          
kubectl get cronjobs
kubectl get jobs
kubectl get pods
kubectl describe cronjob datacenter


kubectl logs -l job-name=<job-name-from-yaml>
kubectl logs podName
```



1. Create a job named `countdown-devops`.
2. The spec template should be named `countdown-devops` (under metadata), and the container should be named `container-countdown-devops`
3. Utilize image `ubuntu` with `latest` tag (ensure to specify as `ubuntu:latest`), and set the restart policy to `Never`.
4. Execute the command `sleep 5`

```
cat countdown.yaml 
apiVersion: batch/v1
kind: Job
metadata:
  name: countdown-devops
spec:
  template:
    metadata:
      name: countdown-devops
    spec:
      containers:
      - name: container-countdown-devops
        image: ubuntu:latest 
        command: ["/bin/sh", "-c", "sleep 5"]
      restartPolicy: Never  
  backoffLimit: 4 
```