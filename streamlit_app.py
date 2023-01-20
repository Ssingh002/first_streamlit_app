import streamlit
import requests
#imports results into variable

#Pandas is another pacakage library. File below is picked from our s3 bucket
import pandas

import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text ('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach & Rocke Smoothie')
streamlit.text ('🐔Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  
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

#create the repeatable code block(function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
  
streamlit.header("Fruityvice Fruit Advice!")  
# As per Lession 12 - Try/Except chapter
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
    streamlit.error ("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
 
except URLError as e:
    streamlit.error()
    
#New section to display fruitvice api response
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") 
# kiwi above is hardcoded to the website addresss
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
# the above allows fruit choice to be added on the fly

#The following dumps the information of the Watermelon in a straighline
#streamlit.text(fruityvice_response.json())
#rturns dump: { "genus": "Citrullus", "name": "Watermelon", "id": 25, "family": "Cucurbitaceae", "order": "Cucurbitales", "nutritions": { "carbohydrates": 8, "protein": 0.6, "fat": 0.2, "calories": 30, "sugar": 6 } }


# Normalizes the above data in columns and values
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# dumps the variable
#streamlit.dataframe(fruityvice_normalized)

#don't run anything past here while we troubleshoot
#streamlit.stop()

#Lesson 12. Created new requirements.txt
# query trail a/c metadata

#L12. Button Action
streamlit.header ("The fruit load list contains:")
#Snowflake - related functions
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute ("select * from fruit_load_list")
      return my_cur.fetchall()
 
#Add a button to load the fruit
if streamlit.button('Get Fruit Load list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows) 

#would put all the data into normalized format - column/row



#streamlit.stop()


#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)



#New section to display fruitvice api response
add_my_fruit = streamlit.text_input('What fruit would you like like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)


#this will not work correctly
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")



#Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_curr:
    my_curr.execute("insert into fruit_Load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit


    
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

