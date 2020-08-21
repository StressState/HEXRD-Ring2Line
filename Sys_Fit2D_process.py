# -*- coding: utf-8 -*-
"""
2020.08.18创建
用于处调用Fit2D进行批量化
Harbin Institute of Technology
Author: Kesong Miao
Modified from Ulla Vainio (ulla.vainio@hzg.de)
"""
import os
import numpy as np
import subprocess
import re
import errno



def cake(macpara, datapath, testflag):
    '''
    函数有两部分功能
    第一部分为根据参数生成对应的mac文件
    第二部分为调用Fit2D运行mac序列
    输入参数macpara（list格式），数据文件夹路径，测试模式“ON”或者其他
    '''
    #从macpara读取参数并转化为.mac文件需要的格式
    fit2dversion = "fit2d_12_077_i686_WXP.exe"
    firstazimuthangle = float(macpara[1])
    lastazimuthangle = float(macpara[3])
    innerradius = float(macpara[5])
    outerradius = float(macpara[7])
    radialbins = int(np.min([outerradius - innerradius, float(macpara[9])]))
    cake_azimuthal_bins = int("360")
    if macpara[13][:2] == "NO":
        maskfile = 'mask.msk'
        maskyesno = 'NO'
    else:
        maskfile = macpara[13][:len(macpara[13]) - 1]
        maskyesno = 'YES'
        print("Mask file: %s" % maskfile)
    if macpara[15][:2] == "NO":
        dcfile = 'darkcurrent.bin'
        dcyesno = 'NO'
    else:
        dcfile = macpara[15][:len(macpara[15]) - 1]
        dcyesno = 'YES'
    beamcenterx = float(macpara[17])
    beamcentery = float(macpara[19])
    wavelength = float(macpara[21])
    sample2detector = float(macpara[23])
    pixelsizex = float(macpara[25])
    pixelsizey = float(macpara[27])
    detectortiltrotation = float(macpara[29])
    detectortiltangle = float(macpara[31])
    detector = macpara[33][:len(macpara[33]) - 1]
    if detector == 'mar345':
        pixels1 = 3450
        pixels2 = 3450
        file_extension = ".mar3450"
    elif detector == 'perkinelmer':
        pixels1 = 2048
        pixels2 = 2048
        file_extension = ".tif"
    elif detector == 'pilatus300k':
        pixels1 = 487
        pixels2 = 619
        file_extension = ".tif"
    else:
        errorsfound = 1
        print("未识别探测器 %s!" % detector)
        print("当前处理无法继续进行")
    #    fit2dpath           = parameters[35][:len(parameters[35])-1]
    scantype = macpara[37][:len(macpara[37]) - 1]
    if macpara[39][:2] == 'NO':
        overwriting = 0
    else:  # Assuming it's YES
        overwriting = 1
    if macpara[41][:3] == 'OFF':  # OFF
        pausing = 0
    else:  # Assuming it's ON
        pausing = 1
    subdirname = "integ_" + str(macpara[43])

    # 开始写入mac文件
    f = open("./fit2dint.mac", 'w')
    print('%!*' + '\\' + ' BEGINNING OF GUI MACRO FILE', file=f)
    print('%!*' + '\\', file=f)
    print('%!*' + '\\ This is a comment line', file=f)
    print('%!*' + '\\', file=f)

    print('I ACCEPT', file=f)
    print('POWDER DIFFRACTION (2-D)', file=f)

    # Counting how many file names exceed 80 characters for *.asc files
    errors = 0
    counterfiles = 0
    for dirpath, dirnames, filenames in os.walk(datapath):
        if dirpath[len(dirpath) - len(subdirname):] != subdirname:
            for file1 in filenames:
                prefix, postfix = os.path.splitext(file1)
                temp1 = re.findall("[\S\d]*(?=_\d{5}_\d{5})", prefix)
                tempb = re.findall("[\S\d]*(?=_\d{5})", prefix)
                temp1.extend(tempb)
                if len(temp1) > 0:
                    subdirprefix = min(filter(None, temp1), key=len)
                else:
                    subdirprefix = ''
                subpath = dirpath + "/" + subdirprefix + '/' + subdirname + "/"
                # As a default overwrite
                overwritingthisone = 1
                # If files exist, then don't overwrite if not allowed
                if os.path.isfile(subpath + prefix + ".chi") and cake_azimuthal_bins == 1 and overwriting == True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath + prefix + ".chi") and cake_azimuthal_bins == 1 and overwriting == False:
                    overwritingthisone = 0
                    print("Did not overwrite: %s" % subpath + prefix + ".chi")
                elif os.path.isfile(subpath + prefix + ".asc") and cake_azimuthal_bins > 1 and overwriting == True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath + prefix + ".asc") and cake_azimuthal_bins > 1 and overwriting == False:
                    overwritingthisone = 0
                    print("Did not overwrite: %s" % subpath + prefix + ".asc")
                # Compare extensions to find only the 2D files
                # Only accept the ones which are allowed to be overwritten
                if postfix == file_extension and overwritingthisone == True:
                    try:  # Try creating the subdirectory for integrated files if it does not exist
                        os.makedirs(subpath)
                    except OSError as exc:  # Python >2.5
                        if exc.errno == errno.EEXIST and os.path.isdir(subpath):
                            pass
                    if counterfiles == 0:
                        print("Preparing a fit2d.mac for files:")
                    counterfiles = counterfiles + 1
                    fullfile1 = dirpath + "/" + file1
                    print(fullfile1)
                    # Write to fit2d.mac
                    print("INPUT", file=f)
                    print(fullfile1, file=f)
                    # For some reason Pilatus 300k seems to require an extra OK
                    if detector == 'pilatus300k' or detector == 'perkinelmer':
                        print("O.K.", file=f)
                    # Define common parameters
                    print("DARK CURRENT", file=f)
                    print(dcyesno, file=f)
                    print("DC FILE", file=f)
                    print(dcfile, file=f)
                    print("O.K.", file=f)
                    print("CAKE", file=f)
                    if counterfiles == 1:
                        print("NO CHANGE", file=f)
                        print("           1", file=f)
                        print(" 3.1346145E+03", file=f)
                        print(" 1.7431051E+03", file=f)
                        print("           1", file=f)
                        print(" 3.0989375E+03", file=f)
                        print(" 1.7074276E+03", file=f)
                        print("           1", file=f)
                        print(" 1.8680677E+03", file=f)
                        print(" 1.7431051E+03", file=f)
                        print("           1", file=f)
                        print(" 3.4200337E+03", file=f)
                        print(" 1.7163469E+03", file=f)
                    if maskyesno == 'YES':
                        print("MASK", file=f)
                        print("LOAD MASK", file=f)
                        print(maskfile, file=f)
                        print("EXIT", file=f)
                    print("INTEGRATE", file=f)
                    print("X-PIXEL SIZE", file=f)
                    print(pixelsizex, file=f)
                    print("Y-PIXEL SIZE", file=f)
                    print(pixelsizey, file=f)
                    print("DISTANCE", file=f)
                    print(sample2detector, file=f)
                    print("WAVELENGTH", file=f)
                    print(wavelength, file=f)
                    print("X-BEAM CENTRE", file=f)
                    print(beamcenterx, file=f)
                    print("Y-BEAM CENTRE", file=f)
                    print(beamcentery, file=f)
                    print("TILT ROTATION", file=f)
                    print(detectortiltrotation, file=f)
                    print("ANGLE OF TILT", file=f)
                    print(detectortiltangle, file=f)
                    print("O.K.", file=f)
                    print("START AZIMUTH", file=f)
                    print(firstazimuthangle, file=f)
                    print("END AZIMUTH", file=f)
                    print(lastazimuthangle, file=f)
                    print("INNER RADIUS", file=f)
                    print(innerradius, file=f)
                    print("OUTER RADIUS", file=f)
                    print(outerradius, file=f)
                    print("SCAN TYPE", file=f)
                    if scantype == 'TTH':
                        print("2-THETA", file=f)
                    elif scantype == 'Q':
                        print("Q-SPACE", file=f)
                    elif scantype == 'RADIAL':
                        print("Q", file=f)
                    else:
                        print("SCAN TYPE NOT IDENTIFIED! USE TTH or Q.")
                    print("1 DEGREE AZ", file=f)
                    print("YES", file=f)
                    if radialbins == 1:
                        print("AZIMUTH BINS", file=f)
                        print(int(lastazimuthangle - firstazimuthangle), file=f)
                        print("RADIAL BINS", file=f)
                        print("1", file=f)
                    else:
                        print("AZIMUTH BINS", file=f)
                        print(cake_azimuthal_bins, file=f)
                        print("RADIAL BINS", file=f)
                        print(radialbins, file=f)
                    print("POLARISATION", file=f)
                    print("NO", file=f)
                    print("CONSERVE INT.", file=f)
                    print("NO", file=f)
                    print("GEOMETRY COR.", file=f)
                    print("YES", file=f)
                    print("MAX. D-SPACING", file=f)
                    print(1000.00000, file=f)
                    print("O.K.", file=f)
                    print("EXIT", file=f)

                    # 输出部分改动为同步输出矩阵和图

                    print("OUTPUT", file=f)
                    print("SPREAD SHEET", file=f)
                    print("YES", file=f)
                    print(subpath + prefix + ".spr", file=f)
                    if len(subpath + prefix + ".spr") > 79:
                        print("WARNING! Path is too long for saving *.spr files")
                        print(subpath + prefix + ".spr exceeds limit (80 caharacters). Length %d." % len(
                            subpath + prefix + ".spr"))
                        errors = errors + 1
                    print("YES", file=f)

                    if testflag == "ON":
                        break
    # Exit Fit2d at the end
    print("EXIT", file=f)
    print("EXIT", file=f)
    print("YES", file=f)
    print('%!*' + '\\' + ' END OF IO MACRO FILE', file=f)
    f.close()  # Close fit2d macro file

    if pausing == True:
        os.system("pause")

    # Change directory to Fit2d directory and execute only if macro was filled
    if counterfiles > 0 and errors == 0:
        print ("")
        print ("Succesfully created fit2d.mac")
        print ("")
        print ("Executing: %s" % str(fit2dversion+' -dim'+str(pixels2)+'x'+str(pixels2)+' -macfit2dint.mac'))
        # Execute the created Fit2d macro with Fit2d
        p = subprocess.Popen(str(fit2dversion+' -dim'+str(pixels2)+'x'+str(pixels2)+' -macfit2dint.mac'))
        p.wait()
    else:
        print ("Did not execute Fit2d because the filenames are too long or")
        print ("there were no files that needed to be integrated.")

    print ("")
    if overwriting == False:
        print ("Note! Overwriting of existing .chi and .asc files is disabled")
        print ("in the parameter file. To change this, edit the parameter file:")

    print ("")
    print ("End of script.")
    # Pause just to give the chance for the user to look at the output before closing the shell.
    if pausing == True:
        os.system("pause")

