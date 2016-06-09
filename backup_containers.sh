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

# Archive RUNNING Container on DockerHUB
image=$(docker images|grep $repo|grep latest|awk '{print $3}')	
container_id=$(docker ps |grep $container|awk '{print $1}')
docker rmi $repo:backup-$(date +%u)
docker commit -p -a "Francisco Palacios" -m "Dayly Backup" $container $repo:backup-$(date +%u)
docker rmi $repo:latest
docker commit -p -a "Francisco Palacios" -m "Dayly Backup" $container $repo:latest

# Local Archive 
#docker save -o $container_store_path/$container.$(date	+%F).tar $image
