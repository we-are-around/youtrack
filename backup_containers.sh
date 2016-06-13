#!/bin/bash	

# Local backups
container_store_path="/root/backups"	

# Around HUB
repo="wearearound/youtrack"

# Container List
container="around-youtrack"

# Docker Hub Login
hub_pwd="Sarasa12"
hub_usr="wearearound"

# Log on to Docker Hub
docker login --username $hub_usr --password $hub_pwd

# prepare dinamic image and container variables
image=$(docker images|grep $repo|grep latest|awk '{print $3}')	
container_id=$(docker ps |grep $container|awk '{print $1}')

# Archive week day RUNNING Container on DockerHUB
docker rmi $repo:backup-$(date +%u)
docker commit -p -a "Francisco Palacios" -m "Dayly Backup" $container $repo:backup-$(date +%u)
docker push wearearound/youtrack:backup-$(date +%u)

# Archive latest RUNNING Container on DockerHUB
docker rmi $repo:latest
docker commit -p -a "Francisco Palacios" -m "Dayly Backup" $container $repo:latest
docker push wearearound/youtrack:latest

# Local Archive 
#docker save -o $container_store_path/$container.$(date	+%F).tar $image

