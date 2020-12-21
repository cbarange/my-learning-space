# REST API
> cbarange | 15th October 2020
---

## Setup

* Install database
* Create users and role
* Privilege
* Database and template
* Schema public and other
* backup solution
* remote connections
* table, trigger, function
* deplacer le repertoir des données
* pagination https://www.citusdata.com/blog/2016/03/30/five-ways-to-paginate/

```bash
# --- Install postgresql service ---
sudo apt update && sudo apt upgrade -y
# Official repo
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
# Linux distribution repo
# sudo apt-get install postgresql postgresql-contrib
# --- === ---

# --- Installation's check ---
service postgresql status
sudo service postgresql start
sudo -u postgres psql --version
#sudo -u postgres psql
# --- === ---

# --- Connection ---
export NAME_SUPERUSER_POSTGRES="demo_root"
export PASSWORD_SUPERUSER_POSTGRES="Epsi_2020!"
export DATABASE_NAME_POSTGRES="demo_db"
#export QUERY_SQL="SELECT version();"
export QUERY_SQL_FILE="setup_schema_postgres.sql"
export HOST_POSTGRES="127.0.0.1"
export PORT_POSTGRES="5432"
export OUTPUT_FILE="setup_output_postgres_`date +"%Y-%m-%d"`.log"

echo "" > $OUTPUT_FILE

sudo -u postgres psql -c "DROP DATABASE IF EXISTS $DATABASE_NAME_POSTGRES;"
sudo -u postgres psql -c "DROP ROLE IF EXISTS $NAME_SUPERUSER_POSTGRES;"
sudo -u postgres psql -c "CREATE USER $NAME_SUPERUSER_POSTGRES WITH PASSWORD '$PASSWORD_SUPERUSER_POSTGRES' SUPERUSER;"
sudo -u postgres psql -c "CREATE DATABASE $DATABASE_NAME_POSTGRES WITH OWNER=$NAME_SUPERUSER_POSTGRES ENCODING 'UTF8';"

#psql -f thefile.sql targetdatabase
sudo -u postgres PGPASSWORD="$PASSWORD_SUPERUSER_POSTGRES" \
psql -t -A \
-h "$HOST_POSTGRES" \
-p "$PORT_POSTGRES" \
-U "$NAME_SUPERUSER_POSTGRES" \
-d "$DATABASE_NAME_POSTGRES" \
-f "$QUERY_SQL_FILE"
#-o "$OUTPUT_FILE"
#-c "$QUERY_SQL"
# --- === ---

# --- Check ---
sudo -u postgres PGPASSWORD="$PASSWORD_SUPERUSER_POSTGRES" psql -h "$HOST_POSTGRES" -p "$PORT_POSTGRES" -U "$NAME_SUPERUSER_POSTGRES" -d "$DATABASE_NAME_POSTGRES"
#\conninfo
#\dn
#\dt demo_schema.
# --- === ---
```

