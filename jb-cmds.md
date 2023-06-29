# Basic Django Setup CMDs
===================================================================================================
### Create the venv
===================================================================================================
python -m venv venv <!-- To creat venv for Windows-->
venv\Scripts\activate.bat <!-- To activate the venv for Windows and run pip freeze to confirm empty venv-->
venv\Scripts\deactivate <!-- To deactivate for Windows -->

sudo apt install python3-venv <!-- To install venv for Ubuntu -->
python3 -m venv venv <!-- To create for Ubuntu/Unix/MacOS    -->
source venv/bin/activate <!-- To activate venv for Ubuntu/Unix MacOS -->
deactivate <!-- To deactivate venv for Ubuntu/Unix MacOS -->
===================================================================================================
### Some Pip Installations on the venv
===================================================================================================
pip install --upgrade pip
pip install django 
pip install python-dotenv <!-- for .env -->
pip install djongo <!-- for `mongo` which will also require/install `pymongo` and `dnspython` while `psycopg2-binary
mysqlclient` and `psycopg2-binary
mysqlclient` for `postgres` n `mysql` resp-->
pip install xhtml2pdf <!-- for  xhtml to pdf conversions and downloads -->
pip install django-crispy-forms crispy-bootstrap4 bootstrap4  <!-- # You will need to pip install crispy-bootstrap4 and add crispy_bootstrap4 to your list of INSTALLED_APPS. Also add: CRISPY_TEMPLATE_PACK = 'bootstrap4' to settings.py -->
pip install pandas matplotlib <!-- for some visualizations -->
pip install channels channels_redis <!-- for live data streaming  --> 
pip install Pillow <!-- for files --> 
pip install djangorestframework django-cors-headers <!-- for DRF pointing to React, Vue or Angular -->
pip install gunicorn <!-- for nginx (prod) -->
<!-- 
pip install django python-dotenv djongo django-crispy-forms crispy-bootstrap4 bootstrap4 coverage flake8 pep8 pandas xhtml2pdf 
pip install djongo psycopg2-binary mysqlclient
pip install matplotlib Pillow  channels channels_redis  djangorestframework django-cors-headers 
 -->
===================================================================================================
### Some Basic Django Testings with `coverage`, flake8 and pep8 
===================================================================================================
pip install coverage flake8 pep8
coverage --version
coverage report
coverage html
coverage run --omit='*/venv/*' manage.py test
py manage.py test
<!-- flake8 and pep8 -->
<!-- 
#setup.cfg
[flake8]
exclude = .git,*migrations*,*venv*
max-line-length = 119 
#Run `flake8` 
-->
===================================================================================================
Pip freeze for requirements.txt file and Setup for prod
===================================================================================================
pip freeze > requirements.txt <!-- To freeze requirements.txt-->
pip install -r requirements.txt <!-- To install requirements.txt-->
===================================================================================================
### Setup Django project and app(s) 
===================================================================================================
django-admin startproject trader_dashboard . <!-- To startproject -->
python manage.py startapp user_dashboard <!-- To startapp -->

python manage.py makemigrations <!-- To make migrations for db model(s) -->
python manage.py migrate <!-- To migrate migrations data to db -->

