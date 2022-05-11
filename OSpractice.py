import os

Script = """
echo "hello world"

for i in {1..5}
do
  echo "number: $i"
done

"""

#using system, no output
#calls command in shell
os.system(Script)

print("\n")


#using popen to capture output
process = os.popen(Script).read()
print(process)

#using subprocess
import subprocess
import shlex

Script2 = "ls -l"
#shlex splits strings in a sequence of commands that subprocess requires
args = shlex.split(Script2) 

#subprocess runs command and stores output
p = subprocess.check_output(args)

#useful to decode output from a byte to standard UTF-8
p = p.decode("utf-8")
print(p)
