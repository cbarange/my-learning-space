# Kubernetes
> cbarange | 12th October 2020
---

**Une architecture conteneurisée**
* Monolithic → Microservice
* Cycle de développement long → Cycle de développement court
* Mise en production peu fréquente → Mise en production fréquente
* Scaling vertical → Scaling horizontal
* \+ Automatisation des tests et d'intégration
* \+ Application portable

Pour gérer les containers on utilise un orchestrateur, Kubernetes (K8s) est un système open-source d'ochestration de conteneurs qui par defaut exécute des containers docker. 

Il existe plusieurs façon d'utiliser kubernetes, en locale avec minikube, solution hébergée AWS-EKS Google-GKE Azure-AKS, solution on-promise avec Kubespray ou kubeadm ou bien avec K3s est un package de moins de 40MB certifié par Kubernetes. Il comprend toutes les dépendances et peut s'éxécuter sur des architectures ARM64 ou ARMv7. [Avantage de K3s](https://www.it-wars.com/posts/cloud-native/kubernetes-avec-k3s-pour-sauver-la-planete/). 

> Pour aller plus loins et provisionner automatiquement des machines dans le cloud : [Ansible](https://blog.zwindler.fr/2019/03/21/deployer-en-5-minutes-un-cluster-kubernetes-sur-arm-avec-k3s-et-ansible/)

## Setup & Installation : On-Premise
> Cours de Google : https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615

> Cours linkedin learning : https://www.linkedin.com/learning/l-essentiel-de-kubernetes/aborder-les-prerequis-pour-installer-on-premise?u=43271628

> Tutoriel officiel : https://kubernetes.io/docs/tutorials/kubernetes-basics/

> Présentation des concepts : https://medium.com/@coopTilleuls/introduction-%C3%A0-kubernetes-utilisation-partie-2-8ed54e3246b2

> Choisir son installeur : https://github.com/kubernetes-sigs/kubespray/blob/master/docs/comparisons.md

> Kubeadm : https://kubernetes.io/fr/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

> Kubespray : https://kubernetes.io/fr/docs/setup/custom-cloud/kubespray/

> Kubespray + Ansible : https://www.civo.com/learn/getting-started-with-kubernetes

**Mots Clés**
* Nodes : machines physiques ou virtuelles connectées au master
* Noeud : Ensemble de nodes
* Pods : objets kubernetes regroupant un ou plusieurs container, une adresse ip par pods
* Volumes : stockage partagé entre les pods
* Deployments : objects kubernetes décrivant la configuration des pods
* Services : objects kubernetes avec une adresse ip statique pour accéder aux pods qui eux ont une adresse ip dynamiques
* Ingress : Loadbalancer qui expose les services publiquement
* Namespaces : definit la porté des objects

**Notions Clés**
* gestion des applications : pods, deployment, replicaset
* loadbalancing : service, add-on réseau
* configuration des applications : configmap, secret
* stockage : persitent volume, volume claim
* configuration du cluster : metadata, namespace, roles 

**Prérequis minimale pour un K8s :**
* 1 x master : 2 Go de RAM / 16 Go SSD / 2 vCPU
* 2 x worker : 2 Go de RAM / 10 Go SSD / 2 vCPU
* Hostname, Adresse mac et Product_id unique pour chaque machine
* Désactiver le swap
* Ouverture des ports [détails](https://kubernetes.io/fr/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#verify-the-mac-address-and-product-uuid-are-unique-for-every-node)

```bash
# - OS Update - 
sudo apt update
sudo apt upgrade -y
# - Disable Swap and SE linux -
sudo swapoff -a
setenforce 0
# - Check for unique hostname,  mac address and product_id -
ip link
ifconfig -a
sudo cat/sys/class/dmi/id/product_uuid
# - Install kubeadm on master -
apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl

less /var/lib/kubelet/kubeadm-flags.env

systemctl daemon-reload
systemctl restart kubelet




kubeadm init
kubectl apply -f https://raw.githubusercontent.com/coreos/kube-flannel.yml
# - Install kubeadm on workers -
kubeadm join 192.168.116:6443 --token mm20xq?g0xx7p1wzrx75tv3

# - Install kubernetes dashboard on master -
# TODO Kubernetes Dashboard (Check for container from Docker hub)

```

```bash
# - Install kubectl on master -
# Installation de kubectl, l'outil permettant d'interagir avec le master kubernetes
# https://kubernetes.io/fr/docs/tasks/tools/install-kubectl/ 
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl # Telechargement de la dernirere release
chmod +x ./kubectl # Rendre le binaire executable
sudo mv ./kubectl /usr/local/bin/kubectl # Deplace le binaire dans le path
kubectl version --client # Tester le commande
```

## Setup & Installation : Local

```bash
# Minikube est une instance kubernetes mono noeud pour une installation locale sur un poste de developpeur
minikube version
minikube start
# kubectl permet d'interagire avec une instance kubernetes locale ou distante
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



# TODO un cluster Kubernetes fonctionnel et que kubectl est utilisable et correctement configuré.
# Installer Minikube sur sa machine
# Installer Kubernetes avec kops
# Mettre à jour une application
# Le proxy intégré
# Les contrôleurs (déploiements, démons, cronjobs…)
# Les volumes
# Les secrets
# La configuration (configmap)
# La gestion des logs
# Les quotas
# Installation et création de paquets avec Helm
# HTTPS, Let’s Encrypt et Kube Lego
# Gestion dynamique des DNS avec External DNS
# Convertir un fichier docker-compose.yaml avec Kompose
# 
# 

```

## Configurer votre cluster Kubernetes
```bash
kubectl proxy # Lance la console de configuration web de kubernetes
# Utiliser la commande kubectl pour configurer votre K8s puis générer le fichier de configuration ou utiliser directement un fichier de configuration
kubectl get pods --namespace=app --output=yaml # Exemple d'un export de fichier de configuration
kubectl create -f config-file.yaml --namespace=app # Exemple de configuration depuis un fichier de conf
kubectl create namespace app # Creation d'un namespace
kubectl create deployment api-deployment --image=docker-api -n app # Creation d'un objet deployment
kubectl run api-deployment --image=docker-api -n app # create ne permet pas de gerer le nombre de pods repliquer utiliser plutot la commande run
# --- Exemple---  
kubectl run api-deployment --image=docker-api --port=9000 --replicas=1 --env="APP_ENV=dev" --labels="app=api" -n app
kubectl run users-deployment --image=docker-users --port=9000 --replicas=1 --env="APP_ENV=dev" --labels="app=users" -n app
kubectl run nginx-deployment --image=docker-nginx --port=80 --labels="app=nginx" -n ap
kubectl get deployments -n app
kubectl delete pods -l app=users -n app # Suppresion du pod avec le label user, le pod sera instantanément recree puisqu'il est décrit dans l'object deployment
kubectl scale deployment users-deployment --replicas=3 -n app # Repliquer un pods, voir la commande autoscale
# --- === ---

kubectl expose deployment api-deployment --port=9000 # Configurer les Services pour acceder aux pods
kubectl expose deployment users-deployment --port=9001 --target-port=9000
kubectl expose deployment nginx-deployment --port=80 --type=NodePort
kubectl get services -n app
# Il n'existe pas de commande pour créer un ingress utiliser la conf suivante
"
# ingress.yaml :
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress
spec:
  rules:
  - http:
      paths:
      - path: /app
        backend:
          serviceName: nginx
          servicePort: 80
"
kubectl get ingress -n app
```


