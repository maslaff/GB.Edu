**_На основном сервере:_**
```
touch project_folder/docker-compose.prod.yaml
cd project_folder
docker-compose up
docker swarm init
```
  _копируем команду_

**_На worker:_**
```
docker swarm join --token [token] [IP:port]
```

**_На основном сервере:_**
```
docker stack deploy --with-registry-auth -c ./docker-compose.prod.yaml gbstack;
```
![image](https://github.com/maslaff/GB.Edu/assets/33765993/e803c0f4-f6c9-4c6a-9442-808eb2ff954f)
![image](https://github.com/maslaff/GB.Edu/assets/33765993/28e1bd7e-69e8-42ac-a37c-9fdfe4061c1c)


```
docker stack deploy --with-registry-auth -c ./docker-compose.dev.yaml gbdev
docker stack services gbdev
```
![image](https://github.com/maslaff/GB.Edu/assets/33765993/25e101e3-3423-45f2-9859-9c4d28a6b01b)
![image](https://github.com/maslaff/GB.Edu/assets/33765993/5ab5153d-2b0c-4677-a729-9cdf503a361c)

Позже VPS отключили
![image](https://github.com/maslaff/GB.Edu/assets/33765993/56f497d5-5122-4066-a255-2eb2aafd45cb)
