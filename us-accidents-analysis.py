#!/usr/bin/env python
# coding: utf-8

# # US-Accidents: A Countrywide Traffic Accident Dataset analysis
# 
# 
# This dataset is a comprehensive compilation of car accidents that have occurred across all 49 states of the United States. The data collection period spans from February 2016 to March 2023 and was acquired through multiple APIs that continuously feed real-time traffic incident information. The sources of this data include various entities such as the United States and state departments of transportation, law enforcement agencies, traffic cameras, and road network traffic sensors. In total, this dataset comprises approximately 7.7 million records of car accidents.
# 
# ![](https://i.imgur.com/ThC4Pqq.png)
# 
# 
# **What is Exploratory Data Analysis?**
# Exploratory Data Analysis (EDA) serves as a crucial process for delving into data, aiming to uncover patterns, relationships, and insights by employing statistical measures and visualizations. Its primary goal is to foster a deep understanding of the data.
# 
# EDA is a blend of both science and art. On one hand, it relies on a foundation of statistical knowledge, visualization techniques, and data analysis tools like `Numpy`, `Pandas`, `Seaborn`, and more. On the other hand, it requires the skill of posing intriguing questions that steer the investigation and the ability to interpret numerical data and graphical representations to derive meaningful insights.
# 
# For this particular project, I've chosen an US Accidents (2016 - 2023) dataset sourced from [`Kaggle`](https://www.kaggle.com/datasets) to conduct an in-depth analysis. The main objective The objective of performing Exploratory Data Analysis (EDA) on the "US Accidents (2016 - 2023)" dataset is to gain a comprehensive understanding of the data, identify patterns, trends, and insights, and prepare the data for further analysis or modeling. To accomplish this, we'll harness Python libraries such as pandas, `matplotlib`, `seaborn`, `plotly`, and `folium`, which will assist us in conducting an extensive exploratory data analysis of the weather dataset.

# ## How to run the code
# The most straightforward way to execute the code is to click the "Run" button located at the top of this page, and then select "Run on Binder." Alternatively, you can choose to run the code on Google Colab or Kaggle, but keep in mind that you'll need to create an account on Google Colab or Kaggle to use these platforms.
# 
# Certainly, you can run the code using Binder. Binder is a platform that allows you to create interactive, shareable notebooks in a web-based environment. Here's how to run the code on Binder:
# 
# 1. Click the "Run" button at the top of this page.
# 
# 2. Select "Run on Binder."
# 
# 3. The notebook will be launched in a Binder environment, and you can interact with the code.
# 
# 4. You can execute the cells, make changes to the code, and explore the notebook as needed.
# 
# 5. Keep in mind that Binder may take a bit longer to start than Google Colab, but it's a great option for running code without the need to create accounts on external platforms.
# 
# Running the code on Binder is a convenient choice, especially if you prefer a hassle-free and account-free environment for running and experimenting with the code.

# In[1]:


get_ipython().system('pip install jovian --upgrade -q')
import jovian
jovian.set_project('us-accidents-analysis')


# ## Downloading a dataset from an online source
# In this article, I have selected US Accidents (2016 - 2023) data from Kaggle datasets. This dataset contains 7.7 million data about 49 States of US. The data is collected from February 2016 to March 2023. You can find the dataset here [https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
# 
# We'll use the opendatasets library to download the dataset from Kaggle datasets. We have already installed and imported opendatasets library as `od`  in the above section of installing required libraries.

# In[2]:


pip install opendatasets --upgrade --quiet


# In[3]:


import opendatasets as od

download_url = 'https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents'
od.download(download_url)


# In[4]:


data_filename = './us-accidents/US_Accidents_March23.csv'


# In[5]:


import pandas as pd


# In[6]:


df = pd.read_csv(data_filename)


# In[7]:


df


# The dataset contains over 57728394 rows and 46 columns. The data is collected from 2016-02-08 to 2019-08-23. 

# In[8]:


jovian.commit()


# ## Data preparation and cleaning with Pandas
# The quality of data is the most crucial element of any business intelligence strategy. Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.

# Let's view the dataset columns.

# In[9]:


df.columns


# In[10]:


len(df.columns)


# As we can see there are 46 columns presented in the dataset

# In[11]:


df.info()


# In[12]:


df.describe()


