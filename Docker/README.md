**_На основном сервере:_**
touch project_folder/docker-compose.prod.yaml
cd project_folder
docker-compose up
docker swarm init
  _копируем команду_

**_На worker:_**
docker swarm join --token [token] [IP:port]

**_На основном сервере:_**
docker stack deploy --with-registry-auth -c ./docker-compose.prod.yaml gbstack;

