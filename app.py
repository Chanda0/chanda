import streamlit as st

st.sidebar.header("Description")
st.sidebar.markdown("Better food for more people.” Since our inception in 2010, we have grown tremendously, both in scope and scale - and emerged as India's most trusted brand during the pandemic, along with being one of the largest hyperlocal delivery networks in the country.")     

st.image('download.png')
st.divider()
st.title('Welcome to Zomato')
st.divider()
st.subheader('No cooking, order from zomato sunday kitchen')
st.divider()
st.write('Weeken start hua aapka')
b=st.radio('Feeling hungry',['yes','No'])
if b=='No':
    st.write('Aree kha lo sunday hai , sunday zomato ke sath')

a=st.selectbox('Did u want heavy or light breakfast',['Heavy','Light'])
if a=='Heavy':
    col1 ,col2 =st.columns(2)
    with col1:
       st.radio('heavy menu',['Fried rice','Kepsa rice','butter chicken','tandoori chicken'])
    with col2:
       st.image('images.jpg')
if a=='Light':
    col1 ,col2,col3 =st.columns(3)
    with col1:
         st.radio('Light menu',['Upma','kanda poha','plane sandwich','fruit salad with fruit'])
    with col2:
        st.image('kandapoha.jpg')
    with col3:
        st.image('fruitchat.jpg')   
st.radio('Special sunday',['Dhosa','Sabudana','idli','coffee','menduvada'])
col1 ,col2,col3 =st.columns(3)
with col1:
    st.image('dhosa.jpg')
with col2:
    st.image('idli.jpg')
with col3:
    st.image('sabudana.jpg') 

tab1, tab2 = st.tabs(["feedback","data"])
with tab1:
    st.selectbox('Did u like the food',['preety good','Mast','not good','satisfied'])
    st.text_input('Any special dish for next weekend')
    st.radio('Was the delivery on time',['yes','No'])
    st.text_input('Feedback that may help us to improve')
    st.radio('ratings',['1','2','3','4','5'])
with tab2:
    st.sidebar.header("Zomato Customer satisfaction graph")
    st.image("data-11.png")

