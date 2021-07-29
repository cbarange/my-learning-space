# Some memo for IT
> cbarange | 10th December 2020

## Best Practice

Pas plus de 20 lignes par fonction
On Signe et date les commentaires

## Idées de cours

XML

Regex

Asynchrone / Thread

Gestion de projet



## TODO
* wsdl soap rest
* json ld
* ocaml language
* Qubes-os pop-os 
* knapsack algorithm
* Typescript GraphQL TypeGraphQL TypeORM PostgreSQL React Appollo
* NuxtJs tailwindcss 
* Théorie des graphes Grammaire Langages naturels Machine a état Algo déterministe en temps fini ou np complet 
* Multi Tenant Infra as code Moteurs de regles Extrem Programming & Lean software development contrat d'interface
* Mimio container
* Event sourcing
* Apache Pulsar
* X++
* ionic capacitor
* ACID Database
* Python Theano
* Pghash python  Jwt lié à oidc  Felium map python
* Geohash python
* Open Connect : CDN (Content Delivery Network)
* ionic Bootstrap jquery
* CORS Origin
* CPA Database theorem
* InfluxDB
* SOLID principe
* Peer to Peer
* NESTJS socket io / websocket webRTC NAT / PAT sveltejs ws module websocket de node fastify js redux js parcel js/node/webpack
* Programmation Système :  fork pid ppid process pipe ... (En C et en Python)
* XML XLLT
* Redux
* CodistAI
* samba vs nfs
* extension rust & js pour postgresql
* Javascript / TypeScript, HTML5 / CSS3, SASS / LESS, Animation JS, Canvas et SVG, Frameworks Angular, React, Bootstrap NodeJS
* FAIRE UN REGROUPEMENT DES TECHNOS SUIVANT LES OFFRES D'EMPLOIE (faire des bundles de techno, angular+java react+php ...)
* KeepAliveD
* repMGR
* (reverse software) Gidhra & Radare2)
* shodan et shodan.io
* Grafana + NodeJS et Rsyslog et InfluxDB LDAP SAO
* pfsense packettracer
* webhooks
* Python Django Pyramid Web2Py
* Kafka K8S
* programmation impérative | fonctionnelle | object | reactive
* Quasar Stormbase
* koa. js swagger io / open api 
* loopback io JWT
* micro données seo
* google search console
* dashline
* Firebase
* Ember.js
* sass language
* CLIP OS   Distribution Linux Gentoo
* tween Lo-dash
* iam software
* Vue Materialisée database
* logstash rabbitmq
* assembleur
* jq.node
* 3djs svg / svg dynamic
* nginx/openresty
* istio proxy
* postrest subzero postgraphql prisma
* Prometeus
* Helm et Gitlab CI
* laravel
* p5.js

## Questions
* Langage machine, Binaire, Executable
* Pourquoi utilise un framework js type Angular sachant que c'est mauvais pour le référencement SEO ?
  * Utiliser deux site, un site vitrine et un site pour l'application web. Le site vitrine est un word-press ou autre système avec les bonne normes pour le référencement, c'est depuis ce site que l'application web sous javascript est accéssible. Il est très important d'avoir un site vitrine avec des technos facilement référencable.
* Pourquoi développer des langages multi-plateformes si on développent des logiciels en utilisant des fonctions uniques pour l'OS souhaité, les variables d'environnement, les chemins de fichier ...
* Avec tous les middleware RabbitMQ etcetc on ralentit les applications ? pas trop justement ?
* Il faut que développer pour les machines ou pour les développeurs ? (Code optimisé et pointu VS algorithmes et fonctions basiques )
* La création d'un site full back-end est-ce une bonne chose, #django #flask #symphony ?
* C'est le client qui requêtes les webservices ou c'est un middleware qui pourra aussi gérer les sessions, cela permet de ne pas implémenter un système de session dans chaque webservices ?
* Le nommage : 
  * clients VS clientList VS listClient
  * ServiceObjectInterface CS InterfaceServiceObject
  * sNom = "jean" / iAge = 5 VS nom = "jean" age = 5
    * En anglais tous les noms ne prennent pas de s privilégier un nommage allant du plus spécifique au plus générique ex : lastClientList
* Quand on ce déplace en bus avec son téléphone, on change d'antenne 4G. Comment est rétablie la connexion, dans le cas d'un websocket par exemple
* Redux est un anti-patern ?
  * Static est bien un anti-pattern, cependant dans un monde parfait ou latences réseaux réseaux n'existe pas on pourrait requêter la base de données de permanence des qu'une donnée doit être affichée/traitée. 
  * Redux est alors une sorte de cache qui permet de stocker dans le front les données du back. Cela casse le principe de Single Source of Truth, mais c'est aujourd'hui le moyen le plus propre dans le cadre d'une application Front/API/Back.
  * Redux est a utiliser pour stocker les données métiers et les états globaux


## Objectif
> Installer, Configurer et Utiliser un environnement développement pour la production d'application web ou native dans un environnement Linux

## Quelques Principes

* En informatique il existe deux choses la **data** et la **logic**
* Tous limiter dans le temps et l'espace
* Une seule source de vérité
* Responsabilité minimale

## [Nice to Have](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA)

Paradigme
> fonctionnelle procédurale orientée-objet onpromise cloud serverless proxy loadbalancer message-queuing(AMQP) S3 Progressive-Web-Apps(PWA) server-side-rendering container pagination CI/CD REST-API IAM

Tech
> tcp socket http Cookie Token websocket webRTC regex SQL git OAuth Json Nodejs

## La programmation

