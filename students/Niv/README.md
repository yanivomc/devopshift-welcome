
## Commands
                                                                              // `docker push nivswi/nivswi:[tagname]`
                                                                              // wget https://github.com/yanivomc/seminars/raw/master/docker/artifacts/spring-music.jar



docker images                                                                 // 
docker build -t [repo]/[imagename]:[tag] .                                    // example: `docker build -t nivswi/nivapp:1 .`  (repo = account id = nivswi) 
docker run -ti -p [external-port:internal-port] [repo/imagename]:[tag]        // exmaple: `docker run -ti -p 80:8080 nivapp:1`
docker login                                                                  // docker hub (account id = nivswi, password = email password)
docker push [repo]/[imagename]:[tag]                                          // exmaple: `docker push nivswi/nivapp:1`
