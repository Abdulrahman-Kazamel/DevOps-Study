
```
ssh -i privateKey.pem -l user ip


```

### ssh tunnel from one server to another to connect directly to a private instance through your bastion host


```
ssh -i privateKey.pem -f -N -L portNumber:thedbendpointORitsDNS:portNumber BationUser@IP -v 
```