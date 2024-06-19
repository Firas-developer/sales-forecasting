import pandas as pd					 # to extract data from dataset(.csv file)
import csv							 #used to read and write to csv files
import numpy as np					 #used to convert input into numpy arrays to be fed to the model
import matplotlib.pyplot as plt		 #to plot/visualize sales data and sales forecasting
import tensorflow as tf				 # acts as the framework upon which this model is built
from tensorflow import keras		 #defines layers and functions in the model

#here the csv file has been copied into three lists to allow better availability
list_row,date,traffic = get_data('/home/abh/Documents/Python/Untitled Folder/Sales_dataset')
