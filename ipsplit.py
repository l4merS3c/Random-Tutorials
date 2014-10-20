#!/usr/bin/python   

import sys

if __name__ == '__main__':
	try:
		myf = sys.argv[1]
		numl = int(sys.argv[2])
		sorting = True
		lines = []
		with open(myf,'r') as tf:
		    for row in tf:
			lines.append(row)
		oc = 1
		lc = 0
		while sorting:
		    count = 0
		    inc = (oc-1) * numl
		    it = len(lines) - inc
		    save = "ip_list%s" %(oc)+ ".txt"
		    newl = []
		    if it < numl:
			while count < it:
			    newl.append(lines[lc])
			    count += 1
			    lc += 1
			sorting = False
		    else:
			while count < numl:
			    newl.append(lines[lc])
			    count += 1
			    lc += 1
		    oc += 1
		    with open(save,'w') as newfile:
			for row in newl:
			    newfile.write(row)

			
	except IndexError:
		print 'Usage: %s <inputfile> <size>' % sys.argv[0]
		sys.exit(-1)