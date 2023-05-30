#!/bin/bash

HOME=/home/pi/sensor_garden
VENVDIR=$HOME/sensor_garden_venv
MAINDIR=$HOME/tom_project_2020

cd $MAINDIR
source $VENVDIR/bin/activate
$VENVDIR/bin/python3 $MAINDIR/main.py
export  GOOGLE_APPLICATION_CREDENTIALS="/home/pi/sensor_garden/tom_project_2020/sensor-garden-function-auth.json"