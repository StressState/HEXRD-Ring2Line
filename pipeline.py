# -*- coding: utf-8 -*-
"""
Created on Tue Jan 08 15:32:08 2013

Pipeline script to automatically download and to process data with Fit2d.

Put all the files you get from the github to the "setup" folder,
which should be a subfolder of the folder which contains your data.
The data can also be in subfolders, but the "setup" folder may be
a subfolder of the main folder.
For example, you have data in d:\mydata\data1 and d:\mydata\data2
and you want to integrate both with the same parameters.
Then create a folder d:\mydata\setup and copy the *.py files and
the *.txt files into this setup folder.

Author: Ulla Vainio (ulla.vainio@hzg.de)
"""

##################### ------------------
localdir1 = input("输入数据文件夹路径：")
fit2ddir  = input("输入FIT-2D文件夹路径：")

# Local directory in which or in the subdirectories of which
# all the data that needs to be integrated is found

#localdir1 = r'C:\Users\miaok\Desktop\Ti_Ref'

# Directory where Fit2D (fit2d_12_077_i686_WXP.exe) is

#fit2ddir = r'F:\OneDrive - 哈尔滨工业大学\PythonCode\XRDring2line\Fit2d'

# Directory where the Python macros are found, must be a subdirectory
# of 'localdir1', do not change this
setupdir = localdir1+"/setup"

###################### -----------------

# Append python files to the path and import necessary libraries
import sys
sys.path.append(setupdir)
import speedyprocessing as sp

# Which txt file contains the integration parameters
cakefile1 = "mycakeparameters1.txt"


# Integrate data using the parameters defined in the cakefile
sp.automatedcakes(cakefile1,localdir1,fit2ddir)



###### -----
sys.path.remove(setupdir)
