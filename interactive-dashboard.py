# importing the libraries
import streamlit as st 
import plotly.express as px 
import pandas as pd 

st.title('Dynamic Insights: Interactive Plots in Streamlit!')
st.header('Project by: Aarish Asif Khan')
st.header('Held on: 8th January 2024')

st.markdown('Here is the extensive Gapminder dataset we obtained using Plotly in Python, offering a wealth of diverse information for thorough analysis and insightful exploration.')
st.markdown(' ### **Gapminder Dataset**')
st.markdown('Gapminder dataset refers to a collection of data provided by Gapminder, an organization that focuses on global development and social progress.')
st.markdown('This dataset typically includes a wide range of information related to various countries, covering indicators such as population, income, health, and education.')

# importing the dataset
df = px.data.gapminder()
st.write(df)
# st.write(df.head())
st.markdown(' ### **List of columns from our Dataset**')
st.write(df.columns)


# summary stats/statistics 
st.markdown(' ### **Summary Statistics of our Dataset**')
st.write(df.describe())


# data management on gapminder dataset
st.markdown(' ### **Effective Data Management**')
year_options = df['year'].unique().tolist()

st.markdown('Feel free to make a selection by picking any specific year of your preference!')

year = st.selectbox(' ###### - **For which year do you intend to create a plot?**', year_options, 0)
df = df[df['year']== year]

# plotting
st.markdown(' ###### - **Scatter plot on the basis of gdpPercap and lifeExp**')
st.markdown('The plot will adapt dynamically as we choose different values above, changing from year to year.')

fig = px.scatter(df, x= 'gdpPercap', y= 'lifeExp', size= 'pop', color= 'country', hover_name= 'country', 
                     log_x= True, size_max= 55, range_x=[100,100000], range_y=[20,90])
st.write(fig)

# plotting continent wise
st.markdown(' ###### - **An engaging scatter plot, organized by continents!**')
st.markdown(' The plot remains identical to the one displayed above, with the only modification being the substitution of countries with continents.')


fig = px.scatter(df, x= 'gdpPercap', y= 'lifeExp', size= 'pop', color= 'continent', hover_name= 'continent', 
                     log_x= True, size_max= 55, range_x=[100,100000], range_y=[20,90])
st.write(fig)
