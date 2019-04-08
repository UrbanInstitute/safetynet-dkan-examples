# Safetynet_dkan
Programs to access the Safety Net Almanac data via the DKAN API

So far, we have a Python function get_SNA_data(statid) defined in Safetynet_dkan.py, where statid is the id of a statistic from the 
Safety Net Almanac data. Data is stored at datacatalog.urban.org at https://datacatalog.urban.org/dataset/safety-net-almanac-data.

The function returns a Pandas dataframe, the program test_SNA.py provides an example call. The function get_SNA_data() keeps getting 
data from the DKAN API endpoint until all records for the statid are obtained.
