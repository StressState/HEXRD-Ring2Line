# -*- coding: utf-8 -*-
"""
依据参数生成FIT-2D的mac文件，调用批量处理
"""

import os
import numpy as np
import subprocess
import re
import errno


def automatedcakes(parameterfilename,localdir1,fit2dpath,testflag):
    """

    """
    os.chdir(localdir1)
    fit2dversion = "fit2d_12_077_i686_WXP.exe"
    print ("")
    counter = 0
    parameterfilefound = 0
    """
    遍历数据文件夹,找到对应 mycakeparameters 文件
    """
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file1 in filenames:
            if file1 == parameterfilename and counter == 0:
                paramfile = "%s/%s" % (dirpath,file1)
                print ("Parameter file %s" % paramfile)
                counter = counter + 1
                with open(paramfile,'r') as f:
                    parameters = f.readlines()
                f.close()
                parameterfilefound = 1
    print ("")
    if parameterfilefound == 0:
        print ("Parameter file %s was NOT FOUND anywhere in the directory! Program will exit." % parameterfilename)
        os.system("pause")
        exit(0)

    errorsfound = 0
    # Write the parameters into variables which are easier to identify
    # and more importantly, transform them to the format required by Fit2d
    # 这一部分完全是从mycakeparameters文件读数
    cake_azimuth_start   = float(parameters[1])
    cake_azimuth_end     = float(parameters[3])
    cake_inner_radius    = float(parameters[5])
    cake_outer_radius    = float(parameters[7])
    cake_radial_bins     = int(np.min([cake_outer_radius-cake_inner_radius,float(parameters[9])]))
    cake_azimuthal_bins  = int(parameters[11])
    if parameters[13][:2] == "NO":
        maskfile = 'mask.msk'
        maskyesno = 'NO'
        print ("NO mask.")
    else:
        maskfile = parameters[13][:len(parameters[13])-1]
        maskyesno = 'YES'
        print ("Mask file: %s" % maskfile)
    if parameters[15][:2] == "NO":
        dcfile = 'darkcurrent.bin'
        dcyesno = 'NO'
        print ("NO dark current subtraction.")
    else:
        dcfile = parameters[15][:len(parameters[15])-1]
        dcyesno = 'YES'
        print ("Dark current file: %s" % dcfile)
    beam_center_x       = float(parameters[17])
    beam_center_y       = float(parameters[19])
    wavelength          = float(parameters[21])
    sample_to_detector_distance = float(parameters[23])
    pixel_size_x        = float(parameters[25])
    pixel_size_y        = float(parameters[27])
    detector_tilt_rotation = float(parameters[29])
    detector_tilt_angle = float(parameters[31])
    detector = parameters[33][:len(parameters[33])-1]
    print ("Detector: %s" % detector)
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
        print ("Unknown detector %s!" % detector)
        print ("Cannot proceed with processing.")
