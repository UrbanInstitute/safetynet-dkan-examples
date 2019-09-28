# Safetynet_dkan
Programs to access the Safety Net Almanac data via the DKAN API. Data is stored at datacatalog.urban.org at https://datacatalog.urban.org/dataset/safety-net-almanac-data. An example query for the DKAN API for this would be 
https://datacatalog.urban.org/api/action/datastore/search.json?resource_id=aa7c5ea3-ff23-494d-8bbf-a7496a0541bc&limit=5

For R: 
 See dkan_r_experiments.html and .rmd -- this can do everything one needs to do, in R. This uses the dkanTools package https://rdrr.io/github/daltare/dkanTools/ .
 
 R markdown for the example is available here: https://urbaninstitute.github.io/safetynet-dkan-examples/dkan_r_experiments.html

For Python:
 In test_SNA.py, set mygraphicid to a graphic ID classified as "Series_Line" - this is the only type of graphic we've dealt with yet.

 We then call three Python functions to get three dataframes. The call to get_SNA_graphic supplies the statid used by the graphic,
 then this gets passed to validate_statid(statid), get_SNA_data(statid), and get_SNA_meta(statid) .

 Once these calls are made, we should have enough information to do a graphic. 

 The R script SNA_do_grpahic.R calls this using the reticulate package, and then creates a graphic using ggplot2. However, most likely the best idea is to use the functions in dkan_r_experiments.
 


This is a work in progress, will post refinements as improvements are made, for example to automate getting current resource ids.
