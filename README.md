How to start this project with current python --version from host 


step 1: this command start a pipenv shell in current directory with the python interpreter from the system
python3 -m pipenv --python $(which python3)

step 2: start the shell and go inside it
pipenv shell

step3:
install django using pip

$ python -m pip install Django



How to setup posgresql local environment to work first need to start pipenv shell python versio 3.11 then install pgadmin4 

then install psql and create new user with password and remember those data

now creta .pg_service.conf file in hoem directory with the same name and password you created psql user

"[my_service]
host=localhost
user=user_domain_com
dbname=name
port=5432
password=123456"

now go to psql create necessary table you need then they will be visible in pgadmin once you create server with the values your provided in th config file 

Projects git:(main) ✗ cd pgadminenv 
➜  pgadminenv git:(main) ✗ pipenv install --python 3.11      # or '3.10' if available

Warning: Python 3.11 was not found on your system...
Would you like us to install CPython 3.11.11 with Pyenv? [Y/n]: y
Installing CPython 3.11.11 with /home/wishwa/.pyenv/bin/pyenv (this may take a few minutes)...
✔ Success!
⠹ Installing python...
Warning: The Python you just installed is not available on your PATH, apparently.
➜  pgadminenv git:(main) ✗ pipenv shell

Creating a virtualenv for this project...
Pipfile: /home/wishwa/Projects/pgadminenv/Pipfile
Using default python from /usr/bin/python3 (3.12.3) to create virtualenv...
⠧ Creating virtual environment...created virtual environment CPython3.12.3.final.0-64 in 272ms
  creator CPython3Posix(dest=/home/wishwa/.local/share/virtualenvs/pgadminenv-6gM0vK_e, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/home/wishwa/.local/share/virtualenv)
    added seed packages: pip==24.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/wishwa/.local/share/virtualenvs/pgadminenv-6gM0vK_e
Creating a Pipfile for this project...
Launching subshell in virtual environment...
 . /home/wishwa/.local/share/virtualenvs/pgadminenv-6gM0vK_e/bin/activate
➜  pgadminenv  . /home/wishwa/.local/share/virtualenvs/pgadminenv-6gM0vK_e/bin/activate
(pgadminenv) ➜  pgadminenv git:(main) ✗ pip install pgadmin4
Collecting pgadmin4
  Using cached pgadmin4-9.6-py3-none-any.whl.metadata (2.9 kB)
Collecting Authlib==1.6.* (from pgadmin4)


now create a file name .my_bgpass
and this data in it 

"localhost:5432:NAME:USER:PASSWORD"

now make sure settings.py files has this 


DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "OPTIONS": {
      "service": "my_service",
      "passfile": ".pgpass",
    },
  }
}


How to start postgres db for development 

step 1: start pgadmin4 web interface 

create a directory name pgadmin4

write this process carefully start pgadming web interface 

$ sudo mkdir /var/lib/pgadmin
$ sudo mkdir /var/log/pgadmin
$ sudo chown $USER /var/lib/pgadmin
$ sudo chown $USER /var/log/pgadmin
$ python3 -m venv pgadmin4
$ source pgadmin4/bin/activate
(pgadmin4) $ pip install pgadmin4
...
(pgadmin4) $ pgadmin4
NOTE: Configuring authentication for SERVER mode.

Enter the email address and password to use for the initial pgAdmin user account:

Email address: user@domain.com
Password: 
Retype password:
Starting pgAdmin 4. Please navigate to http://127.0.0.1:5050 in your browser.
 * Serving Flask app "pgadmin" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off


 step2: run psql server

  
  sudo systemctl start postgresql


you can use this command to see the state of postgres server

  sudo systemctl status postgresql

now user the same user name and pass word you use in postgressql database in pgadmin4 interface which is most 
probably availbla in 

http://127.0.0.1:5050/browser/


this command let you connect with postgressql service from terminal

sudo psql -h localhost -U "user_domain_com" -d name -W

password is 123456

it think for this to work it expercts information from .pg_Service.conf file in home directory





This is what the fuck is going on here for some reason user@domain.com in pgadmin4 is equal to user_domain_com  from config file 

so this is the database configuration code  we have setup in django setting files 


DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "OPTIONS": {
      "service": "my_service",
      "passfile": ".pgpass",
    },
  }
}

what this means is my_service data in pg_service.conf file that should be in home directory has all the data to start a connection for my_django_app or psql command
this is what is has 

[my_service]
host=localhost
user=user_domain_com
dbname=name
port=5432
password=123456

and .pgpass which also should place in the home directory provides the password and other paramters in .pg_service.conf file 

this is what containes 

localhost:5432:name:user_domain_com:123456

this should be in the correct order that file needs permission to read using this command

chmod 0600 ~/.pgpass and it should stricly be 0600 permission

now you can connect to the pgadmin4 interface with user@domain.com and the same password 123456 it is weird but it works.

but in order to run migrations you have to make sure that user@domain.com has the right permission to create tables in the database for that
you have switch in postgresql user who is runnning the postgress server service and then define the password for postgresuser 

now move out to normal user and login to postrgress terminal with that password but still with permission as postgressql SUPERUSER
and give persmission to user_domain_name to create tables 

now you can run python manage.py migrate and it will run the migrations and you can see those tables in pgadmin4 interface taa daa daa.

this is termianl logs of doing this 

  ~ sudo vim .pgpass
[sudo] password for wishwa:             
➜  ~ chmod 0600 ~/.pgpass
➜  ~ sudo chmod 0600 ~/.pgpass
➜  ~ sudo -i -u postgres
[sudo] password for wishwa:             
postgres@wishwa-Modern-14-C11M:~$ psql
psql (16.9 (Ubuntu 16.9-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# ALTER USER postgres WITH PASSWORD '123456';
ALTER ROLE
postgres=# \q
postgres@wishwa-Modern-14-C11M:~$ \q
Command 'q' not found, but can be installed with:
apt install python3-q-text-as-data
Please ask your administrator.
postgres@wishwa-Modern-14-C11M:~$ exit
logout
➜  ~ psql -U postgres -h localhost -d name
Password for user postgres: 
psql (16.9 (Ubuntu 16.9-0ubuntu0.24.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

name=# SELECT rolname FROM pg_roles;
           rolname           
-----------------------------
 pg_database_owner
 pg_read_all_data
 pg_write_all_data
 pg_monitor
 pg_read_all_settings
 pg_read_all_stats
 pg_stat_scan_tables
 pg_read_server_files
 pg_write_server_files
 pg_execute_server_program
 pg_signal_backend
 pg_checkpoint
 pg_use_reserved_connections
 pg_create_subscription
 user_domain_com
 postgres
(16 rows)

name=# GRANT CREATE ON SCHEMA public TO "user_domain_com";
GRANT
name=# 

