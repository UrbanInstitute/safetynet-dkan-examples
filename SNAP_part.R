# 
# SNAP_part.R
# Doug Murray 4/19/2019
# use safetynet_dkan Python package to get data
# plot using ggplot
#
# the python program will bring in two dataframes:
#   df_meta - titles, other metadata
#   df_data - the data
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

# call python programs - note that we make sure we know which python we're using
use_python("D:\\Users\\dmurray\\AppData\\Local\\Programs\\Python\\Python36")
source_python("D:/python/SafetyNet/DKAN/safetynet_dkan.py")
source_python("D:/python/SafetyNet/DKAN/test_SNA.py")


# following the call, we should have the two dataframes from thy python functions
mytitle    =  df_meta["statistics_label"]
mynotes    =  df_meta["notes"]

# pass the data and labels to ggplot
q <- ggplot(data = df_data, mapping = aes(x = year, y = as.integer(data), group=1)) +
  geom_line() +
  scale_y_continuous(labels = scales::comma) +
  scale_x_discrete() +
  labs(title = mytitle,
       caption = mynotes,
       x = "Year",
       y = "Thousands of Households")

q + theme(axis.text.x = element_text(angle = 90, hjust = 1))

# that's all folks...
