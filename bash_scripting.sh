#!/bin/bash

myFunction()
{
myOS=`uname -a`
echo "$myOS"

read -p "Please, enter your OS's name: " x

counter=0

if [ "$x" == "Linux" ]; then
	echo "YOU CHOSE RIGHT OS"
	sudo apt-get update && sudo apt-get upgrade
elif [ "$x" == "MacOS" ]; then
	while [ $counter -lt 10000 ]; do
		echo -n " CHOOSE LINUX "
		counter=$(($counter+1))
done
else 
	for ((j=0; j<10000; j++)); do
		echo -n " BOOM "
done
fi
}

myFunction



