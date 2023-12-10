## Docker Run CLI:
-t > --tty
-p > --publish list (ports config)
-v > --volume list
-i > --interactive
-d > --detach

## Build & Run Commands:
docker inspect [imagename]                                                              // metadata of the object
                                                                                        // wget https://github.com/yanivomc/seminars/raw/master/docker/artifacts/spring-music.jar
docker images                                                                           // 
docker build -t [repo]/[imagename]:[tag] .                                              // example: `docker build -t nivswi/nivapp:1 .`  (repo = account id = nivswi) 
docker run -ti -p [external-port:internal-port] [repo/imagename]:[tag]                  // exmaple: `docker run -ti -p 80:8080 nivapp:1`
docker login                                                                            // insert docker hub infos (account id = nivswi, password = email password)
docker push [repo]/[imagename]:[tag]                                                    // exmaple: `docker push nivswi/nivapp:1`
docker tag [old-repo]/[old-imagename]:[old-tag] [new-repo]/[new-imagename]:[new-tag]    // re-tag existing container exmaple: `docker tag nivswi/nivapp:1 nivswi/nivapp:latest`
                                                                                        // example2: `docker run -dti -p 80:8080 -v "$pwd":/var/tmp nivswi/nivapp:1 ash`

## Volume Commands:
docker run -v [machine-data]/[volumename]:[container-data] [repo]/[imagename]:[tag]     // example1: `docker run -ti -v /var/tmp:/var/conttmp nivswi/nivapp:1`
docker volume inspect [repo]/[imagename]:[tag]                                          // 
docker volume create [volume-name]                                                      // create managed volume, example: `docker volume create fs_shared`
docker volume ls                                                                        // shows managed volumes
docker run --rm -tdi --name [imagename] -v [volumename]:[container-data] alpine sh      // run & mount example: `docker run --rm -tdi --name alpine2 -v fs_shared:/app alpine sh`

docker exec -it [container-id] ash                                                      // run docker shell