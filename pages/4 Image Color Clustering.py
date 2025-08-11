import PIL
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
import os

random_state = 25

def create_clusters(models, img_df):
    for model, labels in models.items():
        colors = pd.concat(
            [img_df,pd.DataFrame({'cluster':labels})],axis=1
            ).groupby('cluster').mean()
        rgb_colors = colors[['R', 'G', 'B']].values
        rgb_colors = [tuple(map(int, row)) for row in rgb_colors]


        colors_tuple = [tuple(color) for color in rgb_colors]

        html_blocks = f"<h5> Top 5 Colors (According to {model}):</h5>" + "".join(
        f"<div style='display:inline-block; width:125px; height:50px; background-color:rgb{color}; margin:2px;'></div>"
        for color in colors_tuple
        )

        st.markdown(html_blocks, unsafe_allow_html=True)

st.header('Image Color Clustering')
st.subheader('Upload an image to see its 5 dominant colors.')

img_b = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])
if img_b is not None:
    with open('temp_image.jpg', 'wb') as f:
        if img_b is not None:
            f.write(img_b.getbuffer())
            st.success('Image you uploaded:')
            st.image(img_b)
            img_path = 'temp_image.jpg'
        else:
            img_path = None
            st.error('Error uploading image. Please try again.')
try:
    if st.button('Cluster Colors'):

        img = np.array(PIL.Image.open(img_path).resize((100,100)))
        R = img[:,:,0].flatten()
        G = img[:,:,1].flatten()
        B = img[:,:,2].flatten()
        img_df = pd.DataFrame({'R':R,'G':G,'B':B})

        km = KMeans(n_clusters=5, random_state=random_state)
        ag = AgglomerativeClustering(n_clusters=5)
        gm = GaussianMixture(n_components=5, random_state=random_state)
        km.fit(img_df)
        ag.fit(img_df)
        gm.fit(img_df)

        models = {
            'KMeans': km.labels_,
            'Agglomerative Clustering': ag.labels_,
            'Gaussian Mixture Models': gm.predict(img_df)
        }

        create_clusters(models, img_df)

        if os.path.exists(img_path):
            os.remove(img_path)
except:
    st.error("Please upload a valid image file and try again.")