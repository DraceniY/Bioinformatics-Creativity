# Fastest way to download uniprot proteome from list of ID
# Yasmine Draceni March 2019

import os
# file must have be scientific ID of organisms separated by "_"

f = open("list-organism.txt", "r")

for i in f:
	names =i.replace("_" , "+").replace("\n" , "") 

	os.system ("curl 'https://www.uniprot.org/uniprot/?query=organism:"+names+"&format=fasta&include=no&compress=no' > "+names.replace("+", "_")+".fa")

	

