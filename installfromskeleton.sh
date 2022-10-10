#!/bin/bash

# create a test env in tmp dir
# clone model and a test app
# overwrite model with 

# templates
# static 
# pages urls
# forms

# in the future anything defined will overwrite the skeleton otherwise it will be left unchanged

# needs tests

#set -e

export testdir=/tmp/test-skel
mkdir -p ${testdir}
echo ${skelrepopath}


cd ${testdir}
git clone git@github.com:uklg/django-site-docker-models.git
git clone git@github.com:YellLabs/django-site-docker-jmd.git




rm -rf django-site-docker-models/staticfiles-to-build/*
rm -f django-site-docker-models/pages/urls.py
rm -r django-site-docker-models/pages/forms.py
rm -r django-site-docker-models/pages/views.py
rm -rf django-site-docker-models/pages/templates/*


cp -pr django-site-docker-jmd/staticfiles-to-build/* django-site-docker-models/staticfiles-to-build/
cp django-site-docker-jmd/pages/urls.py django-site-docker-models/pages/urls.py
cp django-site-docker-jmd/pages/forms.py django-site-docker-models/pages/forms.py
cp django-site-docker-jmd/pages/views.py django-site-docker-models/pages/views.py
cp django-site-docker-jmd/pages/templates/* django-site-docker-models/pages/templates/
 


echo $(pwd)

cd 




