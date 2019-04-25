#testing SNA package
import os
os.chdir("D://python//SafetyNet//DKAN/")

import safetynet_dkan as sd
from tabulate import tabulate

mystatid = 102

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
#print(tabulate(df_meta, showindex=False,  floatfmt=".0f",tablefmt="presto",headers=['isindex','isnum','isratio', 'isshare', 'jsvarname', 'ndecimals', 'notes','program_id', 'select_label','sourcenotes','sourceurl','statid','statistic','statistics_label','statistics_label_short']))

print("\nDone")





