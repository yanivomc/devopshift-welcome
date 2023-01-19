kubectl apply -f volumes-pods.yaml 

kubectl exec -ti volumes-pod -c app2 -- ash
cd storage/
touch from_app1
exit

 kubectl exec -ti volumes-pod -c app1 -- ash
 cd /storage/
touch from_app2
exit