Functionnel
Orienté objet
[Structure de données](https://fr.wikipedia.org/wiki/Structure_de_donn%C3%A9es)
Concaténation et Substitutions avec string, (String format, etcetc)
Design Patterns
  https://ravindraelicherla.medium.com/10-design-patterns-every-software-architect-must-know-b33237bc01c2
  https://www.youtube.com/watch?v=zlg4jCY2g4o
  https://www.youtube.com/watch?v=NjhUK68rzCs
  https://www.youtube.com/watch?v=agkWYPUcLpg
  https://www.youtube.com/watch?v=v9ejT8FO-7I
  SOLID
  MVC
  Singleton

inheritance : https://javarevisited.blogspot.com/2012/10/what-is-inheritance-in-java-and-oops-programming.html
polymorphism :  https://javarevisited.blogspot.com/2011/08/what-is-polymorphism-in-java-example.html

MultiTache
Persistence

## [Paradigme](https://www.youtube.com/watch?v=4Zc9ci9L5wY)
  * Idempotent : "The same", Une opération appliquée plusieurs fois qui donne toujours le même résultat. eg : 1*1*1*1=1 & 1*1=1 est indempotent, array.push n'est pas indempotent mais set.add l'est. Pour une API Http GET PUT et DELETE doivent toujours être indempotent
  * Ephemeral : opposite of persitent, un object est par défaut éphémaire car on peut le modifier, utiliser Object.freeze permet de le rendre Immutable
  * Predicate : 
  * Serialize : Encode un objet dans un format universel, texte ou binaire. L'objet pourra être récupérer par un autre système
  * Memoization : Permet de mettre en cache le résultat d'opération
  * Anonymous : Opération qui n'a pas de nom
  * Abstraction : Permet de cacher les détails d'une implementation complexe


## Programming Language

**Some list of them :**
* C++
* Python 3
* C
* D
* Bash
* Dart
* Perl
* Go
* Objective-C
* Pascal
* Rust
* Java
* Ruby
* C#
* Clojure
* F#
* Groovy
* Haskell
* Haxe
* Delphi
* Crystal
* 1C
* Ada
* JavaScript
* Kotlin
* Lua
* OCaml
* PHP
* Scala
* Swift
* TypeScript
* VB.NET
* BrainFuck
* Q#
* Cobol
* Erlang & Elexir
* Lisp
* Elm
* Fortan
* Assembleur
* Matlab
* Lolcode
* R
* ...

## Algorithms et Complexité

* Arbre / Arbre enraciné / Changer la racine d'un arbre
* b tree
* segment tree
* fenwick tree
* BFS
* binary tree and reverse it
* Range sum query
* Range product query
* Rabin Karp Rolling Hash
* Polynomial Hashing
* baby step giant step
* Programmation dynamique recherche opérationnelle (prog dyn bottom up & prog dyn top down)
* PD ProgDyn
* backpack algorith
* prefix tree 

### Récursivité
* Évaluation_paresseuse
* Mémoïsation

## Graphe

* Graphe_hamiltonien
* Graphe_eulérien
* Graphe non orienté / Graphe orienté


## Shell

/ * TO DO * /

## Fail2Ban

## Administration UNIX

## SystemCLT SystemD Service

## Dev et Secu
https://www.youtube.com/watch?v=PIgSrjt76Lo&feature=youtu.be
https://www.youtube.com/watch?v=26DZpCFWBdw

## AWS

https://www.youtube.com/watch?v=0YXfDuaJkCY

Aller sur aws.amazon.com/free et créer un compte "personal"
Ouvrir la console EC2, ajouter une nouvelle instance avec une offre "tier-gratuit" 
Récupérer la clé ssh privée, l'ip public et la commande ssh de connexion 
Depuis la console "AWS Cost Explorer", aller dans la console de facturation et dans les "préférences de facturation" pour ajouter le rappel de tier-gratuit
Depuis la console EC2 modifier le groupe de sécurité launch-wizard-1 ajouter des règles de pare-feu

user : cbarange
machine : i-030516c68287448cb
Public IPs: 13.59.162.131      
Private IPs: 172.31.35.140
ssh -i "aws_micro.pem" ubuntu@ec2-13-59-162-131.us-east-2.compute.amazonaws.com


Déploiements Bleus / verts : https://www.youtube.com/watch?v=NxbDHn5ryc8
Sécuriser l'utilisateur root : https://www.youtube.com/watch?v=29qidFrp0fs
Le stockage S3 : https://www.youtube.com/watch?v=4RI3pDKpx38

# Modélisation

## [UML](https://i.stack.imgur.com/tc9E4.png)

## Merise

## Personas

## Methode APTE



# DataBase

## Databse Paradigme

|Paradigme|Systeme|Description|
|:--|:--|:--|
|Relational|MySQL/MariaDB PostgreSQL SQL-Server Oracle| Provide ACID compliant|
|Document|MongoDB CouchDB FireBase|Schema-less|
|Key Value|Redis Memcached DynamoDB|RAM storage|
|Graph|neo4j|High coupling data|
|Wide-Column|HBase Cassandra||
|Timeseries|Influxdb||
|Search|Elasticsearch MeiliSearch||
|Multi-Model|Fauna||


## SQL & Relational Model

**Constraint**

|Constraint| Description|
|:--|:--|
|UNIQUE|This ensures that every record in your database has a unique value for the field that is set to unique. For example, you might want every user to have a unique email address. It is important to note that Postgres is case sensitive, so jon@CALHOUN.io is not the same as jon@calhoun.io. You will need to account for this on your own when writing data to your database.|
|NOT NULL|This ensure that every record in your database has a value for this field. When you don’t provide a value for a field the database will traditionally store null, but this prevents that from being valid.|
|PRIMARY KEY|This constraint is similar to combining both UNIQUE and NOT NULL but it can only be used once on each table, and it will automatically result in a the creation of an index for this field. The index is used to make it faster to look up records by this field.|

**File**

|File|Desciption|
|:--|:--|
|DDL||
|DML||
|DCL||

---
## PostgreSQL
> database postgresql sgbdr

**ref**
* https://www.postgresql.org/ https://www.postgresql.fr/ https://www.linkedin.com/learning/decouvrir-postgresql

PostgreSQL : Système de gestion de bases de données relationelle (SGBD) très performant sous licence BSD=gratuit avec des performances comparables à Oracle. Il propose beaucoup de fonctionnalitées et intègre plusieurs langages embarqués Perl, Python, Java, JavaScript et Rust.

**Types principaux**

|Types principaux|Desciption|
|:--|:--|
|INT|Integers between -2147483648 and 2147483647|
|SERIAL|Integers between 1 and 2147483647. Serial automatically set a value if you don’t provide one, value increase by 1|
|VARCHAR(n) VARYING(n)|String with max length as n|
|TEXT|String unlimited length|
|CHARACTER(n) CHAR(n)|String with fixed length at n|
|DATE TIMESTAMP TIME||
|BOOLEAN||
|DOMAIN||
|ENUM||
|JSON||
|GIS||

### Installation

#### Serveur
```bash
sudo apt update && sudo apt upgrade -y
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt install postgresql postgresql-contrib -y # Un nouvel utilisateur est crée pendant l'installation

service postgresql status
sudo service postgresql start
sudo -u postgres psql --version

# More
less /etc/passwd # Attention l'utilisateur postgres possède une shell, il faut le sécuriser
sudo passwd postgres # Définition du mot de passe
```

#### Client
**PLSQL**
```bash
sudo apt install -y postgresql-client
# Seul le nouvel utilisateur postgres a accés à l'interface de postgreSQL, pour ce connecter à l'interface il faut saisir une des commandes suivantes 
sudo -i -u postgres # -i Permet de charger un shell avec les variables spécifiques a l'utilisateur, $HOME, fichiers .profile et .login au users spécifié par l'option -u
psql # Lancement de l'interface postgreSQL 
# Autre commandes
su postgres
psql # Lancement de l'interface postgreSQL
# Sur une seule ligne, recommandé
sudo -u postgres psql
\q # Pour quitter l'interface PostgreSQL saisir
exit # Pour quitter la session postgres (Pour les deux premieres commandes uniquement)
less /etc/postgresql/9.4/main/postgresql.conf # Configuration du service
sudo service postgresql restart
psql --version
# L'interface PSQL nous permet d'intéragir avec les base de données via des requêtes SQL et le paramètrage de postgreSQL, un utilitaire nommé PgAdmin4 fait la même chose mais depuis l'interface graphique d'un navigateur web
\l # Permet de lister les bases de données
SELECT version(); # Affiche la version
```

**PGADIM**
```bash

```

## Best Patrices
```bash

```


## Create database
```bash

```

## Manage database
```bash

```


## Use master slaves cluster

```bash

```

## Use multi masters cluster

```bash

```


## MariaDB

## RedisDB

```bash
# Installation


```

```js
```


## MongoDB
https://www.youtube.com/watch?v=ZS_kXvOeQ5Y
https://www.youtube.com/watch?v=pWbMrx5rVBE

## PouchDB / CouchDB

## FireBase

## CassandraDB

## ScyllaDB

## OracleDB

## SQL Server

# Programming languages

## Python

* https://realpython.com/python-sleep/
* https://code.tutsplus.com/fr/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
* https://realpython.com/intro-to-python-threading/
* https://www.youtube.com/watch?v=7lmCu8wz8ro
* https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python
* 

* Numpy
* SciPy
* Boto 3
* TensorFlow
* Keras
* pytorch
* xgboost

https://www.youtube.com/watch?v=7lmCu8wz8ro

```python
from multiprocessing import Process

def e():
    1000**1000**1000**1000**1000

for i in range(1,4):
    p = Process(target=e)
    p.start()

```
--- Cours IA EPSI I4 ---
matplot
panda
numpy
sklearn & sklearn.linear_model LinearRegression
import os
import pefile
notepad = pefile.PE("notepad.exe", fast_load=True)
dbgRVA = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress
imgver = notepad.OPTIONAL_HEADER.MajorImageVersion
expRVA = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
iat = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress
sections = notepad.FILE_HEADER.NumberOfSections
dll = notepad.OPTIONAL_HEADER.DllCharacteristics
print("Notepad PE info: \n")
print ("Debug RVA: " + dbgRVA)
print ("\nImage Version: " + imgver)
print ("\nExport RVA: " + expRVA)
print ("\nImport Address Table: " + iat)
print ("\nNumber of Sections: " + sections)
print ("\nDynamic linking libraries: " + dll)







1 - Faire un programme qui attend 20 seconde et afficher pstree
2 - Faire un programme avec deux thread et afficher pstree
3 - Faire un programme avec deux process et afficher pstree
4 - Faire un programme avec deux enfant (fork) et afficher pstree

1 - Faire un programme qui écoute sur un port et affiche le résultat dans la console
Soit vie un websocket soit vers un socket. L'objectif est d'afficher des messages dans le terminale d'une autre machine



Python2 et Python3

https://www.youtube.com/watch?v=sugvnHA7ElY
https://www.youtube.com/watch?v=7lmCu8wz8ro
https://deusyss.developpez.com/tutoriels/Python/args_kwargs/

Variable https://www.youtube.com/watch?v=BJ-VvGyQxho
Fonction https://www.youtube.com/watch?v=rq8cL2XMM5M
Classe https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Héritage
Lambda
import
exceptions
interface, enum, abstract, static, final
PEP8
les meilleurs modules
 flask
 https://www.youtube.com/watch?v=FWU_tJqr1Po
 cgi
 pygame
 json
MultiTasking
  https://www.youtube.com/watch?v=JnFfp81VbOs
  https://www.youtube.com/watch?v=fKl2JW_qrso
  MultiThreading
  MultiProcessing
Python data modele
Python decorator
Programmation Système


Différence entre tâches et processus, une tâche ou Thread en anglais est 

A l'inverse un processus peut fonctionner en meme temps que les autres, ils sont cependant limité par le nombre de processeurs disponibles


Créer une Tâche :
En python la bibliothèque `threading` permet de créer des tâches parallèles nommées `Thread`. Pour cela la bibliothèque nous offre deux solution soit d'instancier un nouvel objet _Thread_ avec une expression lambda, soit de créer une class qui hérite de la classe _Thread_, cette deuxième option est préférable cela permet de regrouper les fonctionnallités au sein d'une seule classe et nous offre plus de flexibilité.



Ah non, toujours pas, mais pourquoi ? Et pourquoi cela prend-il plus de temps avec des threads qu'en utilisant une simple boucle for ?

Créer la queue et la remplir avec les nombres, puis créer les threads rend le déroulement du processus un peu plus lent, mais ce n'est pas la raison principale : nous avons la même durée d'exécution à la fin, car la tâche est intensive en temps CPU et l'implémentation CPython de Python (celle que vous pouvez télécharger par défaut sur le site officiel de Python) a un mécanisme nommé Global Interpreter Lock (GIL) qui garantit qu'un seul thread peut exécuter du code Python à un moment donné.

Quand nous téléchargeons des images, nous attendons la fin d'opérations réseau. C'est pourquoi il est possible d'effectuer des opérations en parallèle beaucoup plus vite. Il n'y a pas d'exécution de code quand on est en attente du réseau.

Nous avons vu que paralléliser des applications en utilisant la bibliothèque de threading rend les exécutions plus rapides à condition que nous donnions suffisamment de temps au processeur pour attendre et utiliser de multiples threads . Si nous avons des tâches qui consomment beaucoup de temps CPU, le nombre de threads assignés n'a pas d'importance ; nous aurons le même résultat qu'en d'exécutant un seul thread. Ceci est dû au GIL (Global Interpreter Lock). Cependant, il y a également une solution à cela : démarrer des processus multiples pour un gain de temps à l'exécution. Mais nous introduirons ce sujet dans un autre article.


On utilise Thread pour das actions bloquante et multiprocessing pour des actions lourdes


Option Daemon dans thread
La classe Queue
```py
# https://ghajba.developpez.com/tutoriels/python/programmation-parallele-python/
# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_parallelisation/thread.html
# https://riptutorial.com/fr/python/example/1778/bases-du-multithreading
# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html#gilexamplerst
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/2235545-faites-de-la-programmation-parallele-avec-threading
# https://www.youtube.com/watch?v=ecKWiaHCEKs
# https://www.youtube.com/watch?v=PJ4t2U15ACo
# https://www.youtube.com/watch?v=Lu5LrKh1Zno Multiprocessing
# https://www.youtube.com/watch?v=_1ZwkCY9wxk Pool map-reduce
# https://www.youtube.com/watch?v=nYDKH9fvlBY Decorator
# https://www.youtube.com/watch?v=sp7EhjLkFY4 Share data between process with Queue 
# https://www.youtube.com/watch?v=uWbSc84he2Q Share data between process with share memory
# https://www.youtube.com/playlist?list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6 Multiprocessing Playlist
# https://www.youtube.com/watch?v=RR4SoktDQAw Multiprocessing Part 1
# https://www.youtube.com/watch?v=itbx_hDX7z8 Multiprocessing Part2
# https://www.youtube.com/watch?v=e-HqKSBZOXo&list=PL5tcWHG-UPH3jJIyJvBrvu4LwXeZLBnEp&index=2 marckdown → pandadoc →  Beamer-LaTeX
# https://www.youtube.com/watch?v=4E7N7W1lUkU&list=PL5tcWHG-UPH3jJIyJvBrvu4LwXeZLBnEp&index=1 wav → mp3 converter

from threading import Thread
from queue import Queue


class Downloader(Thread):
    def __init__(self, queue, folder):
        Thread.__init__(self)
        self.queue = queue
        self.folder = folder

    def run(self):
        while True:
            url = self.queue.get()
            download_images(self.folder, url)
            self.queue.task_done()

thread_count = 4

queue = Queue()

for i in range(thread_count):
    downloader = Downloader(queue, 'images')
    downloader.daemon = True
    downloader.start()

for url in image_url_list:
    queue.put(url)

queue.join()
```

```py
queue = Queue() 

for i in range(thread_count):
    t = Thread(target = lambda: calculate(queue))
    t.daemon = True
    t.start()

for n in numbers:
    queue.put(n)

queue.join()

def calculate(numbers_queue):
    while True:
        number = numbers_queue.get()
        result = factors([], number)
        numbers_queue.task_done()

```

```py
print(“Total number of threads”, threading.activeCount())

print(“List of threads: “, threading.enumerate())
```

```py
import threading

import time

list1 = []

def fun1(a):

  time.sleep(1)# complex calculation takes 1 seconds

list1.append(a)

thread1 = threading.Thread(target = fun1, args = (1, ))

thread1.start()

thread2 = threading.Thread(target = fun1, args = (6, ))

thread2.start()

thread1.join()

thread2.join()

print(“List1 is: “, list1)
```

Créer un processus :

## Java



## Rust

## Go

https://www.youtube.com/watch?v=LIFZPzupwgs


## Assembleur

## Basic

## VB

## VBA

## Nodejs

See dependencies volume with : `webpack bundle analyzer` : https://www.npmjs.com/package/webpack-bundle-analyzer

Remove all node_modules folder on machine : `npx npkill`

**A Voir**
* node fastify
* ngrok

https://openclassrooms.com/fr/courses/1056721-des-applications-ultra-rapides-avec-node-js
https://www.youtube.com/watch?v=IwpBluLjynI
```bash
mkdir projectFolder
cd projectFolder
npm init
npm install -s discord.js dotenv
npm install -g nodemon
nodemon index.js
```
```js
require('dotenv').config();

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

let idOfAsignRole = "788221813264089119"
let idOfRevokeRole = "788239285873934366"

client.on('message', msg => {
  // --- DEBUG ---
  console.log("--- Liste des roles du server")
  msg.guild.roles.cache.map(e=>console.log(`${e.name}:${e.id}`))// Show Existing role
  /// --- === ---
  if(msg.content.includes('fm!certify')){
    let member=msg.mentions.members.first()
    // Si pas de user mentionne quiter
    if(!member) return msg.channel.send("Il manque le paramètre utilisateur")
    let roleToAssign = msg.guild.roles.cache.find(e=>e.id==idOfAsignRole)
    if(!roleToAssign) return msg.channel.send("Impossible de trouver le role")
    let roleToRevoke = msg.guild.roles.cache.find(e=>e.id==idOfRevokeRole)
    if(!roleToRevoke) return msg.channel.send("Impossible de trouver le role")
    // --- Try to asign role ---
    member.roles.add(roleToAssign)
    member.roles.remove(roleToRevoke)
  }
});
client.login(process.env.DISCORD_TOKEN);
````



## VueJs

## ReactJs

## AngularJs

## [Flutter](https://flutter.dev/community)
> [mobile, framework, dart, google, crossplatform]

Flutter est un SDK pour le développer des applications crossplatforme, principalement Android & IOS mais aussi Linux, Mac, Windows et le web... Open-sourcé par Google en 2017 il se veut plus bas niveau que les SDK existant, ionic, react native, cordova, appcelerator...

**Tools**
* Android Studio
* IntelliJ
* VS Code
* Dart DevTools
* Codemagic by Nevercode
* Flare by 2dimensions

### Setup
```bash
sudo snap install flutter --classic
flutter doctor
```
### Hello world !
```bash
```
### Common Usage
```bash
```

## Electron

## Fask

## Danjgo

## Python_mod

## Python_CGI

## HTTP

## HAProxy

## Apache

## Hadoop

https://www.youtube.com/watch?v=MfF750YVDxM

## Nginx

## PostgREST

## Git

Gitlab, Github, Bitbucket (altasian)
Editeur, Service
merge, rebase, checkout, pull (request), fetch, status, push, commit, reset, revert, clone

Git
- Commit
- Pusher
- Puller
- Je sais fetch !
- Je sais checkout
- Je sais créér une branche
- Je sais merger une branche
- Je sais rebaser
<<<<<<< HEAD
- Je sais faire trop de truc
=======
- C'est bientôt terminé
>>>>>>> ed9d2f2a210634a48833800b50550837a17bf6d4

## SSH

```bash
ssh-keygen Epsi2020!
cat pubkey > ~/.ssh/authorized_keys
sudo nano /etc/ssh/sshd_config
# PublicKeyAuthentication yes
# PasswordAuthentication no
sudo service ssh restart
sudo service sshd restart
cat privkey #Don't forget the \n at end of the key
sudo ssh -i ./k lwa@{IP} -p {PORT}
```

## TMUX / Shell decorator

## SSL


sudo certbot certonly --manual --cert-name ws_cert -d aws.cbarange.ovh --register-unsafely-without-email --preferred-challenges dns --dry-run

## VPN

```bash
# Server
cd
mkdir openvpn
cd openvpn
wget https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
sudo bash openvpn-install.sh
# Enable UDP on 1194
scp -i "publickey.pem" user@host:/home/user/client.ovpn ./client.ovpn
# Client for popos
#https://support.system76.com/articles/use-openvpn/
sudo apt install network-manager-openvpn-gnome
```

## Linux & Unix

Quelques packages
microk8s
wekan
docker
mosquitto
etcd
stress-ng
aws-cli
google-cloud-sdk
doctl
heroku
postgresql10
keepalived
prometheus
net-tools
git-all

---
## Virtualisation

Il existe plusieurs logiciels qui vous permettent d'éxécuter un ou plusieurs systèmes d'exploitations à l'intérieur du votre. Différent du **dual-boot** qui vous permet d'avoir plusieurs systèmes d'exploitations sur votre ordinateur, la virtualisation fonctionne avec des logiciels (*eg vmware virtualbox hyper-v*). Ces logiciels bien que performant diminuent les performances des machines virtualisées de 5 à 30% pour certains usages. 

### Clone

Cloner une machine permet de gagner du temps, vous configurez une fois votre machine idéale et la répliquez autant de fois que nécessaire. Mais attention si votre objectif est de créer des dixaines de machines vous devez plutot utiliser une système de gestion de configuration (*eg puppet ansible*). En effet apres avoir cloné une machine il reste quelques actions à faire et la maintenance de toutes ces machines est très couteuse, c'est pour cela que les outils de gestion de configuration existent. Ils peuvent gérer les évolutions de l'infrastructure peu importe le nombre de machines. Cloner une machine virtuelle est cependant intéressant à petite échelle. 

Après avoir cloné votre machine voici les actions à réaliser : 
* Pour un environment DOS exécuter simplement 
  ```batch
  C:\Windows\System32\sysprep\sysprep.exe /oobe /generalize /shutdown
  ```
* Pour une machine UNIX voici les étapes,
  
  **hostname**
  ```bash
  sudo hostnamectl set-hostname u20serverworker1
  sudo nano /etc/hosts # 127.0.0.1 u20serverworker1
  sudo sed 's/preserve_hostname: false/preserve_hostname: true/' /etc/cloud/cloud.cfg
  sudo reboot # reboot permet de réinitialiser la variable P1
  # ne pas le faire entraine un ralentissement important de la commande sudo
  ```
  **ip address**
  ```bash
  ip a
  ```
  **unique machine id**
  ```bash
  cat /etc/machine-id 
  sudo rm /etc/machine-id
  sudo systemd-machine-id-setup
```

---
## Conteneurisation

Complémentaire à la virtualisation les conteneurs permettent d'isoler des applications sous la forme de package intégrant toutes les dépendances. Les permiers systèmes de conteneurs sont apparus peu avant 2010, mais c'est en 2015 avec la norme OCI *Open Container Initiative* et le soutien des entreprises que leur utilisation a explosé. Ces packages sont téléchargables et exécutables sans que la machine hôte possède les dépendances. Les logiciels de conteneur (*eg docker podman LXC*) allouent des ressources à chaque conteneur *systèmes de fichiers, réseau, processeur, mémoire vive ...* cela permet l'isolation entre le système d'exploitation et les autres conteneurs. Ainsi un conteneurs utilise directement les ressources de l'ordinateur sans aucunes pertes de performances. Très utiliser dans le cloud les conteneurs sont souvent moins cher en maintenance qu'un VPS. Les cloud-provider (*eg GoogleCloud AmazonWebService MicrosoftAzure DigitalOcean ScaleWay*) propose des solutions pour déployer, exécuter, manipuler, monitorer, **orchestrer**... vos conteneurs (*eg google_kubernetes_engine amazon_EKS aws_lambda*)

---
## Docker
https://www.youtube.com/watch?v=8q0wcmeJ2Gk
```bash
# Dockerfile
FROM debian
MAINTAINER cbarange <cbarange@gmail.com>
# Stage 1
RUN apt-get update
# Stage 2
RUN apt-get install -y wget
# Stage 3
RUN apt-get install -y curl nginx 

# ADD and COPY
# ADD pathFromHost pathToGuest, ADD supporte aussi des url pour le chemin d'origine du fichier
# COPY pathFromHost pathToGuest
# Les paths est celui du Dockerfile
ADD script.sh /usr/bin/script.sh
RUN chmod 755 /usr/bin/script.sh
# Open port in container
EXPOSE 80

# CMD and ENTRYPOINT
# CMD : Peut etre surchagé quand on passe des arguments lors du lancement de l'image
# ex : docker run --it ubuntu bash, ici bash surcharge l'instruction CMD
# ENTRYPOINT : Ne peut pas être surchagé
# ex : 
# ENTRYPOINT ["wget"]
# CMD ["--help"]
# Pour changer le comportement de notre container
# docker run -it --rm  image_name -drc URL
# En combinant ENTRYPOINT et CMD, on peut passer des paramètres à une commande
ENTRYPOINT ["scripts.sh"]
#CMD ["script.sh"]
# Le container doit être dans un état bloquant pour ne pas se couper, on desactive le mode deamon pour avoir une commande active dans la console du container
#CMD ["nginx", "-g", "deamon off;"]

# Map un dossier entre l'host et le container
VOLUME /volume/data 

# Variables d'environment
ENV MYSQL_USER_PASSWORD superpassword!

```

```bash
docker build -t pseudo/projectname:version path/to/Dockerfile
# les RUN sont des "stages" des étapes, elles sont mises en cache et server de "snapshots" pour les futures évolutions de l'image
# Si on supprime une commande RUN an haut du fichier, l'ensemble les stages suivants seront recréer sans utiliser le cache
# On met en haut du docker file les packages standard qui n'évolurons pas, on gagne ainsi du temps lors du build 
# C'est le fonctionnement de l'AUFS
docker run --rm -it pseudo/projectname
# --rm : Remove le container quand il s'arrete
# -it : Affiche dans la console les sorties du container
# -d : Mode détaché
# -p : Map le port entre l'host et le container 
# -v : Map un dossier ente l'host et le container
# -e : Assigne des variables d'environment
# ex : docker run -d -p 80:80 -e MYSQL_USER_PASSWORD=superNewpassword! -v /path/from/host:/path/to/container pseudo/projectname
docker inspect containerID
docker ps -a
docker rm containerID
docker exec -ti containerID command
docker exec -ti containerID bash
```


## Grafana

## Monitoring

## RabbitMQ

## LogStash ou LoDash ou DashLine ou loopback.io

## Service LDAP ou SSO

## Webhooks

## InfluxDB

## RsyLog

## Animation JS

## Animation CSS

## ChartJs

## D3Js

## Canvas et SVG

## Bootstrap

## Kubernetes

## [PWA Progrssive Web App](https://medium.com/james-johnson/a-simple-progressive-web-app-tutorial-f9708e5f2605)

## [Micro Service Architecture](https://medium.com/swlh/building-javascript-microservices-with-node-js-d88bf0bb2b92)

* Objectif : Réduire la **taille** et la **complexité** de votre application. 
* Comment ? : Utiliser un **système distribué** pour passer d'une monolithe à de petites applications **indépendantes**
* Quelques avantages : modulaire, uniforme, Robuste, Maintenable, Scalable, Disponible, Testable
* Remarque : Aujourd'hui l'immense majorité des architectures micro services sont basées sur le protocole HTTP.


## Open Api / Swagger
https://www.youtube.com/watch?v=N_jQcjqEJN8&list=PLwF40GVCw5Zq4IZ5HYzd428pL-pM8Fym9&index=142&t=0s
https://www.youtube.com/watch?v=0FQ6w4CO5Nw


## HTML


`data:text/html;base64,PGgxPkhleSAhPC9oMT4=`
https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/Data_URIs

```html
<!DOCTYPE html>
<title>My Example</title>

<div style="border:1px solid black;height:100px;width:140px;overflow-y:hidden;overflow-x:scroll;">
<p style="width:250%;">
By using overflow-x, we can create scroll bars when the contents of this div are wider than the container. By setting this paragraph to 200 percent, it is 200 percent wider than the parent container - forcing an overflow. 
</p>
</div>
```


### Common usage of html
> docs : https://developer.mozilla.org/en-US/docs/Learn

#### index.html file
```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="author" content="Here your name">
    <meta name="description" content="This will appear under search engines results">

    <!-- Open Graph, used for previsualisation by socials networks and others -->
    <meta property="og:title" content="site_title">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="site_name">
    <meta property="og:url" content="https://here_url_of_website.com">
    <meta property="og:image" content="https://url_to_your_logo.png">
    <meta property="og:description" content="site_description">
    <!-- Twitter tag: https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards -->
    <meta name="twitter:title" content="site_title_twitter">
    <!-- Change mobile browser color interface -->
    <meta name="theme-color" content="#2196F3">

    <!-- Import --> 
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="my-css-file.css">
    <script src="my-js-file.js" defer></script> <!-- defer instructs the browser to load js after finished parsing html -->

    <title>title of tab</title>
  </head>
  <body>
    <p>This is my page</p>

    <p>Japanese example: <span lang="ja">ご飯が熱い。</span>.</p>

    <h1></h1> <!-- <h1> represents the main heading (use single h1 per page), <h2> represents subheadings, <h3> represents sub-subheadings, avoid to use more than 3 different heading level per page -->

  </body>
</html>
```

#### Form

#### 

## CSS

Tailwind started kit : https://github.com/creativetimofficial/tailwind-starter-kit

Boite scrollable, Dimension, Responsive ...
Texte sur une image

Exemple
```css
::before, ::after {
    box-sizing: border-box;
}
element {
    top: 77px;
}
body.dialog #divPageBody {
    position: absolute;
    top: 70px;
    right: 0;
    left: 0;
    padding: 0;
    overflow: auto;
    background: #fff;
}
div#divPageBody {
    bottom: 40px;
}
#divPageBody {
    position: absolute;
    top: 79px;
    right: 0;
    bottom: 25px;
    left: 0;
    padding: 0;
    overflow: auto;
    background: #fff;
}
body, div, span, th, td, p, a, layer, label, ul, li {
    font-kerning: normal;
    text-rendering: optimizeLegibility;
    color: #5b5d5e;
    font-size: 15px;
    line-height: 18px;
    font-family: Arial, Helvetica, sans-serif;
}
body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, code, form, fieldset, legend, input, select, option, textarea, p, blockquote, th, td {
    margin: 0;
    padding: 0;
}
* {
    box-sizing: border-box;
}
html body {
    text-align: left;
}
body {
    font-family: Arial,sans-serif;
    font-size: 14px;
    line-height: 1.42857;
    color: #3d3d3d;
}
body {
    font-family: Arial, Helvetica, Sans-serif;
    font-size: 15px;
}
html {
    font-family: sans-serif;
    -webkit-text-size-adjust: 100%;
}
```

## WebSocket

https://stackoverflow.blog/2019/12/18/websockets-for-fun-and-profit/
https://blog.stanko.io/do-you-really-need-websockets-343aed40aa9b
https://medium.com/voodoo-engineering/websockets-on-production-with-node-js-bdc82d07bb9f
https://www.ably.io/topic/websockets

## Javascript

top 10 des librairies 2021 : https://medium.com/javascript-in-plain-english/top-10-most-popular-javascript-libraries-to-use-in-2021-5da60f187992

programmation fonctionnel : https://www.youtube.com/watch?v=mW_nLYvXyKk
programmation fonctionnel : https://www.youtube.com/watch?v=YZwilQqzdYA
programmation fonctionnel : https://www.youtube.com/watch?v=-Cdt-1tWJ3M


https://www.youtube.com/watch?v=Kp3HGwlXwCk
```js
// L'objet / JSON qui stocke ke formulaire
atDataForm = {
        user_firstname: null,
        user_lastname: null,
        user_email: null,
        user_subject: null,
        user_message: null
      }

