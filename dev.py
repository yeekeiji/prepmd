#!/usr/bin/env python

from subprocess import check_call
import argparse

# Command line argument parsing
def cmdLineParse():
    '''runs through rudimentary argparse commands to parse name of files
       input:
            none
       output:
            array holding file names you wish to process
    '''
    # create a cmdline parser object
    parser = argparse.ArgumentParser(description="converts marked snippets of markdown to html")
    
    #define possible arguments and flags
    parser.add_argument('file',type=str, nargs='+', help="name of file(s) you wish to process")

    #find name of files to process
    filesToProc = parser.parse_args()
    return filesToProc.file 

def newName(fName, N=None):
    '''creates a new file name from input filename
       input:
            fName: Name of original file you want a modified ver of
            N: int you want to append at the end of fName
       output:
            str holding a modified filename of fName
    '''
    if N == None:
        fileCount = '_full'
    else:
        fileCount = str(N)

    # sep index
    j = 0

    # ext & name sep. Finds index of '.' in fName
    for i in range( len( fName ) ):
        if fName[i] == '.':
            j = i
            break

    # breaks fName into two parts name and ext to allow insert of fileCount
    part1 = fName[:j]
    part2 = fName[j:]
    return (part1 + fileCount + part2) 

def getSnippet(readFile, delim, N=None):
    '''creates a tmp file of just deliminated snippet from readFile
       input:
            readFile: file you are extracting the snippet from
                    NOTE: expects an already opened file stream name
            delim: the deliminator that the encloses snippet
            N: int you want to designate this particular snippet
                Usually used for multiple snippets being generated
       output:
            void function. Doesn't return a value.
            generates a tmp snippet file in pwd
    '''
    # gen name of tmp file
    tmp = newName('tmp.md', N)
    
    # extract snippet from ALREADY open file stream
    with open(tmp, 'w') as f:
        for line in readFile:
            if delim in line:
                break
            else:
                f.write(line)

        f. close()
    return

def tranSnippet(snipFile, outFile):
    '''Transforms snippet from Markdown (.md) to html
       input:
            snipFile: str of snippet file you want to transform
            outFile: output file or stdout. Place you want to output to
       output:
            void function. outputs html file to outFile

       Note: requires the Markdown.pl and perl file to exe
    '''
    # command line sequence to transform markdown file
    cmd = ['perl', 'Markdown.pl', snipFile]

    # calls cmd line command and outputs to outFile 
    check_call(cmd,stdout = outFile)
    return

def cleaningUp(N):
    if N == 0:
        return
    for i in range(N):
        tmpFile = newName('tmp.md',i)
        cmd = ['rm',tmpFile]
        check_call(cmd)
    return

def main():
    f_args = cmdLineParse()
    for f in f_args:
        inFile = f 
        outFile = newName(inFile)
        delimB = '[**'
        delimE = '**]'
        snippetCount = 0
        
        # outermost loop to translate md to html in one read
        try:
            f0 = open(inFile,'r')
            f1 = open(outFile,'w')
        except:
            print("Can't read file, invalid type, misspelling, not in dir.")
            return

        # read through infile once. appends desired snippet as it goes
        for line in f0:
            if delimB in line:
                getSnippet(f0,delimE,snippetCount)
                snipFile = 'tmp' + str(snippetCount) + '.md'
               
                # temp fix for output ordering issue
                f1.close()
                f1 = open(outFile,'a')

                tranSnippet(snipFile,f1)
                snippetCount += 1
            else:
                f1.write(line)
        
        # close file streams & rm temp files
        f0.close()
        f1.close()
        cleaningUp(snippetCount)

    return

if __name__ == '__main__':
    main()
