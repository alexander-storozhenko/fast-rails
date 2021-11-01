# postgres

sudo apt-get install postgresql postgresql-contrib libpq-dev
cd /home
sudo -u postgres createuser -s $USER_NAME --createdb
cd 
sudo systemctl restart postgresql