#    fit2dpath           = parameters[35][:len(parameters[35])-1]
    scantype            = parameters[37][:len(parameters[37])-1]
    if parameters[39][:2]=='NO':
        overwriting     = 0 # Integrate only files for which integrated files do not existAlways integrate everything
    else: # Assuming it's YES
        overwriting     = 1 # Always integrate everything
    if parameters[41][:3]=='OFF': # OFF
        pausing         = 0 # Don't pause
    else: # Assuming it's ON
        pausing         = 1 # Always pause
    subdirname = "integ_"+str(parameters[43])


    print (" ")
    if pausing == True:
        os.system("pause")
    if errorsfound > 0:
        exit(0)

    # Start writing the fit2d macro file for integrating the 2D data
    f = open(fit2dpath+"/fit2dint.mac",'w')
    print ('%!*'+'\\'+' BEGINNING OF GUI MACRO FILE',file=f)
    print ('%!*'+'\\',file=f)
    print ('%!*'+'\\ This is a comment line',file=f)
    print ('%!*'+'\\',file=f)

    print ('I ACCEPT',file=f)
    print ('POWDER DIFFRACTION (2-D)',file=f)

    # Counting how many file names exceed 80 characters for *.asc files
    errors = 0
    counterfiles = 0
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        if dirpath[len(dirpath)-len(subdirname):] != subdirname:
            for file1 in filenames:
                prefix,postfix = os.path.splitext(file1)
                temp1 = re.findall("[\S\d]*(?=_\d{5}_\d{5})",prefix)
                tempb = re.findall("[\S\d]*(?=_\d{5})",prefix)
                temp1.extend(tempb)
                if len(temp1)>0:
                    subdirprefix = min(filter(None, temp1), key=len)
                else:
                    subdirprefix = ''
                subpath = dirpath+"/"+subdirprefix+'/'+subdirname+"/"
                # As a default overwrite
                overwritingthisone = 1
                # If files exist, then don't overwrite if not allowed
                if os.path.isfile(subpath+prefix+".chi") and cake_azimuthal_bins==1 and overwriting==True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath+prefix+".chi") and cake_azimuthal_bins==1 and overwriting==False:
                    overwritingthisone = 0
                    print ("Did not overwrite: %s" % subpath+prefix+".chi")
                elif os.path.isfile(subpath+prefix+".asc") and cake_azimuthal_bins>1 and overwriting==True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath+prefix+".asc") and cake_azimuthal_bins>1 and overwriting==False:
                    overwritingthisone = 0
                    print ("Did not overwrite: %s" % subpath+prefix+".asc")
                # Compare extensions to find only the 2D files
                # Only accept the ones which are allowed to be overwritten
                if postfix == file_extension and overwritingthisone==True:
                    try: # Try creating the subdirectory for integrated files if it does not exist
                        os.makedirs(subpath)
                    except OSError as exc: # Python >2.5
                        if exc.errno == errno.EEXIST and os.path.isdir(subpath):
                            pass
                    if counterfiles == 0:
                        print ("Preparing a fit2d.mac for files:")
                    counterfiles = counterfiles + 1
                    fullfile1 = dirpath+"/"+file1
                    print (fullfile1)
                    # Write to fit2d.mac
                    print ("INPUT",file=f)
                    print (fullfile1,file=f)
                    # For some reason Pilatus 300k seems to require an extra OK
                    if detector == 'pilatus300k' or detector == 'perkinelmer':
                        print ("O.K.",file=f)
                    # Define common parameters
                    print ("DARK CURRENT",file=f)
                    print (dcyesno,file=f)
                    print ("DC FILE",file=f)
                    print (dcfile,file=f)
                    print ("O.K.",file=f)
                    print ("CAKE",file=f)
                    if counterfiles == 1:
                        print ("NO CHANGE",file=f)
                        print ("           1",file=f)
                        print (" 3.1346145E+03",file=f)
                        print (" 1.7431051E+03",file=f)
                        print ("           1",file=f)
                        print (" 3.0989375E+03",file=f)
                        print (" 1.7074276E+03",file=f)
                        print ("           1",file=f)
                        print (" 1.8680677E+03",file=f)
                        print (" 1.7431051E+03",file=f)
                        print ("           1",file=f)
                        print (" 3.4200337E+03",file=f)
                        print (" 1.7163469E+03",file=f)
                    if maskyesno == 'YES':
                        print ("MASK",file=f)
                        print ("LOAD MASK",file=f)
                        print (maskfile,file=f)
                        print ("EXIT",file=f)
                    print ("INTEGRATE",file=f)
                    print ("X-PIXEL SIZE",file=f)
                    print (pixel_size_x,file=f)
                    print ("Y-PIXEL SIZE",file=f)
                    print (pixel_size_y,file=f)
                    print ("DISTANCE",file=f)
                    print (sample_to_detector_distance,file=f)
                    print ("WAVELENGTH",file=f)
                    print (wavelength,file=f)
                    print ("X-BEAM CENTRE",file=f)
                    print (beam_center_x,file=f)
                    print ("Y-BEAM CENTRE",file=f)
                    print (beam_center_y,file=f)
                    print ("TILT ROTATION",file=f)
                    print (detector_tilt_rotation,file=f)
                    print ("ANGLE OF TILT",file=f)
                    print (detector_tilt_angle,file=f)
                    print ("O.K.",file=f)
                    print ("START AZIMUTH",file=f)
                    print (cake_azimuth_start,file=f)
                    print ("END AZIMUTH",file=f)
                    print (cake_azimuth_end,file=f)
                    print ("INNER RADIUS",file=f)
                    print (cake_inner_radius,file=f)
                    print ("OUTER RADIUS",file=f)
                    print (cake_outer_radius,file=f)
                    print ("SCAN TYPE",file=f)
                    if scantype == 'TTH':
                        print ("2-THETA",file=f)
                    elif scantype == 'Q':
                        print ("Q-SPACE",file=f)
                    elif scantype == 'RADIAL':
                        print ("Q",file=f)
                    else:
                        print ("SCAN TYPE NOT IDENTIFIED! USE TTH or Q.")
                    print ("1 DEGREE AZ",file=f)
                    print ("YES",file=f)
                    if cake_radial_bins == 1:
                        print ("AZIMUTH BINS",file=f)
                        print (int(cake_azimuth_end-cake_azimuth_start),file=f)
                        print ("RADIAL BINS",file=f)
                        print ("1",file=f)
                    else:
                        print ("AZIMUTH BINS",file=f)
                        print (cake_azimuthal_bins,file=f)
                        print ("RADIAL BINS",file=f)
                        print (cake_radial_bins,file=f)
                    print ("POLARISATION",file=f)
                    print ("NO",file=f)
                    print ("CONSERVE INT.",file=f)
                    print ("NO",file=f)
                    print ("GEOMETRY COR.",file=f)
                    print ("YES",file=f)
                    print ("MAX. D-SPACING",file=f)
                    print (1000.00000,file=f)
                    print ("O.K.",file=f)
                    print ("EXIT",file=f)

                    #输出部分改动为同步输出矩阵和图
                    if cake_azimuthal_bins>1 and cake_radial_bins >1:
                        print("OUTPUT", file=f)
                        print ("SPREAD SHEET",file=f)
                        print ("YES",file=f)
                        print (subpath+prefix+".spr",file=f)
                        if len(subpath+prefix+".spr") > 79:
                            print ("WARNING! Path is too long for saving *.spr files")
                            print (subpath+prefix+".spr exceeds limit (80 caharacters). Length %d." % len(subpath+prefix+".spr"))
                            errors = errors + 1
                        print ("YES",file=f)

                       # print("OUTPUT", file=f)
                       # print("TIFF 8 BIT", file=f)
                       # print("NO", file=f)
                       # print(subpath + prefix + ".spr", file=f)
                       # if len(subpath + prefix + ".spr") > 79:
                       #     print("WARNING! Path is too long for saving *.spr files")
                       #     print(subpath + prefix + ".spr exceeds limit (80 caharacters). Length %d." % len(
                       #         subpath + prefix + ".spr"))
                       #     errors = errors + 1
                       # print("O.K.", file=f)
                       # print("O.K.", file=f)

                    else:
                        print("OUTPUT", file=f)
                        print ("CHIPLOT",file=f)
                        print ("FILE NAME",file=f)
                        print (subpath+prefix+".chi",file=f)
                        if cake_radial_bins == 1:
                            print ("OUTPUT ROWS",file=f)
                            print ("NO",file=f)
                            print ("ROW NUMBER",file=f)
                            print (int(cake_azimuth_end-cake_azimuth_start),file=f)
                        else:
                            print ("OUTPUT ROWS",file=f)
                            print ("YES",file=f)
                            print ("ROW NUMBER",file=f)
                            print ("1",file=f)
                        print ("COLUMN NUMBER",file=f)
                        print ("1",file=f)
                        print ("O.K.",file=f)
    # Exit Fit2d at the end
    print ("EXIT",file=f)
    print ("EXIT",file=f)
    print ("YES",file=f)
    print ('%!*'+'\\'+' END OF IO MACRO FILE',file=f)
    f.close() # Close fit2d macro file

    if pausing == True:
        os.system("pause")

    # Change directory to Fit2d directory and execute only if macro was filled
    if counterfiles > 0 and errors == 0:
        print ("")
        print ("Succesfully created fit2d.mac")
        print ("")
        os.chdir(fit2dpath)
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
        print (paramfile)

    print ("")
    print ("End of script.")
    # Pause just to give the chance for the user to look at the output before closing the shell.
    if pausing == True:
        os.system("pause")

