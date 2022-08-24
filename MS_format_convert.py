#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:58:39 2022
Make sure all preprocessing (centering, smoothing ect.) is already done with 
 Thermo ms convert on the raw data. Use pyopenms/this code 
 only for converting from mzML to mzXML or mzXML to mzML.
@author: Jens Settelmeier
"""
import os
import argparse
import glob

from pyopenms import MSExperiment, MzXMLFile, MzMLFile
import os


def convertFormat(path, input_format='mzXML', output_format='mzML'):
    """

    Parameters
    ----------
    path : str
        path to the folder with the files that should be converted.
    input_format : str, optional
        File format of the input file. mzXML and mZML 
        are supported. The default is 'mzXML'.
    output_format : str, optional
        Target file format. mzML and mzXML are supported.
        The default is 'mzML'.

    Raises
    ------
    ValueError
        Error if unsupported file format or file format of input and target
        are the same.

    Returns
    -------
    experiment : pyopenms object
        Returns the aquaistion as pyopenms object for further processing 
        in python.

    """
    os.chdir(path)
    filenames = glob.glob(f'*.{input_format}')
    if input_format == 'mzXML' and output_format == 'mzML':
        for file in filenames:
            experiment = MSExperiment()
            MzXMLFile().load(os.path.join(os.getcwd(),file), experiment)
            file = file[:-6]
            MzMLFile().store(f"{file}.mzML", experiment)
    elif input_format == 'mzML' and output_format == 'mzXML':
        for file in filenames:
            experiment = MSExperiment()
            MzMLFile().load(os.path.join(os.getcwd(),file), experiment)
            file = file[:-5]
            MzXMLFile().store(f"{file}.mzXML",experiment)
    else:
        raise ValueError('Format not supported or input is equal to ouput format')
    return experiment
    

def parse_args():
    """
    Returns
    -------
    args : TYPE
        Default argument parser for console execution.
    """
    parser = argparse.ArgumentParser(description='Convert mzML or mzXML to mzXML or mzML.')
    parser.add_argument('--p', '--path', type=str, default = os.getcwd(), help='path to the folder containing all files to be converted')
    parser.add_argument('--i', '--input_format', type=str, default = 'mzXML', help='input file format. Default is mzXML')
    parser.add_argument('--o', '--output_format', type = str, default = 'mzML', help='target file format')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    experiment = convertFormat(args.p, args.i, args.o) # why is **args not working...?
