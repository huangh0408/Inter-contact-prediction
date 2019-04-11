#!/bin/sh

for i in $(cat 3_28.txt);do
	a=`echo $i|cut -d '/' -f 6`
	b=`echo $a|cut -d '.' -f 1`
	echo $b >>list.txt
done
