#testing SNA package

import safetynet_dkan as sd

mystatid = 101
print ("\nCalling validate_statid...\n")
myprogram_name = sd.validate_statid(mystatid)
print("Program name is",myprogram_name," for statid ",mystatid)

print ("\nCalling get_SNA_data...\n")
df_data = sd.get_SNA_data(mystatid)
print ("\nCalling get_SNA_meta...\n")
df_meta = sd.get_SNA_meta(mystatid)
print("\nDone")





