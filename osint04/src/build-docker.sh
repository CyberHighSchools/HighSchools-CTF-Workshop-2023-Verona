#!/bin/bash

set -ex

########### ENV VARS ###########
IMAGE=osint_cryptosgamo
HOSTNAME=cybrmnksohq46mrky5oqrkj4zp4l7uq4zy5w54ih3crvu3lczi6xfeid.onion
################################

docker rm -f $IMAGE \
    && \
docker build \
    --tag=$IMAGE:latest . \
    --build-arg HOSTNAME=$HOSTNAME \
    && \
docker run -it --rm \
    --name $IMAGE \
    --hostname cybrmkns \
    -p 8050:8050 \
    $IMAGE
