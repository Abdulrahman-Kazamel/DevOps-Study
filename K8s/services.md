

clusterip  ====> internal access for any pods has clusterip ,also there is no isolation  between clusterip and the other ..

it's preferred to create clusterip to each deployment  


the service opens access to pods inside the  cluster, and if the pod has no service , it will access the other services but no pod will access it.


external