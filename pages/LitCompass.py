import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests


def recommend(input,preference):

    if preference == "By Author":
       index = author.index(input)
    else:
       index = books[books['Book-Title'] == input].index[0]

    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data

# st.title('Book Recommender System')

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400..900;1,400..900&family=Concert+One&family=Playfair+Display:ital,wght@1,400..900&display=swap');
    </style>
    <h1 style='text-align: center; color: #6420AA; font-size: 80px; font-family: "serif";'>
        LitCompass
    </h1>

    <h2 style='text-align: center; color: #C65BCF; font-family: "serif";'>
       Beyond the title, beyond the author. Your perfect book awaits.
    </h2>
    
    """,
    unsafe_allow_html=True
)

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books (2).pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

book_name = list(popular_df['Book-Title'].values)
author=list(popular_df['Book-Author'].values)
image=list(popular_df['Image-URL-M'].values)
votes=list(popular_df['num_ratings'].values)
rating=list(popular_df['avg_rating'].values)


recommendation_preference = st.radio("Choose preference", ["By Author", "By Book Title"])
userinput = ""
if recommendation_preference == "By Author":
    selected_author_name = st.selectbox('Select Author', (author))
    userinput = selected_author_name
else:
    selected_book_name = st.selectbox('Select Book', (book_name))
    userinput = selected_book_name

if st.button('Cue up'):
    data = recommend(userinput,recommendation_preference)

    names = []
    posters = []
    authors = []

    for d in data:
        names.append(d[0])
        posters.append(d[2])
        authors.append(d[1])

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.text(authors[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.text(authors[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.text(authors[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.text(authors[2])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.text(authors[4])
        st.image(posters[4])