# In[13]:


numerics = ['int16','int32','int64','float32','float64']

numeric_df = df.select_dtypes(include = numerics)
print(f"There are {len(numeric_df.columns)} number of numeric columns in the DataFrame.")


# In[14]:


df.isna()


# No data is missing which is great to work with.

# In[15]:


missing_values = df.isna().sum()
missing_values


# The output we are getting is the result of checking for missing values (null or NaN) in each column of your dataset. It appears to be a summary of missing values in each column, represented as the count of missing values for each column. Here's what each part of the output means:
# 
# - The first column lists the column names.
# - The second column shows the count of missing values in each respective column.
# 
# For example, in your dataset:
# 
# - The "ID," "Source," "Severity," "Start_Time," "End_Time," "Start_Lat," "Start_Lng," "Distance(mi)," "Country," and all the columns from "Amenity" to "Turning_Loop" have no missing values, as indicated by the count of 0.
# 
# - The "End_Lat" and "End_Lng" columns have 3,402,762 missing values each.
# 
# - The "Description" column has 5 missing values.
# 
# - The "Street" column has 10,869 missing values.
# 
# - The "City" column has 253 missing values.
# 
# - The "Zipcode" column has 1,915 missing values.
# 
# - And so on for the other columns.
# 
# This information is essential for data cleaning and preprocessing because it helps you understand which columns contain missing data and to what extent. Depending on the analysis you plan to perform, you may need to handle missing values through techniques like imputation or removing rows with missing values.

# Percentage of missing values per column

# In[16]:


missing_percentages = df.isna().sum().sort_values(ascending = False)/len(df)
missing_percentages


# This calculates the percentage of missing values in each column of your dataset and then sorts these percentages in descending order. This is a useful way to assess the extent of missing data for each feature in your dataset. Here's what the output means:
# 
# - For the "End_Lat" and "End_Lng" columns, approximately 44.03% of the data is missing.
# 
# - The "Precipitation(in)" column has around 28.51% missing values.
# 
# - The "Wind_Chill(F)" column contains approximately 25.87% missing data.
# 
# - "Wind_Speed(mph)" has about 7.39% missing values.
# 
# - "Visibility(mi)" has approximately 2.29% missing data.
# 
# - "Wind_Direction" contains around 2.27% missing values.
# 
# - "Humidity(%)" has about 2.25% missing data.
# 
# - "Weather_Condition" contains approximately 2.24% missing values.
# 
# - "Temperature(F)" has about 2.12% missing data.
# 
# - "Pressure(in)" contains around 1.82% missing values.
# 
# And so on for the other columns.

# In[17]:


type(missing_percentages)


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


missing_percentages[missing_percentages != 0].plot(kind='barh')
plt.title('Non-Zero Missing Percentages')
plt.show()


# 
# The bar chart of the percentage of missing values for some feature in the dataset. The y-axis shows the percentage of missing values, and the x-axis shows the feature name.
# 
# The most valuable insight that can be drawn from this chart is that there is a significant amount of missing data for many of the features in the dataset. For example, the feature `"End_lng"` and `"End_lat"` has over 40% missing values, and the feature `"Description "`,` "City"`, `"Zipcode"` almost close to 0% missing values.
# 
# This missing data can pose a number of challenges for machine learning models. For example, if a model is trained on a dataset with a lot of missing data, it may not be able to learn the relationships between the features and the target variable accurately. This can lead to poor performance when the model is deployed to production.
# 
# There are a number of ways to deal with missing data in machine learning datasets. One common approach is to simply remove the rows from the dataset that contain missing values. However, this can reduce the size of the dataset and make it less representative of the real world.
# 
# Another approach is to impute the missing values. This involves replacing the missing values with estimated values. There are a number of different imputation techniques that can be used, depending on the type of data and the specific needs of the project.

# # Exploratory Analysis and Visualization
# 
# Columns we'll analyze 
# 1. City
# 2. Start Time
# 3. Start_Lat and Start_Lng

# In[20]:


df.columns


# ## City

# In[21]:


df.City


# In[22]:


cities = df.City.unique()
len(cities)


# In[23]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[24]:


cities_by_accident[:20]


# In[25]:


cities_by_accident[:20].plot(kind='barh')

plt.title("Top 20 Cities by Accident Count")

