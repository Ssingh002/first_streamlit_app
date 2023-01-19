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

#New section to display fruitvice api response
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
#imports results into variable
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") 
# kiwi above is hardcoded to the website addresss
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
# the above allows fruit choice to be added on the fly

#The following dumps the information of the Watermelon in a straighline
#streamlit.text(fruityvice_response.json())
#rturns dump: { "genus": "Citrullus", "name": "Watermelon", "id": 25, "family": "Cucurbitaceae", "order": "Cucurbitales", "nutritions": { "carbohydrates": 8, "protein": 0.6, "fat": 0.2, "calories": 30, "sugar": 6 } }


# Normalizes the above data in columns and values
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# dumps the variable
streamlit.dataframe(fruityvice_normalized)

#Lesson 12. Created new requirements.txt
import snowflake.connector
# query trail a/c metadata
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute ("select * from fruit_load_list")
my_data_row = my_cur.fetchone() 
# fetches one using cursor
streamlit.text(my_data_row)
stremlit.text ("The fruit load list contains:")
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
