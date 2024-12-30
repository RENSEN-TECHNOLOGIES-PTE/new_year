import streamlit as st
img = "edited_wish2025.gif"
logo ='rensenlogo.png'

# Apply global styles
st.set_page_config(
    page_title="Styled Page", 
    layout="centered",  # 'centered' or 'wide'
    initial_sidebar_state="collapsed"  # 'expanded' or 'collapsed'
    
)

with st.container():

    st.image(logo , width=300)
    st.title("🎉 New Year Wishes... 🎉")
    st.write("")
    st.write("Wishing you a New Year filled with new hopes, new joys, and new beginnings! May this year bring you success, happiness, and good health in abundance. May you always find the strength to chase your dreams and the peace to enjoy every moment. Here's to fresh starts and exciting adventures ahead. Cheers to a year full of love, laughter, and growth. Happy New Year!")
    st.write("")
    st.write("")
    st.image(img)
    st.write("")
    st.write("")
    st.header('Our Products:')
    st.write("")
    st.subheader("Medosys")
    st.write("Medosys is the future of healthcare consultations! Our platform connects patients with qualified doctors through a simple, user-friendly interface, making it easier than ever to schedule consultations and receive medical advice from the comfort of your home. Whether you need a routine check-up or guidance on a specific health issue, we are here to help. Additionally, we offer a community and support portal to enhance the overall experience and provide comprehensive assistance for this solution.")
    st.subheader("Data Infosight")
    st.write("Data Infosight is a tool for transforming data into meaningful, interactive visual insights. Whether you're a business leader, data analyst, or anyone who works with data, our application is designed to simplify complex datasets, helping you make informed decisions with ease.")
    st.subheader("Assetain")
    st.write("Assetain is a cutting-edge solution designed to help manufacturing and production companies maintain optimal asset performance and prevent unexpected downtime..")
    st.header('About us:')
    st.write("We are a Software solution development company coming from consulting experience. From a consultant's view, first, we understand the client's pain points to develop solutions than technology focused. We have developed many solutions for different industries across the globe. Our company is a team of passionate professionals who are dedicated to delivering high-quality products and services to our clients.")

    # st.write("We work on a wide range of technologies and solutions like Application development, Artificial Intelligence, Machine Learning, IoT, Cloud Management, and SaaS solution.")
