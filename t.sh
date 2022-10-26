#!/bin/bash

export keep_db_file=True



# Is db file present
export filepresent=$(docker exec -it models-web ls /code/db.sqlite3 > /dev/null;echo $?)

export returncodelsdb=$(docker exec models-web test -f /code/db.sqlite3;echo $?)
echo ${returncodelsdb}


if [[ $keep_db_file == "False" ]] || [[ ${returncodelsdb} == "0" ]]
  # Only run if keeping the file
  then
  # docker exec -it ${projectname}-web /code/manage.py makemigrations
  # docker exec -it ${projectname}-web /code/manage.py migrate
  docker exec -it ${projectname}-web hostname -s
fi