```sql
-- Remove old permissions for public schema
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE demo_db FROM PUBLIC;
-- Create new schema
-- \c demo_db
CREATE SCHEMA demo_schema;
--\dn
-- Create new table
DROP TABLE IF EXISTS demo_schema.user CASCADE;
CREATE TABLE demo_schema.user(
   username VARCHAR (355) NOT NULL
);

DROP TABLE IF EXISTS demo_schema.message CASCADE;
CREATE TABLE demo_schema.message(
   text VARCHAR (355) NOT NULL
);
-- Create trigger

-- Insert values
DELETE FROM demo_schema.user; -- CASCADE
INSERT INTO demo_schema.user(username) 
VALUES ('JEAN'), ('MICHEL'), ('JACK');
-- Create roles, read, write, update, delete
-- SELECT ROLE
DROP ROLE IF EXISTS select_role;
CREATE ROLE select_role; 
GRANT CONNECT ON DATABASE demo_db TO select_role; -- enable connections on database
GRANT USAGE ON SCHEMA demo_schema TO select_role; -- enable operations on schema
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT SELECT ON TABLES TO select_role; -- automatically assign select when you create new table

-- INSERT ROLE
DROP ROLE IF EXISTS insert_role;
CREATE ROLE insert_role;
GRANT CONNECT ON DATABASE demo_db TO insert_role;
GRANT USAGE ON SCHEMA demo_schema TO insert_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT SELECT, INSERT ON TABLES TO insert_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT USAGE ON SEQUENCES TO insert_role;

-- UPDATE ROLE
DROP ROLE IF EXISTS update_role;
CREATE ROLE update_role;
GRANT CONNECT ON DATABASE demo_db TO update_role;
GRANT USAGE ON SCHEMA demo_schema TO update_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT SELECT, UPDATE ON TABLES TO update_role;
--ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT USAGE ON SEQUENCES TO update_role;

-- DELETE ROLE
DROP ROLE IF EXISTS delete_role;
CREATE ROLE delete_role;
GRANT CONNECT ON DATABASE demo_db TO delete_role;
GRANT USAGE ON SCHEMA demo_schema TO delete_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT SELECT, DELETE ON TABLES TO delete_role;
--ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT USAGE ON SEQUENCES TO delete_role;

-- ADMIN ROLE
DROP ROLE IF EXISTS admin_role;
CREATE ROLE admin_role;
--GRANT ALL ON  DATABASE demo_db TO admin_role;
GRANT CONNECT ON DATABASE demo_db TO admin_role;
GRANT USAGE ON SCHEMA demo_schema TO admin_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT SELECT, INSERT, UPDATE, DELETE, TRIGGER, TRUNCATE ON TABLES TO admin_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT EXECUTE ON FUNCTIONS TO admin_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA demo_schema GRANT USAGE ON SEQUENCES TO admin_role;

-- Create user from role
DROP ROLE IF EXISTS dba_user; 
CREATE ROLE dba_user WITH IN ROLE admin_role LOGIN CONNECTION LIMIT 1 ENCRYPTED PASSWORD 'Epsi_2020!';

-- Add new permissions for new schema
--SET ROLE dba_user;
--SELECT rolname FROM pg_roles;
--\du
--\dg

```

## Plan de backup
```bash
# Source : https://www.digitalocean.com/community/tutorials/how-to-backup-postgresql-databases-on-an-ubuntu-vps
# Backup database
sudo -u postgres pg_dump postgres > postgres_db.bak
# Usage : pg_dump -U user_name -h remote_host -p remote_port name_of_database > name_of_backup_file
# Restore database
sudo -u postgres empty_database_name < postgres_db.bak

# The empty database should be created using "template0" as the base.
#createdb -T template0 restored_database
#psql restored_database < database.bak

# Dump all databases
pg_dumpall > backup_file
psql -f backup_file postgres

# Cron tab + export du backup
```
## Python Flask


## NodeJs 



