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
