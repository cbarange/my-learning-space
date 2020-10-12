# Kubernetes
> cbarange | 12th October 2020
---

Kubernetes (K8s) est un système open-source d'ochestration de conteneurs

K3s est un package d'un seul binaire de moins de 40MB, il est certifié comme distribution de Kubernetes. Il comprend toutes les dépendances et peut s'éxécuter sur des architectures ARM64 ou ARMv7. [Avantage de K3s](https://www.it-wars.com/posts/cloud-native/kubernetes-avec-k3s-pour-sauver-la-planete/)

Aller plus loins avec [Ansible](https://blog.zwindler.fr/2019/03/21/deployer-en-5-minutes-un-cluster-kubernetes-sur-arm-avec-k3s-et-ansible/)

## Setup & Installation

**Configuration minimale pour un K3s :**
* 1 x master : 2.0 Go de RAM / 10 Go SSD / 2 vCPU
* 2 x worker : 1.5 Go de RAM / 10 Go SSD / 2 vCPU

```bash
# https://www.civo.com/learn/getting-started-with-kubernetes
apt update
apt upgrade -y

# Install K8s

# Kubernetes Dashboard (Check for container from Docker hub)

```

```bash
minikube version
minikube start
# 2.5 Ram 2vCpu 14Go Disk
kubectl version
kubectl cluster-info
kubectl get nodes
kubectl create deployment


kubectl get # list resources
kubectl get pods
kubectl describe # show detailed information about a resource
kubectl describe pods
kubectl logs # print the logs from a container in a pod
kubectl exec # execute a command on a container in a pod


```

## 

## 


