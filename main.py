import streamlit as st
import pandas as pd

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
        Here are some of the python projects that I've built or plan to build in the near future.  Contact me
        for more information by visiting the Contact Me page from the left sidebar
    '''
st.info(content_container2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('FILES/data.csv', sep=';')
print(df)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('FILES/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('FILES/' + row['image'])
        st.write(f"[Source Code]({row['url']})")