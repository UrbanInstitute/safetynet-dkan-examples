# Safetynet_dkan
Programs to access the Safety Net Almanac data via the DKAN API. Data is stored at datacatalog.urban.org at https://datacatalog.urban.org/dataset/safety-net-almanac-data. An example query for the DKAN API for this would be 
https://datacatalog.urban.org/api/action/datastore/search.json?resource_id=aa7c5ea3-ff23-494d-8bbf-a7496a0541bc&limit=5



In test_SNA.py, set mygraphicid to a graphic ID classified as "Series_Line" - this is the only type of graphic we've dealt with yet.

We then call three Python functions to get three dataframes. The call to get_SNA_graphic supplies the statid used by the graphic,
then this gets passed to 
    validate_statid(statid)
    get_SNA_data(statid)
    get_SNA_meta(statid)

once the above calls are made, we should have enough information to do a graphic

The R script SNA_do_grpahic.R calls this using the reticulate package. 
 
This is a work in progress, next steps will include making everything work in R independently so we don't need reticulate. 
Reticulate is great, but sometimes a Pandas dataframe will not load due to the row.names problem. We might also do a version
that works independently in Python.
