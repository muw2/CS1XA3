#!/bin/bash
#WORKING SCRIPT

#5.1 Script Input

echo "Hello, "$USER". Do you want to check a number is positive or negative, odd or even?"

echo -n "Please enter an integer and press [ENTER]"
read int

if [$int -eq 0]; then
	echo "$int is zero"
else
	if [$int -lt 0]; then
		echo "$int is negative."
	else 
		echo "$int is positive."
	fi
	if [$((int % 2)) -eq 0]; then
		echo "$int is even."
	else 
		echo "$int is odd"
	fi
fi

echo -n "If you think I am helpful, do you want to be Cosmo's friends?"

echo -n "Enter your name and press [ENTER]"
read name
echo -n "Enter your gender (man or woman) and press [ENTER]"
read gender
echo -n "How old are you?"
read age
echo -n "Which sport do you like?"
read sport
echo "Hello my friend $name, I know you are a $age year old $gender, and you like playing $sport. Now we are friends!"

#5.2 Create a TODO Log

git grep -EI "TODO" >todo.log

#Custom Feature

num=$[RANDOM%100+1]
while :
do
	read -p "There is a number between 1 and 100, you think the number is: " m
	if [ $m -eq $num ]; then
		echo "Congratulations! You get the number!"
		exit
	elif [ $m -gt $num ]; then
		echo "Ooooooops, the number is less than what you guess."
	else 
		echo "Ooooh, the number is greater than what you guess."
	fi
done

