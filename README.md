# Safetynet_dkan
Programs to access the Safety Net Almanac data via the DKAN API

So far, we have a Python function get_SNA_data(statid) defined in Safetynet_dkan.py, where statid is the id of a statistic from the 
Safety Net Almanac data. Data is stored at datacatalog.urban.org at https://datacatalog.urban.org/dataset/safety-net-almanac-data.

The function returns a Pandas dataframe, the program test_SNA.py provides an example call. The function get_SNA_data() keeps getting 
data from the DKAN API endpoint until all records for the statid are obtained.

Statistics are defined in the data dictionary for the Safety Net Data https://datacatalog.urban.org/sites/default/files/data-dictionary-files/SNA_Statistics_Dictionary.xlsx .

Have added a new function get_SNA_meta(statid) which gets the metadata from the Statistics Reference resource into a dataframe. So an example test program would do two calls, e.g.:

df_data = sd.get_SNA_data(103)<br>
df_meta = sd.get_SNA_meta(103)

for statid 103