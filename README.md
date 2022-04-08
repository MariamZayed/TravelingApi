## First: Install Docker

```
sudo apt install docker.io
```
## Second: Install docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```

```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

## Now: Let's build our docker

```
sudo docker-compose up --build
```

## Hola! Now our Docker run with nginx
![](https://i.imgur.com/NdpgUsm.png)
