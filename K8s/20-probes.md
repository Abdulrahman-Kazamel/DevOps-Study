


```
          readinessProbe:

            httpGet:

              path: /health

              port: 3306

              initialDelaySeconds: 5

              periodSeconds: 5

  

          livenessProbe:

          httpGet:

            path: /health

            port: 3306

            initialDelaySeconds: 15

            periodSeconds: 20
```