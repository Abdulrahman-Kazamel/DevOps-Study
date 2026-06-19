

```bash
#mount the current directory to /app 
docker run -p 5173:5173 -v "$(pwd):/app" -v /app/node_modules react-docker:latest
```