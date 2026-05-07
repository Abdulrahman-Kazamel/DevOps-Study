

![[Pasted image 20260429204420.png]]




![[Pasted image 20260429204442.png]]

kubectl get events -n resourseName 

![[Pasted image 20260429204825.png]]



- **`maxSurge`**: Controls how many extra Pods can be created above the desired count, allowing for faster updates.
- **`maxUnavailable`**: Determines the maximum number of Pods that can be offline during the rollout, ensuring service availability.