plt.show()


# The image shows the top 20 cities in the United States with the highest number of accidents, but we cannot specify what type of accidents or the time period over which the data was collected.

# In[26]:


import seaborn as sns
sns.set_style('darkgrid')


# In[27]:


sns.histplot(cities_by_accident, log_scale=True)

plt.title("Histogram of Cities by Accident (Log Scale)")

plt.show()


# The code `sns.histplot(cities_by_accident, log_scale = True)` will create a histogram of the number of accidents in each city, with the y-axis on a logarithmic scale.

# The [histogram](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html) will show the distribution of the number of accidents in each city. The x-axis will show the number of accidents, and the y-axis will show the number of cities with that number of accidents. The bars in the histogram will be sorted in descending order by the number of accidents.

# In[28]:


cities_by_accident[cities_by_accident==1]


# The list of cities with only 1 accident is a diverse group of cities, ranging in size from very small towns to medium-sized cities. The cities are located in different parts of the United States, and there is no clear pattern to their distribution.

# Here are some possible explanations for why these cities have only 1 accident each:
# 
# - Small population density: Cities with a low population density are likely to have less traffic, which can reduce the risk of accidents.
# - Good road conditions: Cities with good road conditions are less likely to have accidents caused by potholes, uneven surfaces, or other road hazards.
# - Safe driving practices: Residents of cities with only 1 accident each may be more likely to drive safely and obey traffic laws. This could be due to a number of factors, such as public awareness campaigns, law enforcement efforts, or a strong sense of community.
# 
# It is also possible that there is some random chance involved in why these cities have only 1 accident each. For example, a city with a small population density may simply have been lucky enough to avoid accidents during the time period that the data was collected.

# ## Start Time

# In[29]:


df.Start_Time


# In[30]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'])


# In[31]:


sns.distplot(df['Start_Time'].dt.hour, bins=24, kde=False, norm_hist=True)

plt.title("Distribution of Start Time Hours")

plt.show()


# - A high percentage of accidents occur between 6 am to 10 am (probably people in a hurry to get to work)
# - Next highest percentage is between 3 pm to 6 pm.

# In[34]:


sns.distplot(df.Start_Time.dt.dayofweek, bins = 7, kde = False, norm_hist=True)
plt.title("Distribution of Days of the Week for Start Time")
plt.show()


# Is the distribution accidents by hour the same on weekends as on weekdays

# In[35]:


weekends = df.Start_Time[(df.Start_Time.dt.dayofweek == 6) | (df.Start_Time.dt.dayofweek == 5)]
sns.distplot(weekends.dt.hour, bins = 24, kde = False, norm_hist=True)
plt.title("Distribution of Start Time Hours on Weekends")

plt.show()


# In[36]:


weekdays = df.Start_Time[(df.Start_Time.dt.dayofweek >= 0) | (df.Start_Time.dt.dayofweek <= 4) ]
sns.distplot(weekdays.dt.hour, bins = 24, kde = False, norm_hist=True)
plt.title("Distribution of Start Time Hours on Weekdays")

plt.show()


# On Sundays, the peak occurs between 10 am and 3 pm unlike weekdays

# In[37]:


months = sns.distplot(df[(df['Start_Time'] >= '2016-02-01') & (df['Start_Time'] <= '2023-03-31')].Start_Time.dt.month, bins = 12, kde = False, norm_hist=True)
plt.title("Distribution of Months in the Specified Date Range")
plt.show()


# The month-wise trend of accidents shown in the graph shows that the number of accidents is lowest in the summer months (March, May, June and July) and highest in the winter months (November, Decemberand January).
# And the reason behind it could be the weather during winter is snowy which makes it difficult for a person to drive as the road may be cover with thin layer of ice unlike during summers.

# In[38]:


months = sns.distplot(df.Start_Time.dt.year, bins = 12, kde = False, norm_hist=True)
plt.title("Distribution of Years from Start Time")
plt.show()


# In[39]:


df.Start_Time.dt.year


# In[40]:


import matplotlib.pyplot as plt

# Extract the year
df['Year'] = df['Start_Time'].dt.year

