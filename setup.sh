#!/bin/sh

SRC=http://community.nuxeo.com/static/releases/nuxeo-5.4.2/nuxeo-dm-5.4.2-tomcat.zip

mkdir $HOME/abiliancloud
mkdir $HOME/abiliancloud/instances
mkdir $HOME/abiliancloud/models

(
cd $HOME/abiliancloud/models
wget $SRC
unzip *.zip
)
