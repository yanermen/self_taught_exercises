if [ "$( sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='it_app'" )" = '1' ]
then
    echo "Database already exists.Succeed."
else
    sudo su - postgres -c "createdb it_app"
fi

