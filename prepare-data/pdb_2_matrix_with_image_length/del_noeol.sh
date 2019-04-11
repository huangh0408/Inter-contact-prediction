#!/bin/sh

for i in $(ls true_contact_matrix);do
#	file='./true_contact_matrix/$i'
	if diff /dev/null ./true_contact_matrix/$i | tail -1 | grep '^\\ No newline' > /dev/null;then 
		rm ./true_contact_matrix/$i
	fi
done
