#!/bin/sh

echo "You can most probably ignore all the warnings"
echo

killall -9 java

for i in 1 2 3 4 5 6 7 8 9
do
  dropdb abilian$i
  sudo su postgres -c "dropdb abilian$i"
done

for pid in $(ps auxxxw | grep nginx | egrep -v '(grep|kill)' | cut -d' ' -f2)
do
  kill $pid
done

rm -rf ~/abiliancloud/instances/*
rm -rf ~/abiliancloud/abiliancloud.db

supervisorctl -c ~/abiliancloud//supervisor.conf shutdown

