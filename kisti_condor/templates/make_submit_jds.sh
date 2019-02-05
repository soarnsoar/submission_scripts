runshell=$1
njob=$2
inputtar=$3


echo "===Make submit.jds==="

echo "executable = ${1}.sh" >> submit.jds 
echo "universe   = vanilla" >> submit.jds
echo "arguments  = \$(Process)" >> submit.jds
echo "requirements = OpSysMajorVer == 6" >> submit.jds
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