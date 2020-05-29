#!/usr/bin/env python3
'''
Created on 7 Jun 2019

@author: saumitras '''
from argparse import ArgumentParser

'''
Convert Gromacs created PDB files into xyz fromat
'''


def ReadPDB(args):
    fname = args.inpfile
    atomno = 0
    with open(fname, 'r') as pdbfile:
        for line in pdbfile:
            if line[:4] == 'ATOM' or line[:6] == "HETATM":
                atomno += 1
            else:
                pass
    return fname,atomno


def WriteXYZ(args):
    fname,ano=ReadPDB(args)
    with open(fname, 'r') as pdbfile, open(args.outfile, 'w') as xyzfile:
        xyzfile.write(str(ano) + '\n')
        xyzfile.write(fname + '\n')
        for line in pdbfile:
            if line[:4] == 'ATOM' or line[:6] == "HETATM":
                # Split the line
                splitted_line_xyz = [line[77:79].rstrip(), line[30:38], line[38:46], line[46:54]]
                # print splitted_line_xyz
                # To format again the pdb file with the fields extracted
                xyzfile.write("%4s    %8s%8s%8s\n" % tuple(splitted_line_xyz), )


if __name__ == '__main__':
    # Initialize parser.
    parser = ArgumentParser(description='Convert .pdb file into .xyz')
    parser.add_argument('-i', dest="inpfile", type=str, help='name of input in PDB format')
    parser.add_argument('-o', dest="outfile", type=str, help='name of output in XYZ format')
    parser.set_defaults(func=WriteXYZ)
    #     ReadPDB('1grl.pdb')

    args = parser.parse_args()
    print(args)

    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        exit(0)
    args.func(args)

    pass
