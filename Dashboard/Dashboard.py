import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
sns.set(style='dark')

# Load dataset
data = pd.read_csv('air_quality_df.csv')

st.title('Air Quality Analysis Gucheng Station')
st.write('This analysis aims to investigate the relationship between air quality and rainfall in Gucheng Station. We will examine historical data for pollutants like CO, SO2, and PM2.5, along with rainfall measurements.')

st.header('Interactive Plot of Pollutant vs Rain')

# Create a calendar sidebar
with st.sidebar:
  # Add Name
  st.title("Muhammad Dicry S.") 
  # Add logo
  st.image("Logo.png")
  # Add tittle
  st.title("Pollutan vs Rain")
  year = st.sidebar.selectbox("Year", data['year'].unique())
  month = st.sidebar.selectbox("Month", data['month'].unique())
  day = st.sidebar.number_input("Start Day", min_value=1, max_value=calendar.monthrange(year, month)[1], step=1)

  # Filter data based on selected date range
  filtered_data = data[(data['year'] == year) & (data['month'] == month) & (data['day'] == day)]

# Create the plot
fig, ax = plt.subplots()
ax.plot(filtered_data['hour'], filtered_data['PM2.5'], label='PM2.5')
ax.plot(filtered_data['hour'], filtered_data['SO2'], label='SO2')
ax.plot(filtered_data['hour'], filtered_data['CO'], label='CO')
ax.set_xlabel("Hour")
ax.set_ylabel("Polutant Level")
ax.set_title("Polutant Levels vs Rain")
ax.legend()

# Add rain information to the plot
rain_events = []
for index, row in filtered_data.iterrows():
    if row['RAIN'] > 0:
        ax.axvline(x=row['hour'], color='r', linestyle='--')
        rain_events.append(row['hour'])

# Add legend for rain events
if rain_events:
    ax.legend(['PM2.5', 'SO2', 'CO', 'Rain Event']) 

# Display the plot
st.pyplot(fig)

# Heatmap - Correlation Matrix
st.header('Correlation Matrix')
correlation_matrix = data[['PM2.5', 'SO2', 'CO', 'RAIN']].corr()
fig1, ax1 = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax1)
ax1.set_title('Correlation Matrix')
st.pyplot(fig1)

years = data['year'].unique()

# Sidebar for user input
st.sidebar.title("Trend of Average Rainfall")
start_year = st.sidebar.selectbox("Start Year", options=years)
end_year = st.sidebar.selectbox("End Year", options=years, index=years.tolist().index(start_year))

# Filter data based on selected year range
filtered_data = data[(data['year'] >= start_year) & (data['year'] <= end_year)]

# Calculate monthly average rainfall
monthly_rain = filtered_data.groupby('month')['RAIN'].mean()

# Line plot - Trend of Rainfall over Months
st.header('Trend of Average Rainfall')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=monthly_rain.index, y=monthly_rain.values, ax=ax)
ax.set_title('Trend of Rainfall over Months')
ax.set_xlabel('Month')
ax.set_ylabel('Average Rainfall')
st.pyplot(fig)

#Conclusion
st.subheader('Conclusion')
st.write("""
- There is a negative relationship between PM2.5, SO2, and CO on rainfall in Gucheng district, which means that the higher the rainfall, the lower the pollutants and vice versa.
- The peak of average rainfall often occurs in month 7, which indicates that it is the rainy season.
""")
