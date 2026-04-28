
```bash
DI has three liftimes types
- **Transient** → multiple instances per request even one request contains                multiple instanses for many classes needes my added services, it will              "create multiple instances per request".
  
- **Scoped** → one instance per request even my request                                   needs multiple instanse for classes inside it,                                     "it will create one instance per request".  
  
- **Singleton** → one instances for entire app "shared by all requests".  


in add{T}<Iinterface,interfaceImplementaion> : 
        which means when anyone needs my interface 
        ---> go and implement its implementaion "Mapping"  
        this way gives high flexibality any time i want to change the implemtaion.

## default and commom is scopped
```
  