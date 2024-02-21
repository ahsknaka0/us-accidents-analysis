# US-Accidents: A Countrywide Traffic Accident Dataset analysis


This dataset is a comprehensive compilation of car accidents that have occurred across all 49 states of the United States. The data collection period spans from February 2016 to March 2023 and was acquired through multiple APIs that continuously feed real-time traffic incident information. The sources of this data include various entities such as the United States and state departments of transportation, law enforcement agencies, traffic cameras, and road network traffic sensors. In total, this dataset comprises approximately 7.7 million records of car accidents.

![](https://i.imgur.com/ThC4Pqq.png)


**What is Exploratory Data Analysis?**
Exploratory Data Analysis (EDA) serves as a crucial process for delving into data, aiming to uncover patterns, relationships, and insights by employing statistical measures and visualizations. Its primary goal is to foster a deep understanding of the data.

EDA is a blend of both science and art. On one hand, it relies on a foundation of statistical knowledge, visualization techniques, and data analysis tools like `Numpy`, `Pandas`, `Seaborn`, and more. On the other hand, it requires the skill of posing intriguing questions that steer the investigation and the ability to interpret numerical data and graphical representations to derive meaningful insights.

For this particular project, I've chosen an US Accidents (2016 - 2023) dataset sourced from [`Kaggle`](https://www.kaggle.com/datasets) to conduct an in-depth analysis. The main objective The objective of performing Exploratory Data Analysis (EDA) on the "US Accidents (2016 - 2023)" dataset is to gain a comprehensive understanding of the data, identify patterns, trends, and insights, and prepare the data for further analysis or modeling. To accomplish this, we'll harness Python libraries such as pandas, `matplotlib`, `seaborn`, `plotly`, and `folium`, which will assist us in conducting an extensive exploratory data analysis of the weather dataset.

## How to run the code
The most straightforward way to execute the code is to click the "Run" button located at the top of this page, and then select "Run on Binder." Alternatively, you can choose to run the code on Google Colab or Kaggle, but keep in mind that you'll need to create an account on Google Colab or Kaggle to use these platforms.

Certainly, you can run the code using Binder. Binder is a platform that allows you to create interactive, shareable notebooks in a web-based environment. Here's how to run the code on Binder:

1. Click the "Run" button at the top of this page.

2. Select "Run on Binder."

3. The notebook will be launched in a Binder environment, and you can interact with the code.

4. You can execute the cells, make changes to the code, and explore the notebook as needed.

5. Keep in mind that Binder may take a bit longer to start than Google Colab, but it's a great option for running code without the need to create accounts on external platforms.

Running the code on Binder is a convenient choice, especially if you prefer a hassle-free and account-free environment for running and experimenting with the code.


## Language used
Python

## Libraries used
- [`Seaborn`](https://seaborn.pydata.org/)
- [`Pandas`](https://pandas.pydata.org/)
- [`opendatasets`](https://pypi.org/project/opendatasets/)
- [`Matplotlib`](https://matplotlib.org/)
- [`Folium`](https://pypi.org/project/folium/)

# How to Download Data set using `opendatasets`

pip install opendatasets --upgrade --quiet
Note: you may need to restart the kernel to use updated packages.
import opendatasets as od

download_url = 'https:.....(link here)'
od.download(download_url)



