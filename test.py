import os
import numpy as np
import subprocess
import re
import errno

localdir1 = r'C:\Users\miaok\Desktop\Ti_Ref'
# Directory where Fit2D (fit2d_12_077_i686_WXP.exe) is
fit2dpath = r'F:\OneDrive - 哈尔滨工业大学\PythonCode\XRDring2line\Fit2d'
# Directory where the Python macros are found, must be a subdirectory
# of 'localdir1', do not change this
setupdir = localdir1+"/setup"
fit2dversion = "fit2d_12_077_i686_WXP.exe"
os.chdir(fit2dpath)
p = subprocess.Popen(str(fit2dversion+' -dim2048x2048 -macfit2dint.mac'))
p.wait()