# Define the years to plot
years_to_plot = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Create separate histograms for each year
for year in years_to_plot:
    # Filter data for the specific year
    year_data = df[df['Year'] == year]
    
    # Create a new figure and axis for each year
    plt.figure(figsize=(8, 6))
    
    # Create a distogram for the annual accidents using Seaborn
    sns.distplot(year_data['Start_Time'], bins=12, kde=False)
    
    # Set labels and title
    plt.ylabel('Number of Accidents')
    plt.title(f'Distribution of Accidents in {year}')
    
    # Show the plot
    plt.show()


# - In the year of 2016, The numbers of accidents at beginning of the year were the lowest recorded. 
# - In the year of 2017, after July the number of accidents increased with a surprising number and then gradually decreases as the reaming months passes by.
# - In the year of 2020, there's a sudden drop in the number of accidents right after June and riped increase is shown durirng the months of September, October and November.
# - In the year of 2021, Starting of year shows high number of accidents but after 2 months, there's a sudden drop.
# - In the year of 2023, bar for March and April shows highest number of accidents but the data for the months September and October is either missing or accidents never happened. 

# ## Start Latitude  and Start  Longitude 

# In[41]:


df.Start_Lat


# In[42]:


df.Start_Lng


# In[43]:


sns.scatterplot(x = df.Start_Lng, y = df.Start_Lat, sizes = (10,200))
plt.title("Scatterplot of Latitude vs. Longitude")

plt.show()


# In[44]:


sample_df = df.sample(int(0.1 * len(df)))
sns.scatterplot(x = sample_df.Start_Lng, y = sample_df.Start_Lat, size = 0.001)
plt.title("Scatterplot of Latitude vs. Longitude")

plt.show()


# In[41]:


import folium 


# In[42]:


# Create a map object
map = folium.Map()

# Iterate over the Start_Lat and Start_Lng columns for the first 10 rows
for lat, lon in zip(df['Start_Lat'][:10000], df['Start_Lng'][:10000]):
    marker = folium.Marker((lat, lon))
    marker.add_to(map)

# Display the map
map


# This map in pin pointing towards the 1000 area where accidents has too place.

# In[45]:


import folium
from folium.plugins import HeatMap

# Create a Folium map
m = folium.Map()

# Create a HeatMap layer with your data
heat_data = list(zip(df['Start_Lat'][:1000], df['Start_Lng'][:1000]))
HeatMap(heat_data).add_to(m)

# Fit the map view to contain all the points
m.fit_bounds(heat_data)

# Show the map
m


# This heat map is showing data of first 1000 cities . Most of them are from California 

# ## Ask & Answer Questions
# 
# 
# 1. Are there more accidents in warmer or colder areas?
# 2. Which 5 states have the highest number of accidents? How about per city?
# 3. Dose New York show up the data? If yes, why is the count lower if this the most populated city.
# 4. What time of the day are accidents most frequently in? - **ANSWERD**
# 5. Which day of the week have the most accidents?
# 6. Which month have the most accidents?
# 7. What is the trend of accidents year over year(decreasing/increasing)?
# 8. Plot a graph of finding which weather condition is not good for accidents.
# 9. What are the top 10 Description for Accidents.

# ### Q1. Are there more accidents in warmer or colder areas?

# In[44]:


df['Temperature(F)']


# In[45]:


# Categorize temperatures into "cold" or "warm"
df['Temperature Category'] = df['Temperature(F)'].apply(lambda x: 'Cold' if x <= 0 else 'Warm')

# Group data by temperature category and count accidents
category_counts = df['Temperature Category'].value_counts().reset_index()
category_counts.columns = ['Temperature Category', 'Accident Count']

# Create a bar graph
plt.figure(figsize=(8, 6))
plt.bar(category_counts['Temperature Category'], category_counts['Accident Count'], color='skyblue')
plt.xlabel('Temperature Category')
plt.ylabel('Number of Accidents')
plt.title('Accidents in Colder and Warmer Areas')
plt.show()


# As we can see in the graph that the Warmer place has high number of accidentaccidents as compare to the colder place. or we can say that colder place in not even showing any data. Possible reasons could be that all places listed in has only accidents during warm seasons or they may some misinformation is stored

# ### Q2. Which 5 states have the highest number of accidents? How about per city?

# In[46]:


df['State']


# In[47]:


df['City']


# In[48]:


# Top 5 states with the highest number of accidents
top_5_states = df['State'].value_counts().nlargest(5)

