#!/bin/bash
IS_UI10=0
IS_UI20=0
if [[ "$HOSTNAME" =~ "ui10" ]];then
    echo "@@ui10 kisti@@"
    IS_UI10=1
elif [[ "$HOSTNAME" =~ "ui20" ]];then
    echo "@@ui20 kisti@@"
    IS_UI20=1
else
    echo "NOT KISTI"
    #exit
fi



runshell=$1
njob=$2
inputtar=$3

if [ "NONE" == "$inputtar" ];then
    inputtar=""
fi

echo "===Make submit.jds==="

echo "executable = ${runshell}" > submit.jds 
echo "universe   = vanilla" >> submit.jds
echo "arguments  = \$(Process)" >> submit.jds

if [ $IS_UI20 -eq 1 ];then
    echo 'requirements = ( HasSingularity == true )' >> submit.jds
    echo 'accounting_group = group_cms' >> submit.jds
    echo '+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el6:latest"' >> submit.jds
    echo '+SingularityBind = "/cvmfs, /cms, /share"' >> submit.jds
fi
if [ $IS_UI10 -eq 1 ];then
    echo 'requirements = OpSysMajorVer == 6' >> submit.jds
fi



echo "log = condor.log" >> submit.jds
echo "getenv     = True" >> submit.jds
echo "should_transfer_files = YES" >> submit.jds
echo "when_to_transfer_output = ON_EXIT" >> submit.jds
echo "output = job_\$(Process).log" >> submit.jds
echo "error = job_\$(Process).err" >> submit.jds
if [ -z "$inputtar" ]
then
    echo "NO INPUT FILES to condor worknode"
else
    echo "transfer_input_files = $inputtar" >> submit.jds
fi
#echo "use_x509userproxy = true" >> submit.jds
#echo "transfer_output_remaps = \"*inDQM.root = OUTPUT_\$(Process).root\"" >> submit.jds
echo "queue $njob" >> submit.jds

echo "===DONE. submit.jds=="
