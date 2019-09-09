#
# D.Murray 9/9/2019
#
# testing SNA package
# set mygraphicid to a graphic ID classified as "Series_Line"
# this is the only type of graphic we've dealt with yet
#
# we call three Python functions to get three dataframes
# the call to get_SNA_graphic supplies the statid used by the graphic,
# then this gets passed to 
#    validate_statid(statid),
#    get_SNA_data(statid)
#    get_SNA_meta(statid)
#
# once the above calls are made, we should have enough information to do a graphic
#
# The R script SNA_do_grpahic.R calls this using the reticulate package
#
#
import os
os.chdir("D://python//SafetyNet//DKAN/")

import safetynet_dkan as sd
import pandas as pd

pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('precision', 5)


mygraphicid = 67

# get graph data for a graphicid
print ("\nCalling get_SNA_graphic...\n")
df_graphic = sd.get_SNA_graphic(mygraphicid)


mystatid = int(df_graphic['s1'][0])

print(mystatid)


# validate this statid
print ("\nCalling validate_statid...\n")
myprogram_name = sd.validate_statid(mystatid)
#print("Program name is",myprogram_name," for statid ",mystatid)

# get data for this statid
print ("\nCalling get_SNA_data...\n")
df_data = sd.get_SNA_data(mystatid)
#print(tabulate(df_data, showindex=False, headers=['data','dataset',' ', 'SNAP_ID', 'StateAbbrev', 'Statecode', 'Statename',
#       'statid', 'statistic','year'] ,floatfmt=".0f",tablefmt="presto"))

# get meta data for this statid
print ("\nCalling get_SNA_meta...\n")
df_meta = sd.get_SNA_meta(mystatid)
#print(tabulate(df_meta, showindex=False,  floatfmt=".0f",tablefmt="presto",headers=['scaler','scaler_label','isindex','isnum','isratio', 'isshare', 'jsvarname', 'ndecimals', 'notes','program_id', 'select_label','sourcenotes','sourceurl','statid','statistic','statistics_label','statistics_label_short']))

#
# Note! although we got the metadata for the statistics id, (mystatid) we want to use the metadata from the graphics record (mygraphicid)
#
# Legend
my_s1_legend = df_graphic['s1_legend'][0]
print(my_s1_legend)
#


print("\nDone")





