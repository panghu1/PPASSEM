#!/usr/bin/python

import os
import sys
import struct

from reads import read
from kmerGenerator import kmerGenerator as generator

def update(dict,extra):
	for k,v in extra.items():
		if k in dict:
			if dict[k] == 255 or dict[k] + v > 255:
				dict[k] = 255
			else:
				dict[k] = dict[k] + v
		else:
			if v > 255:
				dict[k] = 255
			else:
				dict[k] = v
	return dict
def write(dict,output):
	fhandler = open(output,'wb')
	for k,v in dict.items():
		fhandler.write(struct.pack('<qB',k,v))
	fhandler.close()
def kmerCount(seqfile,klen,outprefix):
	gen = generator(klen)
	inputhandler = open(seqfile,'r')
	output = outprefix + '.kmer'
	total = 0
	lines = []
	kmers = {}
	for line in inputhandler:
		total = total + 1
		lines.append(line.rstrip('\n'))
		if total % 4 == 0:
			if lines[2][0] != '+':
				print('invalid fq file')
				sys.exit(0)
			rd = read(lines[0],lines[1],lines[3])
			kmers = update(kmers,gen.generateKmer(rd))
			lines = []
	write(kmers,output) 	

if __name__ == '__main__':
	
	try:
		fqfile = sys.argv[1]
		klen = int(sys.argv[2])
		outfile = sys.argv[3]
		kmerCount(fqfile,klen,outfile)
	except Exception as err:
		print(err)
		sys.exit()
	
