import streamlit as st

st.sidebar.header("Description")
st.sidebar.markdown("Better food for more people.” Since our inception in 2010, we have grown tremendously, both in scope and scale - and emerged as India's most trusted brand during the pandemic, along with being one of the largest hyperlocal delivery networks in the country.")     

st.image('download.png')

st.title('Welcome to Zomato')

st.subheader('No cooking, order from zomato sunday kitchen')
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

import streamlit as st

def feedback_tab():
    st.selectbox('Did you like the food?', ['pretty good', 'Mast', 'not good', 'satisfied'])
    st.text_input('Any special dish for next weekend')
    st.radio('Was the delivery on time?', ['yes', 'No'])
    st.text_input('Feedback that may help us to improve')
    st.radio('Ratings', ['1', '2', '3', '4', '5'])
    if st.button('Submit'):
        st.write('Thank you for your valuable response')

def order_tab():
    st.title("Zomato-like Food Ordering System")

    menu = {
        "Dhosa": 100,
        "Fruitchat": 200,
        "Sabudana": 250,
        "Megaidli": 150,
        
    }

    selected_items = st.multiselect("Select items:", list(menu.keys()))

    if not selected_items:
        st.warning("Please select at least one item.")
        return

    total_price = sum(menu[item] for item in selected_items)

    st.subheader("Selected Items:")
    for item in selected_items:
        st.write(f"- {item} (Rs.{menu[item]:.2f})")

    st.subheader(f"Total Price: Rs.{total_price:.2f}")

    pay = st.selectbox('Payment Method:', ('Cash On Delivery', 'UPI APP'))
    if pay == 'Cash On Delivery':
        st.write('OK')
    if pay == 'UPI APP':
        col1, col2, col3 = st.columns(3)
        with col2:
            st.image('qrcode.jpg')
    if st.button('Submit'):
        st.write(':red[THANK YOU FOR YOUR PURCHASE!]:smile:')
        st.write('Your order is on its way.')

st.sidebar.title("Tabs")
selected_tab = st.sidebar.radio("", ["Feedback", "Order"])


if selected_tab == "Order":
    order_tab()
elif selected_tab == "Feedback":
    feedback_tab()
