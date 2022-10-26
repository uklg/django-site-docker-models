#!/bin/bash

export fname=a.txt
export fname=c.txt
export uname='blah'


if [ "$fname" = "a.txt" ] || [ "$fname" = "c.txt" ]

then

echo inside: $fname $

fi

if [ "$fname" = "a.txt3434" ] || [ "$uname" = "blah" ]

then

echo inside2: $fname $

fi

