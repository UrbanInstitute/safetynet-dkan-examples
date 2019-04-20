#testing SNA package

import safetynet_dkan as sd

mystatid = 101
myprogram_name = sd.validate_statid(mystatid)
print("Program name is",myprogram_name," for statid ",mystatid)

df_data = sd.get_SNA_data(mystatid)
df_meta = sd.get_SNA_meta(mystatid)





