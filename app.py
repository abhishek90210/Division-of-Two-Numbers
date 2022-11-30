import streamlit as st 

def main():
  st.title("Division of Two Numbers - WEEK 8 ASSIGNMENT TDS")
  html_temp = """
  <div style="background-color:VIOLET;padding:10px">
  <h2 style="color:black;text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  
  if(num1==0):
    result = 0
  elif (num2 ==0):
    result = "UNDEFINED"
  elif (num1==0 and num2==0):
    result ="UNDEFINED"
  else:
    result=num1/num2
  
  st.success('The output is {}'.format(result))
  
if __name__=='__main__':
    main()
