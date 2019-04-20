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

set_urbn_defaults(style = "print")
setwd("D:\\python\\SafetyNet\\DKAN")


use_python("D:\\Users\\dmurray\\AppData\\Local\\Programs\\Python\\Python36")
source_python("D:/python/SafetyNet/DKAN/safetynet_dkan.py")
source_python("D:/python/SafetyNet/DKAN/test_SNA.py")

mytitle    =  df_meta["statistics_label"]

ggplot(data = df_data, mapping = aes(x = year, y = as.integer(data), group=1)) +
  geom_line() +
  scale_y_continuous(labels = scales::comma) +
  labs(title = mytitle,
       caption = "Urban Institute",
       x = "Year",
       y = "Thousands of Households")


