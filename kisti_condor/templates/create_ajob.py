#!/usr/bin/python
#runshell=$1
#njob=$2
#inputtar=$3


###To emulate "source"

import argparse

parser = argparse.ArgumentParser()
####Set options###
parser.add_argument("--runshell", help="shell file to run")
parser.add_argument("--inputtar", help="input file to pass")
parser.add_argument("--njob", help=" number of jobs")
parser.add_argument("--jobname", help=" job name")
parser.add_argument("--nosubmit", help=" No submit. Only create the jobdir")

args = parser.parse_args()

if args.jobname:
    jobname = args.jobname
else:
    print "need --jobname argument"
    quit()

if args.nosubmit:
    submit = False
else:
    submit = True



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
currentPath = os.getcwd()

os.system("mkdir -p JOBDIR_"+jobname)
os.system("make_submit_jds.sh "+runshell+" "+str(njob)+" "+inputtar)
os.system("mv submit.jds JOBDIR_"+jobname)
os.system("cp "+runshell+" JOBDIR_"+jobname)
os.chdir(currentPath+"/JOBDIR_"+jobname)
script="submit_tmp.sh"
f_new = open(script,'w')
f_new.write('condor_submit submit.jds')
f_new.close()
os.chmod(script, 0755)



if submit == True:
    import subprocess
    submit=subprocess.Popen(["/bin/bash","-i","-c","source "+script])
    submit.communicate()


os.chdir(currentPath)
