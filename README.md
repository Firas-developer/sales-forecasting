# Sales Forecast Prediction – Python
Forecast prediction is predicting a future value using past values and many other factors.

# Sales forecasting
It is determining present-day or future sales using data like past sales, seasonality, festivities, economic conditions, etc.

So, this model will predict sales on a certain day after being provided with a certain set of inputs.

In this model 8 parameters were used as input:
past seven day sales
day of the week
date – the date was transformed into 3 different inputs
season
Festival or not
sales on the same day in the previous year

How does it work?
First, all inputs are preprocessed to be understandable by the machine. This is a linear regression model based on supervised learning, so the output will be provided along with the input. Then inputs are then fed to the model along with desired output. The model will plot(learn) a relation(function) between the input and output. This function or relation is then used to predict the output for a specific set of inputs. In this case, input parameters like date and previous sales are labeled as input, and the amount of sales is marked as output. The model will predict a number between 0 and 1 as a sigmoid function is used in the last layer. This output can be multiplied by a specific number(in this case, maximum sales), this will be our corresponding sales amount for a certain day. This output is then provided as input to calculate sales data for the next day. This cycle of steps will be continued until a certain date arrives.

# Required packages and Installation
numpy
pandas
keras
tensorflow
csv
matplotlib.pyplot

The use of external libraries has been kept to a minimum to provide a simpler interface.
As you can see, the sales data seems to be following a similar kind of pattern for each year and the peak sales value seems to be increasing with time over the 5-year time frame.

In this 5-year time frame, the first 4 years will be used to train the model and the last year will be used as a test set. 

Now, a few helper functions were used for processing the dataset and creating inputs of the required shape and size. 
They are as follows:
get_data – used to load the data set using a path to its location.
date_to_day – provides a day to each day. For example — 2/2/16 is Saturday and 9/5/15 is Monday.
date_to_enc – Encodes data into one-hot vectors, this provides a better learning opportunity for the model.

Preprocessing:
Initially, the data set had only two columns: date and traffic(sales).

After the addition of different columns and processing/normalization of values, the data contained all these values.

Date
Traffic
Holiday or not
Day
All these parameters have to be converted into a form that the machine can understand, which will be done using this function below.

We will now process some other inputs that were remaining, the reason behind using all these parameters is to increase the efficiency of the model, you can experiment with removing or adding some inputs.

Sales data of the past seven days were passed as an input to create a trend in sales data, this will the predicted value will not be completely random similarly, sales data of the same day in the previous year was also provided.

The following function(other_inputs) processes three inputs:

sales data of past seven days
sales data on the same date in the previous year
seasonality – seasonality was added to mark trends like summer sales, etc

# Defining the Model
Eight separate inputs are processed and concatenated into a single layer and passed to the model.

The finalized inputs are as follows:
Date
Month
Year
Day
Previous seven days sales
sales in the previous year
Season
Holiday or not

Here in most layers, I have used 5 units as the output shape, you can further experiment with it to increase the efficiency of the model. 
