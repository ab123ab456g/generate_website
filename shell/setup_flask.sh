mkdir $1
cd $1
python3 -m virtualenv venv
mkdir app
mkdir app/templates
echo 'from app import app' > $1.py
cp $1.py test.py

echo 'python -m smtpd -n -c DebuggingServer localhost:8025' > start_mail_server.sh

echo 'export FLASK_APP='$1.py > venv.env

cp ../file/__init__.py app/__init__.py

cp ../file/*.py app/
cp ../file/*.html app/templates/



echo 'pip freeze > requirements.txt' > Gen_requirements.sh
echo 'pip install -r=requirements.txt' > install_requirements.sh

git init
git add .
git commit -m 'first commit, Init Project : $1 demo'
