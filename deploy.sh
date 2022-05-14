# !/bin/bash
git pull

source ../qiusuo/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
uwsgi qiusuo_uwsgi.ini
