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

#Lesson 9
streamlit.header("Fruityvice Fruit Advice!")  
import requests
#imports results into variable
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#The following dumps the information of the Watermelon in a straighline
#streamlit.text(fruityvice_response.json())
#rturns dump: { "genus": "Citrullus", "name": "Watermelon", "id": 25, "family": "Cucurbitaceae", "order": "Cucurbitales", "nutritions": { "carbohydrates": 8, "protein": 0.6, "fat": 0.2, "calories": 30, "sugar": 6 } }


# Normalizes the above data in columns and values
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# dumps the variable
streamlit.dataframe(fruityvice_normalized)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# dumps the variable
streamlit.dataframe(fruityvice_normalized)

#
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
