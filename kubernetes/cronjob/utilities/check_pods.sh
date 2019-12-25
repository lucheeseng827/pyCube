#!/bin/bash

#Kube check on stale pods which are terminating and Unknown, this will perfrom force deletion on the pods via kubectl
#this is to check if pods are running or terminating or  unknown status

#eg: you will need to pass namespaces when run this script
# ./check_pods.sh <namespace1> <namespaces2> ..


#Terminating, Unknwon, ImagePullBackOff, ErrImagePull, ImagePullBackOff
for i in  "$@"
do
for pod in  $(kubectl get pods -n $i | grep -e "Terminating" -e "Blocked" -e "Error" -e "Unknown" -e "Evicted" -e "ImagePullBackOff" -e "CrashLoopBackOff" -e "Completed" -e "ContainerCreating" | awk '{print $1}');
do
        echo "Deleting pod $pod";
        kubectl delete pod $pod -n $i  --grace-period 0 --force
done
done