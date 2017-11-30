#!/bin/bash

while read -r old new
do
	echo "$old -> $new"
	perl -pi -e "s|$old|$new|g" *.nt
done
