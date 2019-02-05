#!/usr/bin/python
#runshell=$1
#njob=$2
#inputtar=$3


###To emulate "source"

import argparse
import os
parser = argparse.ArgumentParser()
####Set options###
parser.add_argument("--runshell", help="shell file to run")
parser.add_argument("--inputtar", help="input file to pass")
parser.add_argument("--njob", help=" number of jobs")
parser.add_argument("--jobname", help=" job name")
parser.add_argument("--nosubmit", help=" No submit. Only create the jobdir", action = "store_true")


args = parser.parse_args()

if args.jobname:
    jobname = args.jobname
else:
    print "need --jobname argument"
    quit()



if args.runshell:
    runshell = args.runshell
    os.chmod(runshell, 0755)
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



if args.nosubmit == True:
    print "no submitssion"
    submit=False
    
else:
    submit=True
import os
currentPath = os.getcwd()
JOBDIR=currentPath+"/../JOBS/JOBDIR_"+jobname+"/"
os.system("mkdir -p "+JOBDIR)
os.system("make_submit_jds.sh "+runshell+" "+str(njob)+" "+inputtar)
os.system("mv submit.jds "+JOBDIR)
os.system("cp "+runshell+" "+JOBDIR)
os.chdir(JOBDIR)
#script="submit_tmp.sh"
#f_new = open(script,'w')
#f_new.write('condor_submit submit.jds')
#f_new.close()
#os.chmod(script, 0755)



if submit == True:
    import subprocess
    #submit=subprocess.Popen(["/bin/bash","-i","-c","source "+script])
    #submit.communicate()
    os.system("condor_submit submit.jds")

os.chdir(currentPath)
print "@@OUTPUTDIR="+JOBDIR+"@@"