python manage.py runserver <!-- To run the server at django default port 8000 -->
python manage.py createsuperuser <!-- To create a super user for the admin dashboard -->
===================================================================================================
Username: admin
Email address: syntaxland@gmail.com
Password: boz1234567
===================================================================================================
### QuerySets
===================================================================================================
python manage.py shell <!-- To run the shell for some testings-->
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoursite.settings')
django.setup()
from django.contrib.auth.models import User
from user_dashboard.models import TraderData
from user_dashboard.models import AdminDashboardData 
from myaccount.models import Profile
<!-- #### Model QuerySets -->
TraderData.objects.all()
AdminDashboardData.objects.all()
Profile.objects.all()
<!-- Creating model instance -->
user = User.objects.create(username='ken')
email = 'user@gmail.com'
traders = TraderData.objects.create(user=user, email=email)
<!-- Deleting a model instance(s) -->
TraderData.objects.all().delete()
<!-- #### User Model QuerySets -->
User.objects.all()
User.objects.filter().last()
<!-- Creating a user -->
user = User.objects.create_user('testuser', password='testpassword')
<!-- Deleting user(s) -->
User.objects.all().delete()
User.objects.filter().first().delete()
<!-- Esc deleting superuser -->
User.objects.filter(is_superuser=False).delete()
<!-- customuser operations -->
CustomUser.objects.filter().last()
===================================================================================================
### GIT & GITHUB
===================================================================================================
<!-- ### Create local repo and commit -->
git status
git init <!-- or `git init -b main` -->
git add . <!--or to add all files `git add CMDs-Readme.md` -->
git commit -m "first commit" <!-- git commit -m "new update" -->
<!-- Create Remote Repo and Push to remote repo  -->
git remote add origin https://github.com/syntaxland/django-stock-traders.git
git branch -M main
git push -u origin main
<!-- ### Updating to remote repo -->
git remote -v
git push origin main 
<!-- ### Git Branching and Checkout -->
git branch <!--To see local -->
git branch -r <!--To checkout remote... git checkout <remote-branch-name> -->
git branch -a <!--To checkout both -->
<!-- Pulling from remote origin -->
git pull origin main
===================================================================================================#### Docker | Docker Compose | kubernetes
===================================================================================================
#### Docker
docker -v
docker version
docker ps -a
<!-- Build and run Docker Image: -->
docker pull <image-name>
docker images
docker rmi <image-name-or-id>
docker build -t traderapi . <!-- To build image. Add trailing `.` to build at pwd -->
docker run -p 8000:8000 traderapi <!-- To run the built image -->
<!-- Pushing Images to Docker Hub: -->
docker login
docker tag <image-name-or-id> <username>/<repository>:<tag>
docker push <username>/<repository>:<tag> 
docker tag traderapi jondebosco/traderapi:v1.0 <!-- Tag the built image -->
docker push jondebosco/traderapi:v1 <!-- Then push the image -->
<!-- Build and run Docker Image: -->
docker exec -it djangoapi_container /bin/bash
docker exec -it 8a2449609dee7b579 /bin/sh
docker exec -it 6343202eec sh
vi filename
i => insert mode
Esc => excape
:wq => save exit 
<!-- Docker Container CMD -->
docker start <contaner-name or id>
docker restart <contaner-name or id>
docker stop  <contaner-name or id>
#### Docker-Compose 
docker-compose run <image>
docker-compose run django-admin startproject core .
docker-compose build
docker-compose up
docker-compose up --build -d
docker-compose up -d
<!-- Some Docker Volume CMDs-->
docker volume ls
docker volume rm
<!-- Error Handling -->
<!-- # RUN pip install --no-cache-dir -r requirements.txt -->
docker builder prune
docker-compose build --no-cache
docker-compose up -d
#### kubernetes
<!-- Stopping kubernetes pods: -->
kubectl get pods
kubectl delete pod <pod-name>
kubectl delete pod pod1 pod <!-- or kubectl delete pod -l <label-selector> -->
kubectl delete pod server-57674c8695-rnpv2 
kubectl delete pod mongo-6cf8cb4db5-kz9hq myapp-79f957b9b9-97db5 server-57674c8695-rnpv2 
<!-- To run Kubernetes containers: -->
kubectl get deployments
kubectl get replicationcontrollers
kubectl scale deployment <deployment-name> --replicas=<desired-replicas>
kubectl apply -f <path-to-updated-config-file>
<!-- Deploying fullstack app with kube -->
kubectl create -f mongo-d.yml
kubectl delete -f app-s.yml 
kubectl apply -f app-d.yml
===================================================================================================
### AWS (Cloud)
===================================================================================================
pip install awscli <!-- for aws cmds --> 
===================================================================================================
### CI-CD | GitHub Actions | Jenkens | AWS CodePipeLine
===================================================================================================
