#!/bin/bash
 
NAME="tecon"                                  # Name of the application
DJANGODIR=/home/delremm/webapps/tecon/tecon             # Django project directory
URL=127.0.0.1:23227  # we will communicte using this unix socket
NUM_WORKERS=2                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=hello.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi.production                     # WSGI module name
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $DJANGODIR
source /home/delremm/.virtualenvs/tecon/bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=URL
