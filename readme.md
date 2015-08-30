There is a utility called clinfo that comes in the debian package called
amd-clinfo - AMD OpenCL info utility

This python program reads the output from clinfo. The clinfo command
gathers hardware info about the system, including the type of GPU and the
amount of memory on the GPU.

The output from this program should look something like this:

Board name: AMD Radeon (TM) R9 270 Series
Global memory size: 1979711488


chmod +x clinfo-parse.py

Then this program can be run like this:

clinfo|./clinfo-parse.py

or

clinfo > clinfo.txt
./clinfo-parse.py clinfo.txt


or 

cat clinfo.txt|./clinfo-parse.py

The last one is for cat lovers.
