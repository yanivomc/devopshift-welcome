helm install  spring-music  ./spring-music --debug --dry-run --set release.env=LOCA


kubectl get svc

<!-- NAME                          TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes                    ClusterIP      100.64.0.1      <none>                                                                    443/TCP        154m
spring-music-spring-service   LoadBalancer   100.65.95.197   a2dede67f50174027a48550daf8d6af8-1445878588.eu-west-1.elb.amazonaws.com   80:30312/TCP   3m26s -->