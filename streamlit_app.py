import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach & Rocke Smoothie')
streamlit.text ('🐔Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  
#Pandas is another pacakage library. File below is picked from our s3 bucket
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruite_list is called a dataframe
my_fruit_list = my_fruit_list.set_index('Fruit')
#above allows you to pick the specific fruit from drop down. Without this we would have to use the rowID

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page
#streamlit.multiselect ("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#Above prepopulates listed fruite
#Important: Fruit name needs to be spelled the same as the dataframe. Error otherwise

fruits_selected = streamlit.multiselect ("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#Use Variable to store saved fruit
fruits_to_show = my_fruit_list.loc[fruits_selected]
# variable will pull the details of the selected fruit from dataframe
# .loc gives rows by label
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
