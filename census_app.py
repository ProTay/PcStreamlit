

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('adult.csv',header = None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.title('Census Data Visualisation App')
st.dataframe(census_df)
st.title('Census Data Visualisation App')
if st.sidebar.checkbox('Display Raw Data'):
	plot_list = st.sidebar.multiselect('Select Plot Types:',('Pie Chart', 'Box Chart', 'Count Plot'))
if 'Pie Chart' in plot_list:
	income_data = census_df['income'].value_counts()
	gender_data = census_df['gender'].value_counts()
	pie_data = [income_data, gender_data]
	for i in pie_data:
		st.subheader('Pie Chart for Income Group and Gender')
		plt.figure(figsize = (14,6))
		plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%', startangle = 30, explode = np.linspace(0.06, .16, 6))
		st.pyplot()
if 'Box Chart' in plot_list:
	income_bdata = 'income'
	gender_bdata = 'gender'
	box_data = [income_bdata, gender_bdata]
	for i in box_data:
		plt.figure(figsize = (12,2))
		st.subheader(f'Box Plot for {columns}')
		sns.boxplot(census_df[i])
		st.pyplot()
if 'Count Plot' in plot_list:
	st.subheader('Count Plot for workclss')
	plt.figure(figsize = (12,6))
	sns.countplot(x = 'workclass', data = census_df)
	st.pyplot()