print("Top 5 States with the Highest Number of Accidents:")
print(top_5_states)

# Top 5 cities with the highest number of accidents
top_5_cities = df['City'].value_counts().nlargest(5)

print("\nTop 5 Cities with the Highest Number of Accidents:")
print(top_5_cities)


# In[62]:


# Data for the top 5 states
states = ['CA', 'FL', 'TX', 'SC', 'NY']
state_accidents = [1741433, 880192, 582837, 382557, 347960]

# Data for the top 5 cities
cities = ['Miami', 'Houston', 'Los Angeles', 'Charlotte', 'Dallas']
city_accidents = [186917, 169609, 156491, 138652, 130939]

# Create subplots
plt.figure(figsize=(12, 5))

# Plot for the top 5 states
plt.subplot(1, 2, 1)
plt.barh(states, state_accidents, color='skyblue')
plt.xlabel('Number of Accidents')
plt.title('Top 5 States with the Highest Accidents')

# Plot for the top 5 cities
plt.subplot(1, 2, 2)
plt.barh(cities, city_accidents, color='lightcoral')
plt.xlabel('Number of Accidents')
plt.title('Top 5 Cities with the Highest Accidents')

plt.tight_layout()
plt.show()


# **Graph 1** is showing Top 5 States with the highest number of accidents. As we can see that `California(CA)` has scored top position whit 1741433 accidents where as `New York(NY)`
# has scored the least position with 347960 accidents  in the graph.
# 
# **Graph 2** is showing Top 5 States with the highest number of accidents. As we can see that `Miami` has scored top position whit 186917 accidents where as `Dalas` has scored the least position with 130939 accidents  in the graph.

# ### Q3. Dose New York show up the data? If yes, why is the count lower if this the most populated city

# In[45]:


new_york_count = len(df[df['City'] == 'New York'])
if new_york_count > 0:
    print("New York is present in the data.")
    print(f"Count of New York: {new_york_count}")
else:
    print("New York is not present in the data.")


# The count of "New York" in data may be lower than expected because the term "New York" can refer to different things, and not all instances of "New York" necessarily pertain to the city of New York, which is the most populous city in the United States. Here are a few reasons why the count might be lower than expected:
# 
# 1. Ambiguity: "New York" can refer to the state of New York as a whole, which includes not only New York City but also various other cities, towns, and regions. Therefore, when you see the term "New York" in a dataset, it may not always refer specifically to the city of New York.
# 
# 2. Multiple Meanings: The term "New York" can also refer to New York County, which is one of the five boroughs of New York City. Some data sources might differentiate between "New York City" and "New York" to avoid confusion.
# 
# 3. Context: In some cases, the context in which "New York" is mentioned might not be related to population statistics or demographics. It could refer to various aspects of the state or city, such as culture, history, geography, or businesses, without specifically indicating population.
# 
# To get an accurate count of the population of New York City, you would need to look for data explicitly related to demographics or population statistics for the city rather than relying on the raw count of the term "New York" in a dataset, which may include references to the state, county, or other unrelated subjects.

# ### Q4. Which day of the week have the most accidents?

# In[60]:


# Convert 'Start_Time' to datetime and extract day of the week
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Day_of_Week'] = df['Start_Time'].dt.dayofweek

# Count the number of accidents for each day of the week
day_counts = df['Day_of_Week'].value_counts().sort_index()

# Map numeric day of the week to actual day names
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create a Seaborn bar plot
sns.barplot(x=day_names, y=day_counts)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.title('Accidents by Day of the Week')
plt.show()


# As we can see in the graph that on `Friday` US has highest numbers of accidents than other days of week. 

# ### Q5. Which month have the most accidents?

# In[61]:


df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract the month from 'Start_Time'
df['Month'] = df['Start_Time'].dt.month

# Count the number of accidents for each month
month_counts = df['Month'].value_counts().sort_index()

# Create a Seaborn bar plot
sns.barplot(x=month_counts.index, y=month_counts.values)
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.title('Accidents by Month')
plt.show()


# In the graph ploted above we can see that last month of the year which is `DECEMBER ` is showing highest number of accidents as compare to others.

# ###  Q6. What is the trend of accidents year over year(decreasing/increasing)?

# In[63]:


