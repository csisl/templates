#!/bin/bash

RESET_TEXT="\e[39m"
RESET_BKGRD="\e[49m"
RESET_BLINK="\e[0m"

BLACK="\e[30m"
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAG="\e[35m"
CYAN="\e[36m"
GRAY="\e[37m"

BLINK="\e[5m"

# one sample echo statement with variables
#echo -e "${RED}RED $RESET_TEXT\n"
echo -e "${BLINK}BLINK $RESET_BLINK"

# print the regular text
# color codes 31 thru 37
for i in {31..37}; do
	echo -en "\e[${i}m\\\e[${i}m\t"
done

echo ""

# print the light text
# color codes 90 thru 97
for i in {90..97}; do
	echo -en "\e[${i}m\\\e[${i}m\t"
done

echo ""

for i in {41..46}; do
	echo -en "${BLACK}\e[${i}m\\\e[${i}m${RESET_BKGRD}\t"
done

echo ""

for i in {100..107}; do
	echo -en "${BLACK}\e[${i}m\\\e[${i}m${RESET_BKGRD}\t"
done

echo ""
