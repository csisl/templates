#!/bin/bash

# template to read a file with a bash script

# file you want to read
file=""

# make sure the file exists
if [[ ! -e $file ]]; then
	echo "$file does not exist, try again"
	exit
fi

# print the file contents
while IFS= read -r var
do
	echo $var
done < "$file"
