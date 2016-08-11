#!/usr/bin/env python

import argparse
import io 
import subprocess

# making a cp of original w/changed output
# name separation--> output name

exp = raw_input('File to preprocess: ')  # change name here to your fileName.txt
x = 0
for i in range(len(exp)):
    if(exp[i] == '.'):
        x = i
        break
part1 = exp[:x]
part2 = exp[x:]
cpfile = part1 + '_full' + part2

# may not need copy...active copy that records new ver of input file minus the 
# parts you need to transform
# shutil.copyfile(exp, cpfile) --> not needed. Copy process productive for script

tmp = 'tmp.txt'
counter = 0
## initial test model
# will take an input file and output file and transfer specific chunk to output
with open(exp, 'r') as file1, open(cpfile, 'w') as file2, open(tmp, 'w') as file3:
    # cp input file until first snippet found
    for null_line in file1:
        if '[**' in null_line:
            init_pos = file1.tell()
            break
        else:
            file2.write(null_line)
            counter+=1

    # reads through snippet and stores in tmp file for conversion
    for line in file1:
        if '**]' in line:
            break
        else:
            file3.write(line)
            
    # finishes cp of rest of input file
    for line in file1:
        file2.write(line)

    file1.close()
    file2.close()
    file3.close

# bash markdown command + redirecting output to tmp file
f = open('new_tmp.txt', 'w')

# applying markdown -> html conversion
cmd = ['perl', 'Markdown.pl', tmp]
subprocess.check_call(cmd, stdout = f)
f.close()

# concats cp of input file with transformed snippet 
with open(cpfile,'rw+') as f2:
    for c in range(counter):
        f2.readline()
    init_pos = f2.tell()
    remainder = f2.read()
    f2.seek(init_pos)
    with open('new_tmp.txt','r') as f3:
        f2.write(f3.read())
    f2.write(remainder)



