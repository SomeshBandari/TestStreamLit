import streamlit as st

st.write("""
         # To The largest of the 3 numbers
         Please slect 3 number below to proceed
         """)
         
st.header('User Input Parameters') 
num1 = st.number_input('num1')
num2 = st.number_input('num2')
num3 = st.number_input('num3')


if st.button("Find Largest Number"):
        st.write('Largest number is:' , max(num1,num2,num3))


    
       