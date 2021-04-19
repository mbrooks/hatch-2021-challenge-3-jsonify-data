#!/bin/bash

docker build -t hatch-2021 .
docker run -it --rm --name hatch-2021 hatch-2021