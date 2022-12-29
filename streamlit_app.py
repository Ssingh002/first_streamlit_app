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
#streamlit.multiselect ("Pick some fruits:",list(my_fruit_list.index),['Avacado','Strawberries'])
#Above prepopulates listed fruite
#Important: Fruit name needs to be spelled the same as the dataframe. Error otherwise

streamlit.dataframe(my_fruit_list)   
# display dataframe