# Convert 'Start_Time' to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract the year from the 'Start_Time' column
df['Year'] = df['Start_Time'].dt.year

# Group the data by year and count the number of accidents for each year
yearly_accidents = df['Year'].value_counts().sort_index()

# Create a line plot to visualize the trend
plt.figure(figsize=(12, 6))
plt.plot(yearly_accidents.index, yearly_accidents.values, marker='o', linestyle='-')
plt.title('Trend of Accidents Year Over Year')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.grid(True)

# Show the plot
plt.show()


# From year **2016 to 2022** the number of accidents were increasing but right after that it show a sudden decrease in the trend.

# ### Q7. Plot a graph of finding which weather condition is not good for accidents 

# In[83]:


# Calculate the average number of accidents for each weather condition
weather_avg_accidents = df['Weather_Condition'].value_counts()

# Create a bar plot
plt.figure(figsize=(20, 6))
weather_avg_accidents.plot(kind='bar', color='skyblue')
plt.title("Average Accidents by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Average Number of Accidents")
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Show the plot
plt.show()


# This graph is showing that **FAIR** weather condition has the highest number of accidents.

# ### Q8. What are the top 10 Description for Accidents ? 

# In[50]:


# Assuming df is your DataFrame
top10_descriptions = df['Description'].value_counts()

print(top10_descriptions.head(10))


# From the provided top 10 descriptions of accidents, we can gain several valuable insights about the types of accidents and incidents that frequently occur in the dataset:
# 
# 1. **Common Accident Types:** The descriptions provide insights into common types of accidents and incidents. For example, descriptions like "A crash has occurred" and "Accident" suggest general accident types.
# 
# 2. **Severity:** The descriptions vary in terms of severity, from accidents with minimal delays to those that may require more caution. Understanding the distribution of severity can help prioritize responses.
# 
# 3. **Location Information:** Some descriptions include location details like "At I-15 - Accident" or "At I-5 - Accident," which can provide insights into where accidents frequently occur, potentially aiding in traffic management and safety measures.
# 
# 4. **Confirmation Status:** The descriptions indicate whether a crash or incident is confirmed or unconfirmed. Understanding the confirmation status can be crucial for incident response and resource allocation.
# 
# 5. **Worker Safety:** Descriptions like "Prepare to slow or move over for worker safety" highlight the importance of worker safety during accidents and incidents.
# 
# 6. **Hazardous Conditions:** Descriptions that mention hazards, disabled vehicles, or creating a hazard provide insights into situations that may pose risks to drivers and road safety.
# 
# These insights can help traffic management, emergency response, and road safety organizations make informed decisions, allocate resources efficiently, and take appropriate actions in response to accidents and incidents. Understanding the patterns and common descriptions in accident data is essential for improving road safety and traffic management.

# ## Summary
# The Exploratory Data Analysis on India's Weather dataset is completed.
# Here are the outline's that we have followed:
# 1. Downloaded the dataset from Kaggle
# 2. Data preparation and cleaning was done with Pandas
# 3. Exploratory analysis and visualization was done along with asking and answering interesting questions.
# 
# The following are the observations I have noticed during Exploratory Analysis:
# 
# 1. There is Data Available for NYC.
# 2. FAIR weather condition has the highest number of accidents.
# 3. Warm places has the accident and No data for cold places.
# 4. FAIR weather condition has the highest number of accidents.
# 5. DECEMBER  is showing highest number of accidents as compare to others.
# 6.  On Friday US has highest numbers of accidents than other days of week.
# 7. Top 5 States with the Highest Number of Accidents:
#    - CA     (1741433)
#    - FL     (880192)
#    - TX     (582837)
#    - SC     (382557)
#    - NY     (347960)
# 8. Top 5 Cities with the Highest Number of Accidents:
#    - Miami          (186917)
#    - Houston        (169609)
#    - Los Angeles    (156491)
#    - Charlotte      (138652)
#    - Dallas         (130939)

