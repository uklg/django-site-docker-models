you can set up a Django environment in Docker using ./build 

To use whitenoise (Production handling of static files and caching as such in code)  /admin with css works with debug but not with debug off the css files are missing

To get the admin css  for the staticfiles/admin you can:

./build 

attach to latest container

cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin/static/admin /app/staticfiles/

ow these files can be added to the admin and added to git locally as they are in the repo now



fixes

500 no correct hosts file

500 for form no env file

forms error (wrong version of django - fixed now)


if css does not update then remove staticfiles dir from server republish and restart app

this may not work as debug is turned off and static generation needs to happen in none debug mode




env,dynamically loading, mounted volume,  css_works with debug,

debug, yes, /code, true
prod, no, /app, false


 pip freeze to get a manifest of  versions at run time and apply them to requirements.txt.


### Dev mode

in dev mode can change the code including config on the fly and it makes process restart.

the css is provided by the static to build which is not populated on 

env,DEBUG, css (static load working) Ctrl-f5


dev, False, not working
prod, False, working
dev, True, working
prod, dev, working

s
o only dev non debug is broken and that is ok.

Probably due to the volume being dynamically mounted and this is not OK for dev in non debug






 use this and doc the git logs to get rest
https://docs.docker.com/compose/environment-variables/

htps://docs.docker.com/compose/environment-variables/



./build will build a prod env without dynamic updates of code, sans debug panel

./build debug will have dynamic updates and debug panel



param > build > docker-compose > dockerfile > docker environment
              > firefox
              > unit test

 

./build


will build docker env with prod qualities

no dynamic code updates
no debug toobar.


./build debug

will build docker env with debug settings on and debug toolbar and app restarts on code changes

/build rebuild will rebuild database after change

the reason the db stays is because it is generated in debug but copied over so need to remove it at start of build


## Make a new skeleton repo


./installfromskeleton.sh