// Fonction vérifie si l'object possède des clés dont la valeur est null 
function checkIfObjectContainsNullValue(object){
    let isObjectNullLess = true
    Object.entries(object).map(([k,v]) => !v ? isObjectNullLess = false : undefined )
    return isObjectNullLess
}

// Fonction métier, vérifie sur le formulaire est bien complété
function submitEmailForm(){
  if(checkIfObjectContainsNullValue(atDataForm)){
      emailjs.send(atDataForm)
      alert("Votre email a bien été envoyé")
  } else {
     alert("Veuillez correctement remplire le formulaire")
  }
} 

```

## CTF 

https://ungeek.fr/le-petit-guide-du-chasseur-de-drapeaux/
https://github.com/zardus/ctf-tools
https://github.com/apsdehal/awesome-ctf#solve

icpc programming contest
icpc nwerk
icpc swerc


## Bash commands

```bash
cut
ed
ex
head
join
nl
sed
awk
mount
jq
base64
sha1 md5
strings
tee
uniq
wc
tr
split
tail
netstat
tcpdump
echo
chmod
chown
passwd
alias
sl # Look for
xeyes
```

## REST API
Sources :
* https://atinux.developpez.com/tutoriels/javascript/mongodb-nodejs-mongoose/#LVII
* https://hackernoon.com/goodbye-redux-26e6a27b3a0b
* https://www.toptal.com/nodejs/secure-rest-api-in-nodejs
* https://blog.logrocket.com/setting-up-a-restful-api-with-node-js-and-postgresql-d96d6fc892d8/
* https://www.enterprisedb.com/postgres-tutorials/how-quickly-build-api-using-nodejs-postgresql

## Pentest
> [pentest, whitehat]

### Network

**Yersinia, framework for performing layer 2 attacks like a cisco hardware**
```bash
sudo apt install -y yersinia
yersinia -G
```

## Miscellaneous

### SMS API

* MessageBird
* plivo

### URL
> [url, seo]

Pour les requêtes la taille maximale de l'url est de 2 083 mais pour la SEO entre comptez entre 50 et 60 au maximum et pas plus de 3 à 5 mots, le reste est destiné à la machine.
[doc google](https://chromium.googlesource.com/chromium/src/+/master/docs/security/url_display_guidelines/url_display_guidelines.md)

### Base64
> [base64]

Base64 est généralement 33% plus long que sa valeur text/plain

### Data URLs
> [url, browser, data, base64]

* Answer : https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs

**Example**
* data:image/png;base64,{BASE64_PNG}
* data:image/svg+xml;base64,PB94e...
* data:,Hello%2C%20World!
* data:text/html,%3Ch1%3EHello%2C%20World!%3C%2Fh1%3E
* data:text/html,<script>alert('Hey !');</script>
* [Example png](data:image/png;base64,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)

Peut être utiliser dans l'attribut *href* d'un *svg*, dans l'attribut *src* d'une balise _img_, dans un url de navigateur mais attention la taille ne doit pas dépasser 32768 caractère pour l'affichage mais elle peut aller à plus de 100 000 sur certain navigateur [Wikipedia](https://en.wikipedia.org/wiki/Data_URI_scheme)

### Indentation
> [indentation, space, tab, 4, 2]

https://stackoverflow.com/questions/7070927/is-it-safe-to-indent-with-2-spaces
* Answer : `Use 2 spaces for indentation`

### [Complexité algorithmique](https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes), [Big O notation](https://www.youtube.com/watch?v=g2o22C3CRfU)
> [O(n), o notation, complexité, algorithms]

On mesure deux complexités, celle de *temps* et celle d'*espace*, elles dépendent de la taille (N) de l'entré.
* Temps : Quantité d'opérations, souvent CPU, nécessaire en fonction N
* Espace : Quantité de mémoire, souvent RAM, nécessaire en fonction de N

|N|1000|
|:--|:--|
|O(N)|1000|
|O(log N)|3|
|O(N²)|1 000 000|
|O(2^N)|1e+301|
|O(N!)|4e+2567|

> Resource : [*The Art of Computer Programming*](https://fr.wikipedia.org/wiki/The_Art_of_Computer_Programming)

### Securité
Source:
* https://confituregeek.wordpress.com/2016/01/27/securiser-une-api-rest-via-une-clef-dapi/
* https://www.redhat.com/fr/topics/security/api-security
* https://blog.octo.com/securiser-une-api-rest-tout-ce-quil-faut-savoir/
* https://www.codeheroes.fr/2018/03/23/securiser-une-api-rest/#:~:text=On%20a%20vu%20tout%20au,pour%20l'authentification%20des%20utilisateurs.

Mettre en place une api Rest est une chose, la sécuriser en est un autre.

**Login**

Pour chaque requete le user envoie en paramètre son username et mot de passe. Cette méthode est très vulnérable attaque man in middle et pour chaque requete c'est le même couple username/mot de passe qui est utilisé.  

**Token**

Apres l'authentification avec son username et mot de passe le client reçoit un token qui sera réutilisé pour toute les autres requetes, ce token à une durée de vie limité. C'est le fonctionnemen de "JWT REST". Mais cette solution est toujours vulnerable au vol du token.

**La clef d’api**

On ajoute à chaque requête une signature, un secret est utilisé pour générer un hash : Signature = base64(HMAC-SHA1(requête, motdepasse)). On peut ajouter un timestamp pour limiter la durée de vie de cette signature, Put http://monsitedevoiture/voitures/123&signature=hizuefguzefu123&timestamp=1234567890  {user=toto ; prix=15000}

### P vs NP Problem, [P=NP](https://www.youtube.com/watch?v=AgtOCNCejQ8)
> [P vs NP Problem ,p=np, 7 millennium problems, ] 

> P=NP fait parti des 7 problèmes mathématiques du millénaire. Cette équation décrit la complexité des algorithms.




## Références

### Algo

* `LIVRE` Programmation Efficace Les 128 Algorithmes Qu'il faut avoir compris
* `SITE` france ioi
* `SITE` code forces
* `SITE` CP-Algorithms
* `SITE` coding-game
* `SITE` Isogard
* `LIVRE` Introduction to algorithms (Cormen)
* `LIVRE` Algorithm Design
* `LIVRE` Le mythe de la singularité, faut il craindre l'intelligence artificielle de Jean-Gabriel Ganascia

### Conception

* `LIVRE` Le Mom Test: Comment parler avec les clients et apprendre si votre idée d'entreprise est bonne, quand tout le monde vous ment 



#### Entretient

* Combien d'espace est utilisé pour l'indentation ?
* Changer la couleur des lignes impaire d'un tableau
* Montrer moi comment vous afficher une informations standard, (eg : print, printf, console.log, echo, System.out.print...)
* Mob programming | Pair programming ?


```
Une stack technique moderne. 
La volonté de répondre à un vrai besoin, d'apporter de la valeur & de résoudre des problèmes 😃. 
Etre entouré de personnes compétentes aussi bien dans la technique que dans la conception, l'analyse et l'humain👏.

Et surtout surtout apprendre un max 😎 !
```

## [SEO](https://www.youtube.com/watch?v=-B58GgsehKQ)


