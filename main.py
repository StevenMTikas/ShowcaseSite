import streamlit as st

st.set_page_config(layout='wide')

with st.container():
    # create 2 column layout
    col1, col2 = st.columns(2)

    with col1:
        st.image('FILES/photo.png')

    with col2:
        st.title('Steven Tikas')
        content = '''
        Hi, I am Steven! I am a Python programmer, student, and learner.  I graduated in 2018.  I have
        worked with companies from various countries, such as Center for Conservation Geography, to map
        and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing
        data mining to gain business insights with the Australian Rapid Intelligence (not really to most 
        of this but maybe in the future this is just some content to fill up space but my name is really 
        Steven and I am a Python programmer...in training, student, and learner).
    '''
        st.info(content)

content_container2 = '''
        This is some more content to try and see if this works to pass the Day 21 student project section of
        the course and see if I can move on to Day 22 in the course
    '''
st.info(content_container2)