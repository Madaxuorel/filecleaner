#!/bin/sh
USRNAME=$(whoami)
DIR="/home/$USRNAME/Documents/filecleaner"
if [ -d "$DIR" ]; then
   echo 1
else
   echo 0
fi