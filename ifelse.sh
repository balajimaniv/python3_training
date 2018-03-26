#!/bin/sh

# demonstrate if else statments

echo "Enter your age"

read age

if [ $age -ge 18 ]; then
	echo " you are elligible to vote"
else 
	echo " you are younger!!!"
fi