def automatedcakeserror(parameterfilename,localdir1,fit2dpath):
    """
    Created on Tue Nov 27 09:28:38 2012

    Script creating automated cake integrationsof ERRORS from all files in the directory and
    in all subdirectories, as defined by files myfit2dparams.txt and mycakeparams.txt

    Use "Run number" to separate runs with different angle ranges
    so that the different runs are saved in different subdirectories.

    Don't use this option for detectors which are not single photon counting
    (e.g. it will not work for mar3450 or PerkinElmer)

    Note:

    When saving more than one azimuthal bin, the data is saved as 2-D ASCII.
    This works only if the path and file name are not too long,
    so use short paths and filenames, in total less than 80 caharacters!

    When using this script on Windows 7, make sure the UAC (User account control)
    is disabled! Otherwise the script cannot start Fit2d.

    @author: Ulla Vainio (ulla.vainio@hzg.de)
    """

    os.chdir(localdir1)
    fit2dversion = "fit2d_12_077_i686_WXP.exe"
    print ("")
    # First look for the parameter file in the directories
    # Note, we take the first file we find!
    counter = 0
    parameterfilefound = 0
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for file1 in filenames:
            if file1 == parameterfilename and counter == 0:
                paramfile = "%s/%s" % (dirpath,file1)
                print ("Parameter file %s" % paramfile)
                counter = counter + 1
                with open(paramfile,'r') as f:
                    parameters = f.readlines()
                f.close()
                parameterfilefound = 1
    print ("")
    if parameterfilefound == 0:
        print ("Parameter file %s was NOT FOUND anywhere in the directory! Program will exit." % parameterfilename)
        os.system("pause")
        exit(0)

    errorsfound = 0
    # Write the parameters into variables which are easier to identify
    # and more importantly, transform them to the format required by Fit2d
    cake_azimuth_start   = float(parameters[1])
    cake_azimuth_end     = float(parameters[3])
    cake_inner_radius    = float(parameters[5])
    cake_outer_radius    = float(parameters[7])
    cake_radial_bins     = int(np.min([cake_outer_radius-cake_inner_radius,float(parameters[9])]))
    cake_azimuthal_bins  = int(parameters[11])
    if parameters[13][:2] == "NO":
        maskfile = 'mask.msk'
        maskyesno = 'NO'
        print ("NO mask.")
    else:
        maskfile = parameters[13][:len(parameters[13])-1]
        maskyesno = 'YES'
        print ("Mask file: %s" % maskfile)
    if parameters[15][:2] == "NO":
        dcfile = 'darkcurrent.bin'
        dcyesno = 'NO'
        print ("NO dark current subtraction.")
    else:
        dcfile = parameters[15][:len(parameters[15])-1]
        dcyesno = 'YES'
        print ("Dark current file: %s" % dcfile)
    beam_center_x       = float(parameters[17])
    beam_center_y       = float(parameters[19])
    wavelength          = float(parameters[21])
    sample_to_detector_distance = float(parameters[23])
    pixel_size_x        = float(parameters[25])
    pixel_size_y        = float(parameters[27])
    detector_tilt_rotation = float(parameters[29])
    detector_tilt_angle = float(parameters[31])
    detector = parameters[33][:len(parameters[33])-1]
    print ("Detector: %s" % detector)
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
        print ("Unknown detector %s!" % detector)
        print ("Cannot proceed with processing.")