# ## Conclusion
# 
# 1. **High Accident Frequency in Urban Areas:** The top 5 cities with the highest number of accidents are all major urban areas. Miami, Houston, Los Angeles, Charlotte, and Dallas are densely populated regions with extensive road networks. This suggests that urban areas tend to have a higher frequency of accidents, which could be attributed to increased traffic, congestion, and various road conditions.
# 
# 2. **Geographic Variation:** The distribution of accidents is not uniform across different cities. Some cities have significantly higher accident numbers than others. This indicates that the factors contributing to accidents, such as weather conditions, road infrastructure, and driver behavior, can vary widely from one location to another.
# 
# 3. **Safety Initiatives:** These findings can be valuable for local authorities and transportation departments. They may use this data to prioritize safety initiatives, such as improving road infrastructure, enhancing traffic management, and promoting safe driving practices in cities with high accident rates.
# 
# 4. **Resource Allocation:** The cities listed may need to allocate additional resources to address road safety and reduce the number of accidents. This could include investments in traffic monitoring, law enforcement, and public awareness campaigns to mitigate accidents.
# 
# 5. **Data-Driven Decision-Making:** These statistics underscore the importance of data-driven decision-making in addressing traffic safety issues. By analyzing accident data, authorities can make informed choices to enhance safety and reduce accidents in areas with a high incidence of accidents.
# 
# In summary, the data indicates that urban areas, particularly the listed cities, face challenges in terms of road safety, and addressing these challenges may require targeted efforts and initiatives.

# ## Future Work
# Future work related to the analysis of the "US Accidents (2016 - 2023)" dataset could include a variety of tasks and research areas. Here are some potential directions for future work:
# 
# 1. **Predictive Modeling:** Building machine learning models to predict accident severity, location, or other relevant factors. This can aid in early accident detection and preventive measures.
# 
# 2. **Spatial Analysis:** Explore spatial patterns of accidents using geographic information systems (GIS) to identify accident-prone zones, helping authorities implement safety measures more effectively.
# 
# 3. **Temporal Trends:** Analyze temporal patterns and trends in accidents to understand how accidents vary by time of day, day of the week, or season. This can assist in planning and resource allocation.
# 
# 4. **Impact of Weather Conditions:** Investigate how weather conditions affect accident rates and severity. This could lead to more effective weather-related traffic management and road maintenance.
# 
# 5. **Road Infrastructure Analysis:** Assess the impact of road infrastructure, such as the presence of traffic signals, roundabouts, or road types, on accident occurrence and severity. This can inform decisions about road design and maintenance.
# 
# 6. **Driver Behavior Analysis:** Study the role of driver behavior, such as speeding, distracted driving, and impaired driving, in accidents. This information can guide campaigns to promote safe driving habits.
# 
# 7. **Machine Vision for Accident Detection:** Implement computer vision and image analysis techniques to develop automated accident detection systems using traffic camera data.
# 
# 8. **Emergency Response Optimization:** Optimize emergency response systems by analyzing response times and accident locations to improve the efficiency of emergency services.
# 
# 9. **Public Safety Awareness:** Develop public safety awareness campaigns based on the findings, targeting specific regions or demographics with higher accident rates.
# 
# 10. **Policy Recommendations:** Offer data-driven policy recommendations to local, state, and national authorities to enhance road safety and reduce accidents.
# 
# 11. **Data Integration:** Combine the accident dataset with additional data sources, such as hospital records, vehicle data, or socioeconomic data, to gain a more comprehensive understanding of accident causality and outcomes.
# 
# 12. **Real-Time Accident Monitoring:** Develop a real-time accident monitoring and reporting system that integrates with traffic cameras and sensors for quicker responses to accidents.
# 
# 13. **Ethical and Privacy Considerations:** Explore the ethical implications and privacy concerns related to collecting and sharing accident data, especially in the context of emerging technologies like connected vehicles and smart cities.
# 
# These future work areas can help further the understanding of traffic accidents and contribute to improving road safety and emergency response systems. Additionally, advancements in data analytics and technology can play a significant role in achieving these objectives.

# ## References
# 
# * [User guide for Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
# * [List of properties you can set using update_layout](https://plotly.com/python/reference/layout/)
# * [Seaborn gallery](https://seaborn.pydata.org/examples/index.html)
# * [Matplotlib gallery](https://matplotlib.org/3.1.1/gallery/index.html)
# * [Matplotlib tutorial](https://github.com/rougier/matplotlib-tutorial)
# * [opendatasets Python library](https://github.com/JovianML/opendatasets)
# * [Folium Tutorial](https://python-(https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
# * https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

# In[50]:


jovian.commit()

