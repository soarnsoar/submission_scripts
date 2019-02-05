#!/usr/bin/python

#runshell=$1
#njob=$2
#inputtar=$3
import argparse
parser = argparse.ArgumentParser()
####Set options###
parser.add_argument("--runshell", help="shell file to run")
parser.add_argument("--inputtar", help="input file to pass")
parser.add_argument("--njob", help=" number of jobs")
args = parser.parse_args()



if args.runshell:
    runshell = args.runshell
else:
    print "need --runshell argument"
    quit()


if args.njob:
    njob = args.njob
else:
    print "no --njob argument"
    print "SET njob =1 !!"
    njob = 1


if args.inputtar:
    inputtar = args.inputtar
else:
    print "No input tar"
    inputtar = ""

import os
os.system("make_submit_jds.sh "+runshell+" "+str(njob)+" "+inputtar)
