# RUN WITH Docker

```
docker build . --tag devops-link-shortener
docker run -p 8000:8000 -v data:/app/data devops-link-shortener
```
