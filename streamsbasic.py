import streamlit as st
st.title("CALCULATOR")
number = st.number_input("Insert a number")
n2=st.number_input("Insert 2nd number")
option = st.selectbox(
    "Which operation do you want to perform",
    ("Addition", "Subtraction", "Multiplication","Division"))
if(option == "Addition"):
    st.write("The sum of two number is ", number+n2)
elif(option == "Subtraction"):
    st.write("The difference of two numbers is",number-n2)
elif(option == "Multiplication"):
    st.write("The product of two numbers is",number*n2)
elif(option=="Division"):
    st.write("The division of two numbers is",number/n2)