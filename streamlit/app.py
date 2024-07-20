import matplotlib.pyplot as plt
import streamlit as st 
import pandas as pd
st.header('streamlit')
st.subheader('subhead')
st.write('stream lit')
st.write(65)
st.markdown("give up on yr dream and die ")
st.markdown(65)
st.write("hi nikil")
st.markdown("""
    | col1 | col2 |
    |------|------|
    | 1    | 3    |
    | 2    | 4    |
    """)
st.markdown("_its italic _")
dict= {
    'x ':[1,2,3,5],
    'y':[3,4,5,6]
}
df = pd.DataFrame(dict)
st.write(df)
a = st.button('click')
if a:  
    st.write('clicked chal ab kalti mar')
st.sidebar.write('yeh apna side bar h ')
st.set_option('deprecation.showPyplotGlobalUse', False)

choice = st.sidebar.selectbox('yeh select box h ',{1:'one',2:'two'})


x=[1,2,3,4,5,6,7,8]
y=[2,32,4,24,4,54,5,75,]
plt.plot(x,y)
plt.xlabel  ('x label')
plt.ylabel('y lable')
plt.title("line plt")
st.pyplot()


x=[1,2,3,4,5,6,7,8]
y=[2,32,4,24,4,54,5,75,]
plt.bar(x,y)
plt.xlabel  ('x label')
plt.ylabel('y lable')
plt.title("line plt")
st.pyplot()



x=[1,2,3,4,5,6,7,8]
y=[2,32,4,24,4,54,5,75,]
plt.scatter(x,y)
plt.xlabel  ('x label')
plt.ylabel('y lable')
plt.title("line plt")
st.pyplot()

data =[1,2,3,4,5,6,7,8,9,8,9,7,6,5,4,3,3,21,12,3,4,5,7,7,5,4]
plt.figure()
plt.hist(data,bins=30)
plt.xlabel("value")
plt.ylabel('frequnecy')
plt.title("histogram")
st.pyplot(plt)

lables = ['a','b','c','d','e']
sizes=[15,20,30,10,45]
plt.figure()
plt.pie(sizes, labels=lables,autopct='%1.1f%%',startangle=0)
st.pyplot()

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 10, 5]

fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Plot')

# Corrected line to display the plot in Streamlit
st.pyplot(fig)