#    fit2dpath           = parameters[35][:len(parameters[35])-1]
    scantype            = parameters[37][:len(parameters[37])-1]
    if parameters[39][:2]=='NO':
        overwriting     = 0 # Integrate only files for which integrated files do not existAlways integrate everything
    else: # Assuming it's YES
        overwriting     = 1 # Always integrate everything
    if parameters[41][:3]=='OFF': # OFF
        pausing         = 0 # Don't pause
    else: # Assuming it's ON
        pausing         = 1 # Always pause
    subdirname = "integ_"+str(parameters[43])

    print (" ")
    if pausing == True:
        os.system("pause")
    if errorsfound > 0:
        exit(0)

    # Start writing the fit2d macro file for integrating the 2D data
    f = open(fit2dpath+"/fit2d.mac",'w')
    print ('%!*'+'\\'+' BEGINNING OF GUI MACRO FILE',file=f)
    print ('%!*'+'\\',file=f)
    print ('%!*'+'\\ This is a comment line',file=f)
    print ('%!*'+'\\',file=f)

    print >> f,'I ACCEPT'
    print >> f,'POWDER DIFFRACTION (2-D)'

    # Counting how many file names exceed 80 characters for *.asc files
    errors = 0
    counterfiles = 0
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        if dirpath[len(dirpath)-len(subdirname):] != subdirname:
            for file1 in filenames:
                prefix,postfix = os.path.splitext(file1)
                temp1 = re.findall("[\S\d]*(?=_\d{5}_\d{5})",prefix)
                tempb = re.findall("[\S\d]*(?=_\d{5})",prefix)
                temp1.extend(tempb)
                if len(temp1)>0:
                    subdirprefix = min(filter(None, temp1), key=len)
                else:
                    subdirprefix = ''
                subpath = dirpath+"/"+subdirprefix+'/'+subdirname+"/"
                # As a default overwrite
                overwritingthisone = 1
                # If files exist, then don't overwrite if not allowed
                if os.path.isfile(subpath+prefix+"_err.chi") and cake_azimuthal_bins==1 and overwriting==True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath+prefix+"_err.chi") and cake_azimuthal_bins==1 and overwriting==False:
                    overwritingthisone = 0
                    print ("Did not overwrite: %s" % subpath+prefix+".chi")
                elif os.path.isfile(subpath+prefix+"_err.asc") and cake_azimuthal_bins>1 and overwriting==True:
                    overwritingthisone = 1
                elif os.path.isfile(subpath+prefix+"_err.asc") and cake_azimuthal_bins>1 and overwriting==False:
                    overwritingthisone = 0
                    print ("Did not overwrite: %s" % subpath+prefix+".asc")
                # Compare extensions to find only the 2D files
                # Only accept the ones which are allowed to be overwritten
                if postfix == file_extension and overwritingthisone==True:
                    try: # Try creating the subdirectory for integrated files if it does not exist
                        os.makedirs(subpath)
                    except OSError as exc: # Python >2.5
                        if exc.errno == errno.EEXIST and os.path.isdir(subpath):
                            pass
                    if counterfiles == 0:
                        print ("Preparing a fit2d.mac for files:")
                    counterfiles = counterfiles + 1
                    fullfile1 = dirpath+"/"+file1
                    print (fullfile1)
                    # Write to fit2d.mac
                    print ("INPUT",file=f)
                    print (fullfile1,file=f)
                    # For some reason Pilatus 300k requires an extra OK
                    if detector == 'pilatus300k' or detector == 'perkinelmer':
                        print ("O.K.",file=f)
                    # Define common parameters
                    print ("DARK CURRENT",file=f)
                    print (dcyesno,file=f)
                    print ("DC FILE",file=f)
                    print (dcfile,file=f)
                    print ("O.K.",file=f)
            # The only difference to the automatedcakes() is the SQUARE ROOT
                    print ("EXIT",file=f)
            # A BUG PREVENTS FROM USING THE GRAPHICAL INTERFACE FOR THIS
                    print ("KEYBOARD INTERFACE",file=f)
                    print ("RAISE TO A POWER",file=f)
                    print ("0.5",file=f)
                    print ("EXIT",file=f)
            # Back to integrating
                    print ("POWDER DIFFRACTION (2-D)",file=f)
                    print ("CAKE",file=f)
                    if counterfiles == 1:
                        print ("NO CHANGE",file=f)
                        print ("           1",file=f)
                        print (" 3.1346145E+03",file=f)
                        print (" 1.7431051E+03",file=f)
                        print ("           1",file=f)
                        print (" 3.0989375E+03",file=f)
                        print (" 1.7074276E+03",file=f)
                        print ("           1",file=f)
                        print (" 1.8680677E+03",file=f)
                        print (" 1.7431051E+03",file=f)
                        print ("           1",file=f)
                        print (" 3.4200337E+03",file=f)
                        print (" 1.7163469E+03",file=f)
                    if maskyesno == 'YES':
                        print ("MASK",file=f)
                        print ("LOAD MASK",file=f)
                        print (maskfile,file=f)
                        print ("EXIT",file=f)
                    print ("INTEGRATE",file=f)
                    print ("X-PIXEL SIZE",file=f)
                    print (pixel_size_x,file=f)
                    print ("Y-PIXEL SIZE",file=f)
                    print (pixel_size_y,file=f)
                    print ("DISTANCE",file=f)
                    print (sample_to_detector_distance,file=f)
                    print ("WAVELENGTH",file=f)
                    print (wavelength,file=f)
                    print ("X-BEAM CENTRE",file=f)
                    print (beam_center_x,file=f)
                    print ("Y-BEAM CENTRE",file=f)
                    print (beam_center_y,file=f)
                    print ("TILT ROTATION",file=f)
                    print (detector_tilt_rotation,file=f)
                    print ("ANGLE OF TILT",file=f)
                    print (detector_tilt_angle,file=f)
                    print ("O.K.",file=f)
                    print ("START AZIMUTH",file=f)
                    print (cake_azimuth_start,file=f)
                    print ("END AZIMUTH",file=f)
                    print (cake_azimuth_end,file=f)
                    print ("INNER RADIUS",file=f)
                    print (cake_inner_radius,file=f)
                    print ("OUTER RADIUS",file=f)
                    print (cake_outer_radius,file=f)
                    print ("SCAN TYPE",file=f)
                    if scantype == 'TTH':
                        print ("2-THETA",file=f)
                    elif scantype == 'Q':
                        print ("Q-SPACE",file=f)
                    elif scantype == 'RADIAL':
                        print ("Q",file=f)
                    else:
                        print ("SCAN TYPE NOT IDENTIFIED! USE TTH or Q.")
                    print ("1 DEGREE AZ",file=f)
                    print ("YES",file=f)
                    if cake_radial_bins == 1:
                        print ("AZIMUTH BINS",file=f)
                        print (int(cake_azimuth_end-cake_azimuth_start),file=f)
                        print ("RADIAL BINS",file=f)
                        print ("1",file=f)
                    else:
                        print ("AZIMUTH BINS",file=f)
                        print (cake_azimuthal_bins,file=f)
                        print ("RADIAL BINS",file=f)
                        print (cake_radial_bins,file=f)
                    print ("POLARISATION",file=f)
                    print ("NO",file=f)
                    print ("CONSERVE INT.",file=f)
                    print ("NO",file=f)
                    print ("GEOMETRY COR.",file=f)
                    print ("YES",file=f)
                    print ("MAX. D-SPACING",file=f)
                    print (20.00000,file=f)
                    print ("O.K.",file=f)
                    print ("EXIT",file=f)
                    print ("OUTPUT",file=f)
                    if cake_azimuthal_bins>1 and cake_radial_bins > 1:
                        print ("2-D ASCII",file=f)
                        print ("NO",file=f)
                        print (subpath+prefix+".asc",file=f)
                        if len(subpath+prefix+"_err.asc") > 79:
                            print ("WARNING! Path is too long for saving *.asc files")
                            print (subpath+prefix+".asc exceeds limit (80 caharacters).")
                            errors = errors + 1
                        print ("NO",file=f)
                    else:
                        print ("CHIPLOT",file=f)
                        print ("FILE NAME",file=f)
                        print (subpath+prefix+"_err.chi",file=f)
                        if cake_radial_bins == 1:
                            print ("OUTPUT ROWS",file=f)
                            print ("NO",file=f)
                            print ("ROW NUMBER",file=f)
                            print ("360",file=f)
                        else:
                            print ("OUTPUT ROWS",file=f)
                            print ("YES",file=f)
                            print ("ROW NUMBER",file=f)
                            print ("1",file=f)
                        print ("COLUMN NUMBER",file=f)
                        print ("1",file=f)
                        print ("O.K.",file=f)
    # Exit Fit2d at the end
    print ("EXIT",file=f)
    print ("EXIT",file=f)
    print ("YES",file=f)
    print ('%!*'+'\\'+' END OF IO MACRO FILE',file=f)
    f.close() # Close fit2d macro file

    if pausing == True:
        os.system("pause")

    # Change directory to Fit2d directory and execute only if macro was filled
    if counterfiles > 0 and errors == 0:
        print ("")
        print ("Succesfully created fit2d.mac")
        print ("")
        os.chdir(fit2dpath)
        print ("Executing: %s" % str(fit2dversion+' -dim'+str(pixels2)+'x'+str(pixels2)+' -macfit2d.mac'))
        # Execute the created Fit2d macro with Fit2d
        p = subprocess.Popen(str(fit2dversion+' -dim'+str(pixels2)+'x'+str(pixels2)+' -macfit2d.mac'))
        p.wait()
    else:
        print ("Did not execute Fit2d because the filenames are too long or")
        print ("there were no files that needed to be integrated.")

    print ("")
    if overwriting == False:
        print ("Note! Overwriting of existing .chi and .asc files is disabled")
        print ("in the parameter file. To change this, edit the parameter file:")
        print (paramfile)

    print ("")
    print ("End of script.")
    # Pause just to give the chance for the user to look at the output before closing the shell.
    if pausing == True:
        os.system("pause")
