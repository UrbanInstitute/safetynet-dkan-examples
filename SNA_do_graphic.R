# 
# SNA_do_graphic.R
# Doug Murray 4/19/2019
# updated 9/4/2019
# use safetynet_dkan Python package to get data,
# plot using ggplot
#
# the python program will bring in three dataframes:
#   df_meta     - titles, other metadata for the statid
#   df_data     - the data
#   df_graphic  - parameters for a particular graphic (one record) in the SNA database
#


library(ggplot2)
library(urbnthemes)
library(extrafont)
library(tidyverse)
library(reticulate)
library(gapminder)
library(sys)

# set up for urban style
set_urbn_defaults(style = "print")

# make sure we are in the right working directory
setwd("D:\\python\\SafetyNet\\DKAN")

# run python scripts
source_python("D:/python/SafetyNet/DKAN/safetynet_dkan.py")
source_python("D:/python/SafetyNet/DKAN/test_SNA.py")
# call python function to do a graphic
#do_SNA_graphic(150)


# following the call, we should have the dataframes from the python functions
mytitle     <-  df_graphic["title"]
mysubtitle  <-  df_graphic["subtitle"]
mynotes     <-  paste("Source:",df_graphic["graphic_source"], "\n" , "Note:",df_graphic["graphic_note"])
mylegend_y  <-  df_graphic['yaxis_label']
my_s1_scaler <- as.double(df_graphic['s1_scaler'])
#my_s1_scaler <- 1.0
#
# if national_level = 1, subset to just the national values
#
# if (df_graphic['national_level'] == 1) {
#   mydata <- df_data[ which(df_data$statecode == 99)]
# } else {
#   mydata <- df_data
# }
mydata <- df_data  

# pass the data and labels to ggplot
ggplot(data = mydata, mapping = aes(x = year, y = as.double(data)*my_s1_scaler, group=1)) +
  geom_line() +
  scale_y_continuous(labels = scales::comma) +
  scale_x_discrete() +
  theme(axis.text.x = element_text(angle = 45)) +
  labs(title = mytitle,
       subtitle = mysubtitle,
       caption = mynotes,
       x = "Year",
       y = mylegend_y ) 

# that's all folks...
