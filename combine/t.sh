#!/bin/bash
if [[ $1 == "rebuild" ]]
  then # this is next bit to be run after then
   echo inside loop: ${1}
fi


if [[ $1 == $(./t.py) ]]
  then # this is next bit to be run after then
   echo inside loop: ${1}
   
fi


echo $1|cat -A $1
