import streamlit as st
import pickle
import os
import sys
root_dir = os.getcwd()
sys.path.insert(0, os.path.join(root_dir,'Spam Classification'))
import helper

text_ppl_path = os.path.join(root_dir,'Spam Classification','text_ppl.pkl')

with open(text_ppl_path, 'rb') as f:
    text_ppl = pickle.load(f)

st.title('E-Mail/SMS Spam Classification')
st.subheader('Upload an E-Mail file below: (EML or TXT format only)')
file = st.file_uploader('Upload E-Mail/SMS file', type=['eml', 'txt'])
with open('temp.eml', 'wb') as f:
    if file is not None:
        f.write(file.getbuffer())
        st.success('File uploaded successfully!')
        email_text = ''
    file_path = 'temp.eml'

st.subheader('OR')
st.subheader('Enter the E-Mail/SMS text directly below:')
if file is not None:
    st.text_area('E-Mail/SMS Text', height=200, disabled=True)
else:
    email_text = st.text_area('E-Mail/SMS Text', height=200)

st.text('')
if st.button('Classify'):
    if file is not None and email_text:
        st.warning('Please provide either a file or text input, not both.')

    elif file is not None:
        email_text = helper.EmailToText().transform(file_path)
        if isinstance(email_text, list):
            email_text = email_text[0]

    prediction = text_ppl.predict([email_text])
    if prediction[0] == 1:
        st.error('This E-Mail/SMS is SPAM.')
    else:
        st.success('This E-Mail/SMS is NOT SPAM.')
    st.write("E-Mail/SMS Content:")
    st.caption(email_text)
if os.path.exists(file_path):
    os.remove(file_path)