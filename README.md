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
