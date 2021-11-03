# postgres

sudo apt-get install postgresql postgresql-contrib libpq-dev
sudo -u postgres createuser -s $USER_NAME --createdb
sudo systemctl restart postgresql

sudo python ./py/pg_hba.py $USER_NAME