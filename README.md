###### auteur : Clément BARANGER	date : 16-07-2020

## Objectif

> Installer, Configurer et Utiliser un environnement développement pour la production d'application web dans un environnement Linux, (Ubuntu 18LTS).


# Les Traitement

# Les Données

## Les base de données
Les performances des différentes solutions et usages
/ * TO DO * /
A quoi ça sert ?

---

# Outils et Langages

## La programmation

Functionnel
Orienté objet
Concaténation et Substitutions avec string, (String format, etcetc)
Design Patterns
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


---


## PostgreSQL

PostgreSQL est un système de gestion de bases de données (SGBD) très performant sous licence BSD dont les performances sont comparables à Oracle 9. 

Il propose de très nombreuses fonctionnalités, tout en respectant les standards SQL : SQL 92, 99 et en partie la norme SQL2003. En outre, il intègre plusieurs langages embarqués (Perl, Python, Java, JavaScript et Rust) depuis de nombreuses années.

https://www.postgresql.org/
https://www.postgresql.fr/

### Installation & Setup

```bash
sudo apt update && sudo apt upgrade -y # L'option -y valide la demande de validation de l'installation, ce n'est pas une option obligatoire
sudo apt install postgresql postgresql-contrib -y # Un nouvel utilisateur est crée pendant l'installation
sudo apt install finger # Finger est un outil pour afficher les détails d'un utilisateur
finger postgres # Affichage des attributs de l'utilisateur postgres
less /etc/passwd # Attention l'utilisateur postgres possède une shell, il faut le sécuriser
sudo passwd postgres # Définition du mot de passe, patate
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



drop database if exists DBNAME;
create database DBNAME;
\c DBNAME;
drop schema if exists SCHEMANAME;
create schema SCHEMANAME;

CREATE USER ps_admin WITH encrypted PASSWORD 'EPSI_2020';
GRANT ALL privileges ON database mspr_prestashop to ps_admin;
GRANT ALL privileges on SCHEMA mspr TO ps_admin;
GRANT ALL privileges ON ALL TABLES IN SCHEMA mspr TO ps_admin;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA mspr TO ps_admin;

drop table if exists mspr.user;
CREATE TABLE mspr.user(
   -- user_id SERIAL PRIMARY KEY,
   user_id integer PRIMARY KEY,
   email VARCHAR (355) NOT NULL,
   passwd VARCHAR (355) NOT NULL
);

-- alter table mspr.user  ALTER COLUMN passwd TYPE varchar(355);
\d mspr.user
delete from mspr.user;
insert into mspr.user(user_id, email,passwd) values (0,'email@email.fr','$2a$10$gt/8moSeQUxRsy13qbeE4edMnfbhKxIkSDB5NzYkY4BFz12KLn/MS');
select * from mspr.user;

create extension if not exists "uuid-ossp";

drop table if exists mspr.coupon;
CREATE TABLE  mspr.coupon(
	coupon_id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   	product_id integer NOT NULL,
   	value integer NOT NULL,
   	start_date date not null,
   	end_date date not null,
   	message varchar(355) not null,
   	description varchar(355) not null,
   	CONSTRAINT PK_COUPON PRIMARY KEY(coupon_id)
);
delete from mspr.coupon;
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(1,25,'01/01/2020','01/01/2021','REDUC','Utiliser ce coupon sur l article carnet de note en liege');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(2,5,'01/01/2020','01/01/2021','PAPER','Utiliser ce coupon sur l article carnet de note en carton');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(3,3,'01/01/2020','01/01/2021','PAPER','Utiliser ce coupon sur l article carnet de note en papier');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(4,2,'01/01/2020','01/01/2021','TOPCADOC','Utiliser ce coupon sur l article carnet de note en tissu');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(5,0.50,'01/01/2020','01/01/2021','FOXY','Utiliser ce coupon sur l article fox');
select * from mspr.coupon;

-- --------------------------
-- --- CREATE TABLE ADMIN ---
-- ---                    ---
drop table if exists mspr.admin;
CREATE TABLE mspr.admin(
   admin_id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   email VARCHAR (355) NOT NULL,
   passwd VARCHAR (355) NOT NULL,
   CONSTRAINT PK_ADMIN PRIMARY KEY(admin_id)
);

\d mspr.admin
insert into mspr.admin(email,passwd) values ('email@email.fr','password');
insert into mspr.admin(email,passwd) values ('admin@email.fr','$2y$10$ehWoifyiW1tKUIgMZA9fmOLkOHpGw9oTniXkVlrTs889IY0LR58Uq');
insert into mspr.admin(email,passwd) values ('test@test.fr','$2a$10$gt/8moSeQUxRsy13qbeE4edMnfbhKxIkSDB5NzYkY4BFz12KLn/MS');

-- -------------------------------
-- --- CREATE TABLE HISTORIQUE ---
-- ---                         ---
drop table if exists mspr.historique;
CREATE TABLE mspr.historique(
   id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   _date date null default CURRENT_DATE,
   coupon UUID not null,
   user integer null,
   CONSTRAINT PK_HISTORIQUE PRIMARY KEY(id)
);
\d mspr.historique
insert into mspr.historique(email,passwd) values ('email@email.fr','password');

```


### Premiers Pas



### Usages Avancés

Backup, plan de backup dump import, import mariadb, oracle etc etc...

Comment securiser l'utilisateur postgres apres l'installation de postgreSQL , acces que local a l'utilisateur ?

### Bonnes Pratiques

---

## MariaDB

### Installation & Setup

### Premiers Pas

### Usages Avancés

### Bonnes Pratiques

--- 

## RedisDB

## MongoDB
https://www.youtube.com/watch?v=ZS_kXvOeQ5Y
https://www.youtube.com/watch?v=pWbMrx5rVBE

## PouchDB / CouchDB

## FireBase

## CassandraDB

## ScyllaDB

## OracleDB

## SQL Server

## HAProxy

## Apache

## Hadoop

https://www.youtube.com/watch?v=MfF750YVDxM

## Nginx

## PostgREST

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

## NodeJs

https://openclassrooms.com/fr/courses/1056721-des-applications-ultra-rapides-avec-node-js
https://www.youtube.com/watch?v=IwpBluLjynI



## VueJs

## ReactJs

## AngularJs

## Electron

## Fask

## Danjgo

## Python_mod

## Python_CGI

## Git

Gitlab, Github, Bitbucket (altasian)
Editeur, Service
merge, rebase, checkout, pull (request), fetch, status, push, commit, reset, revert, clone

## SSH

## TMUX / Shell decorator

## SSL

## VPN

## Docker

## Virtualisation

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

## Open Api / Swagger
https://www.youtube.com/watch?v=N_jQcjqEJN8&list=PLwF40GVCw5Zq4IZ5HYzd428pL-pM8Fym9&index=142&t=0s
https://www.youtube.com/watch?v=0FQ6w4CO5Nw


## HTML
```html
<!DOCTYPE html>
<title>My Example</title>

<div style="border:1px solid black;height:100px;width:140px;overflow-y:hidden;overflow-x:scroll;">
<p style="width:250%;">
By using overflow-x, we can create scroll bars when the contents of this div are wider than the container. By setting this paragraph to 200 percent, it is 200 percent wider than the parent container - forcing an overflow. 
</p>
</div>
```

## CSS

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


## Javascript

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

