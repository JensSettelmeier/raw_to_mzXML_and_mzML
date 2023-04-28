#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:56:22 2022
add iRTs to a database. Usefull for Fragpipe workflow, since
Fragpipe does not include them automatically. 
@author: Jens Settelmeier
"""

import mmap
import os
import shutil
import argparse

def checkiRT(path2database, database_name):
    """

    Parameters
    ----------
    path2database : str
        Path to the folder where the database is stored.
    database_name : str
        The name of the database stored in path2database.

    Returns
    -------
    new_name : str
        Returns the name of the new database which is iRTs_<database_name>.

    """
    database = os.path.join(path2database,database_name)   
    with open(f'{database}', mode='r+', encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as s:

            if s.find(b'LGGNEQVTRYILAGVENSKGTFIIDPGGVIRGTFIIDPAAVIRGAGSSEPVTGLDAKTPVISGGPYEYRVEATFGVDESNAKTPVITGAPYEYRDGLDAASYYAPVRADVTPADFSEWSKLFLQFGAQGSPFLK') != -1:
                print('iRTs included')
            else:
                print('add iRTs')
                lines = ['>Biognosys|iRT-Kit_WR_fusion GN=iRTKit', 'LGGNEQVTRYILAGVENSKGTFIIDPGGVIRGTFIIDPAAVIRGAGSSEPVTGLDAKTPVISGGPYEYRVEATFGVDESNAKTPVITGAPYEYRDGLDAASYYAPVRADVTPADFSEWSKLFLQFGAQGSPFLK']
                with open('iRTs.txt', 'w') as f:
                    for line in lines:
                        f.write(line)
                        f.write('\n')
                new_name = f'iRTs_{database_name}'
                with open(new_name,'wb') as wfd:
                    for doc in ['iRTs.txt',f'{database}']:
                        with open(doc,'rb') as fd:
                            shutil.copyfileobj(fd, wfd)
                wfd.close()
                f.close()
                database_name = new_name
                # check if iRTs are correctly added
                checkiRT(path2database, database_name)
                return new_name
            s.close()
        return 
    

def parse_args():
    """

    Returns
    -------
    args : TYPE
        Default argument parser for console execution.

    """
    parser = argparse.ArgumentParser(description='Adds the iRTs to a database.')
    parser.add_argument('--p', '--path2database', type=str, default = os.getcwd(), help='path to the folder with the database')
    parser.add_argument('--n', '--database_name', type = str, default = 'database.fasta', help='Name of the database fasta or fas file.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    new_name = checkiRT(args.p, args.n) # why is **args not working...?
