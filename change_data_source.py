# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 19:20:26 2018

@author: Alexander

The purpose of this script is to:
    1) Search through MXDs in a directory
    2) In each MXD, search for the existence of a specific layer name
    3) If that specific layer exists, check the data source
    4) Change the data souce if the data source does not match a given variable

"""

import arcpy
import os
import time
#
# this is the directory for MXDs to be examined
#
my_dir     = r"C:\Users\Alexander\Desktop\School\Projects\Change_Data_Source\MXD"
#
# this is the layer you are looking for
#
lyr_sought = "counties"
#
# this is the ***full filepath*** desired
#
new_source = r"C:\Users\Alexander\Desktop\School\Projects\Change_Data_Source\Data\New_Database.gdb\counties"
#
#
#
new_gdb    = r"C:\Users\Alexander\Desktop\School\Projects\Change_Data_Source\Data\New_Database.gdb"
#
#
#
def change_data_source(input_dir, input_lyr, input_data_source, input_gdb):
    #
    start_time   = time.time()
    #
    list_of_mxds = [os.path.join(my_dir, f) for f in os.listdir(input_dir) if f[-3:] == "mxd" ]
    #
    if len(list_of_mxds) > 0:
        #
        for m in list_of_mxds:
            #
            print m
            #
            mxd  = arcpy.mapping.MapDocument(m)
            #
            try:
                #
                for lyr in arcpy.mapping.ListLayers(mxd, input_lyr):
                    #
                    if lyr.supports("DATASOURCE"):
                        #
                        data_source = str(lyr.dataSource)
                        #
                        if data_source == input_data_source:
                            #
                            print "all good in the hood"
                            #
                            print lyr.dataSource
                            #
                        else:
                            #
                            print lyr.dataSource
                            #
                            lyr.replaceDataSource(new_gdb, "FILEGDB_WORKSPACE", input_lyr)
                            #
                            print "replaced data source"
                            #
                            print lyr.dataSource
                            #
                            mxd.save()
                            #
                        #
                    #
                    else:
                        #
                        print "lyr does not support dataSource"
                        #
                    #
                #
            except Exception as e:
                #
                print e
                #
            #
            print "\n"
            #
        #
    #
    else:
        #
        print "there are no MXDs in this directory"
        #
    #
    end_time     = round(time.time() - start_time, 5)
    #
    print "Seconds elapsed: {0}".format(end_time)
#
#
#
change_data_source(my_dir, lyr_sought, new_source, new_gdb)
#