#!/bin/bash

name="poem"
if [[ -n $(docker ps | grep $name) ]];then
echo 'Now stop the container...'
docker stop $name
echo 'Now delete the container...'
docker rm $name
fi

if [[ -n $(docker images | grep $name) ]];then
echo 'Now delete the image...'
docker rmi $name
fi

echo 'Now build the new image...'
docker build -t $name .
echo 'Now run the new image...'
docker run --name $name -d -p 5555:5555 $name