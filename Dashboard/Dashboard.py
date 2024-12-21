import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('./data/air_quality_df.csv')

def main():

  st.title('Air Quality Analysis Gucheng Station')
  
  with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Location_of_Gucheng_within_Yunnan_%28China%29.png")
    
  
  # Scatter Plots - PM2.5 vs RAIN, SO2 vs RAIN, CO vs RAIN
  st.header('Relationships between Pollutants and Rainfall')
  col1, col2, col3 = st.columns(3)

  with col1:
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data, x='PM2.5', y='RAIN', ax=ax1)
    ax1.set_title('PM2.5 vs RAIN')
    st.pyplot(fig1)

  with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data, x='SO2', y='RAIN', ax=ax2)
    ax2.set_title('SO2 vs RAIN')
    st.pyplot(fig2)

  with col3:
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data, x='CO', y='RAIN', ax=ax3)
    ax3.set_title('CO vs RAIN')
    st.pyplot(fig3)

  # Heatmap - Correlation Matrix
  st.header('Correlation Matrix')
  correlation_matrix = data[['PM2.5', 'SO2', 'CO', 'RAIN']].corr()
  fig4, ax4 = plt.subplots(figsize=(8, 6))
  sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax4)
  ax4.set_title('Correlation Matrix')
  st.pyplot(fig4)

  # Calculate monthly average rainfall
  monthly_rain = data.groupby('month')['RAIN'].mean()

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
- There is a very significant peak in rainfall in the 7th month. This indicates that there is a very confusing rainy season that month.
""")
  

if __name__ == '__main__':
  main()