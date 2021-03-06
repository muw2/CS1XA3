#!/bin/bash
#WORKING SCRIPT

#5.1 Script Input

echo "Hello, "$USER". Do you want to check a number is positive or negative, odd or even?"

echo -n "Please enter an integer and press [ENTER]"
read int

if [ $int -eq 0 ]; then
	echo "$int is zero"
else
	if [ $int -lt 0 ]; then
		echo "$int is negative."
	else 
		echo "$int is positive."
	fi
	if [ $((int % 2)) -eq 0 ]; then
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
echo "Hello my friend $name, I know you are a $age year old $gender. Now we are friends!"

#5.2 Create a TODO Log

grep -r "#TODO" . --exclude={todo.log,project_analyze.sh}>todo.log

#5.3 Compile Error Log

find . -name "*.hs" -exec ghc -fno-code {} \; > compile_fail.log

#5.5 File Type Count
echo "HTML: $(find /home/muw2 -iname "*.html" |wc -l), Javascript: $(find /home/muw2 -iname "*.js" | wc -l), CSS: $(find /home/muw2 -iname "*.css" | wc -l), Python: $(find /home/muw2 -iname "*.py" | wc -l), Haskell: $(find /home/muw2 -iname "*.hs" | wc -l), Bash Script: $(find /home/muw2 -iname "*.sh" | wc -l)"

#5.6 Delete Temporary Files

git clean -n
echo "Are you sure to delete the files above, if yes enter 1 no enter 2"
read a
if [ $a -eq 1 ]; then
	git clean -f
fi

#Custom Feature 1

tm=$(date +%H)

if [ $tm -le 12 ]; then
	msg="Good Morning $USER"
elif [ $tm -gt 12 -a $tm -le 18 ]; then
	msg="Good Afternoon $USER"
else
	msg="Good Night $USER"
fi
echo "$(date +"%Y-%m-%d %H:%M:%S")"
echo -e "\033[34m$msg\033[0m"

#Custom Feature 2

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