```sql
-- source : https://aws.amazon.com/fr/blogs/database/managing-postgresql-users-and-roles/#:~:text=Users%2C%20groups%2C%20and%20roles%20are,to%20log%20in%20by%20default.&text=The%20roles%20are%20used%20only,grant%20them%20all%20the%20permissions.
-- Users and Roles Bests Practices
CREATE ROLE readonly_user;
GRANT CONNECT ON DATABASE mydatabase TO readonly_user; -- enable connections on database
GRANT USAGE ON SCHEMA myschema TO readonly; -- enable operations on schema
GRANT SELECT ON TABLE mytable1, mytable2 TO readonly; -- enable select for tables
GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO readonly; -- same for all tables
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO readonly; -- automatically assign select when you create new table
-- Same for READ and WRITE user
CREATE ROLE readwrite;
GRANT CONNECT ON DATABASE mydatabase TO readwrite;
GRANT USAGE ON SCHEMA myschema TO readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE mytable1, mytable2 TO readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA myschema TO readwrite;
GRANT USAGE ON SEQUENCE myseq1, myseq2 TO readwrite; -- must enable SEQUENCES permission for insert
GRANT USAGE ON ALL SEQUENCES IN SCHEMA myschema TO readwrite;
-- automatically do the same things when new tables will add
-- ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT USAGE ON SEQUENCES TO readwrite;

-- Create user
CREATE USER myuser1 WITH PASSWORD 'secret_passwd';
GRANT readonly TO myuser1;
REVOKE readwrite FROM myuser1;

-- audit : https://github.com/pgaudit/pgaudit
-- show user roles and permissions
SELECT r.rolname, 
      ARRAY(SELECT b.rolname
            FROM pg_catalog.pg_auth_members m
            JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)
            WHERE m.member = r.oid) as memberof
FROM pg_catalog.pg_roles r
WHERE r.rolname NOT IN ('pg_signal_backend','rds_iam',
                        'rds_replication','rds_superuser',
                        'rdsadmin','rdsrepladmin')
ORDER BY 1;
-- liste role
SELECT rolname FROM pg_roles;




-- SUMMARY
-- Revoke privileges from 'public' role
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE mydatabase FROM PUBLIC;
-- Read-only role
CREATE ROLE readonly;
GRANT CONNECT ON DATABASE mydatabase TO readonly;
GRANT USAGE ON SCHEMA myschema TO readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO readonly;
-- Read/write role
CREATE ROLE readwrite;
GRANT CONNECT ON DATABASE mydatabase TO readwrite;
GRANT USAGE, CREATE ON SCHEMA myschema TO readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA myschema TO readwrite;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA myschema TO readwrite;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT USAGE ON SEQUENCES TO readwrite;
-- Users creation
CREATE USER reporting_user1 WITH PASSWORD 'some_secret_passwd';
CREATE USER reporting_user2 WITH PASSWORD 'some_secret_passwd';
CREATE USER app_user1 WITH PASSWORD 'some_secret_passwd';
CREATE USER app_user2 WITH PASSWORD 'some_secret_passwd';
-- Grant privileges to users
GRANT readonly TO reporting_user1;
GRANT readonly TO reporting_user2;
GRANT readwrite TO app_user1;
GRANT readwrite TO app_user2;
```

```sql
SELECT version();
-- --- Create database and schema ---
drop database if exists $DATABASE_NAME;
create database $DATABASE_NAME;
create schema $SCHEMA_NAME;
-- --- === ---

-- --- Create user ---
DROP ROLE IF EXISTS $ROLE_NAME;

CREATE ROLE $ROLE_NAME WITH LOGIN;
-- ALTER ROLE $ROLE_NAME WITH NOLOGIN; -- 
-- CREATE ROLE myuser WITH LOGIN PASSWORD 'secret_passwd';

-- show search_path; -- 
-- REVOKE CREATE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON demo TO test_user;
ALTER TABLE hello OWNER TO demo_role;
-- CREATE USER rolen_ame; -- create role with login privileges as default
-- liste role
\du 

CREATE ROLE login_role WITH login;
CREATE ROLE access_role;
\du
CREATE DATABASE demo_application WITH OWNER access_role;
\c demo_application
REVOKE ALL ON SCHEMA public FROM public;
GRANT ALL ON SCHEMA public TO access_role;

RESET ROLE;
GRANT access_role TO login_role;
SET ROLE login_role;
CREATE TABLE test_table(
	name varchar(25)
);

CREATE USER $USER_NAME WITH encrypted PASSWORD $USER_PASSWORD;
GRANT ALL PRIVILEGES ON DATABASE $DATABASE_NAME TO $USER_NAME;
GRANT ALL PRIVILEGES ON SCHEMA $SCHEMA_NAME TO $USER_NAME;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA mspr TO $USER_NAME;
-- --- === ---

-- --- Create table ---
drop table if exists $SCHEMA_NAME.$TABLE_NAME;
CREATE TABLE $SCHEMA_NAME.$TABLE_NAME(
   username VARCHAR (355) NOT NULL
);
-- --- === --- 
```



