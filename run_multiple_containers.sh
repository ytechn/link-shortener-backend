docker run -p 7000:8080 -v ./data/:/app/data/ link-shortener-devops &
docker run -p 7001:8080 -v ./data/:/app/data/ link-shortener-devops &
docker run -p 7002:8080 -v ./data/:/app/data/ link-shortener-devops &

wait
