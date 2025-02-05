from typing import Union
import argparse
import os

def read_file(file):
    return open(file, "r")

def write_file(data:Union[str, list[str]], file: str, append: bool = False):
    # if I want to append to the file I can use the append option.
    # this will decrease the total memory cost by using constant memory instead
    # of reading both files in entirety and then writing them out
     
    if append:
        f = open(file, "a")
        f.write(data)
    else:
        f = open(file, "w")
        f.writelines(data) 


def check_for_dupes(potential_dupe, line, fp):
    while potential_dupe == line:
        line = fp.readline()
    return line

def xor_merge(file1, file2):
    fp1 = read_file(file1)
    fp2 = read_file(file2)
    line1 = fp1.readline()
    line2 = fp2.readline()
    out1 = 'output1.txt'
    out2 = 'output2.txt'
    potential_dupe = None
    while line1 and line2:
        # if line1 is greater than line2 we know line2 is unique, since we are ascending
        if line1 > line2:
            write_file(line2, out2, append=True)
            line2 = fp2.readline()
        # visversa
        elif line1 < line2:
            write_file(line1, out1, append=True)
            line1 = fp1.readline()
        # if they match skip
        else:
            # if there is a duplicate we need to retain the value
            potential_dupe = line1
            line1 = fp1.readline()
            line2 = fp2.readline()
        line1 = check_for_dupes(potential_dupe, line1, fp1)
        line2 = check_for_dupes(potential_dupe, line2, fp2)
    
    # If any lines remain in fp1 or fp2, write them
    while line1:
        write_file(line1, out1, append=True)
        line1 = fp1.readline()

    while line2:
        write_file(line2, out2, append=True)
        line2 = fp2.readline()
    # if the file has no records, we need to create it and leave it empty
    if not os.path.exists(out1):
        write_file('', out1)
    if not os.path.exists(out2):
        write_file('', out2)
    
        
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="Name of first file",
                type=str)
    parser.add_argument("file2", help="Name of second file",
                type=str)
    args = parser.parse_args()  
    xor_merge(args.file1, args.file2)
    


    
    
        

        