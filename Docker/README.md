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
![1](https://github.com/maslaff/GB.Edu/assets/33765993/f56fad67-94ab-471c-ba9a-164636f8f67c)
![2](https://github.com/maslaff/GB.Edu/assets/33765993/e962a59b-a366-4561-9d0e-5bdcb5e7b711)

```
docker stack deploy --with-registry-auth -c ./docker-compose.dev.yaml gbdev
docker stack services gbdev
```
![image](https://github.com/maslaff/GB.Edu/assets/33765993/25e101e3-3423-45f2-9859-9c4d28a6b01b)
![image443](https://github.com/maslaff/GB.Edu/assets/33765993/f5f20f07-a5f2-407f-980e-022762a22276)

Позже VPS отключили
![rect488](https://github.com/maslaff/GB.Edu/assets/33765993/d356db9f-6122-47c7-a2df-c30f420c16ae)
