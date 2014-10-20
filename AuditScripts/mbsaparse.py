#######################################
#Read XML v0.1                        #
#Description:                         #
#read MSBA xml files and print        #
#patches.                             #
#                                     #
#Author: l4mers3c                     #
#                                     #
#Usage:                               #
#Add to the directory                 #
#in which the XML file is located     #
#root@bt:~#python readxml.py test.xml #
#######################################
#
#
#!/usr/bin/env python
#####################

import sys
import os

from xml.etree import ElementTree

def notinstalled():
 for node in ser.iter('UpdateData'):
    installed = node.attrib.get('IsInstalled')
    if installed == 'false':
            bid = node.attrib.get('BulletinID')
            if bid:
                BulletinID = bid
            else:
                bid = node.attrib.get('ID')
    
            severity = node.attrib.get('Severity')
            
            for title in node.getiterator('Title'):
                gettitle = title.text
            print "{:<10}{:^20}{:^10}".format(bid,severity,gettitle)


def installed():
 for node in ser.iter('UpdateData'):
    installed = node.attrib.get('IsInstalled')
    if installed == 'true':
            bid = node.attrib.get('BulletinID')
            if bid:
                BulletinID = bid
            else:
                bid = node.attrib.get('ID')
            severity = node.attrib.get('Severity')
           
            for title in node.getiterator('Title'):
                gettitle = title.text
            print "{:<10}{:^20}{:^10}".format(bid,severity,gettitle) 


def main():
#Give Options for Installed or Not
    try:       
        print "Which do you want to see? Installed or Not Installed"
        print "[*] Installed = 1"
        print "[*] Not Installed = 2"
        choice = raw_input("\tChoice: ")
        answer = int(choice)
        if answer == 1:
            installed()
        elif answer == 2:
            notinstalled()
    except ValueError:
        print "Did not understand your choice!"
        sys.exit(-1)

if __name__ == "__main__":
    try:
        #Open File and parse with ElementTree
        file = sys.argv[1]
        ser = ElementTree.parse(file)
        main()
    except IndexError:
        print 'Usage: %s <inputfile.xml>' % sys.argv[0]
        sys.exit(-1)
