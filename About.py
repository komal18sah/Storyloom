import streamlit as st

# st.set_page_config(
#     page_title="Multipage App",
#     page_icon="😃",
# )

# st.title("Main Page")
# st.sidebar.success("select a page above")

st.set_page_config(page_title="Recommender System", layout="wide")

# Header
# st.title("STORYLOOM")

# Footer
st.markdown(
    """
    <h1 style='text-align: center; color: #6420AA; font-size: 80px; font-family: "serif";'>
        StoryLoom
    </h1>

    <h2 style='text-align: center; color: #C65BCF; font-family: "serif";'>
      weaving together your personalized narratives
    </h2>
     
    <h5 style='text-align: center; color: #C65BCF; font-family: "serif";'>
     your one-stop destination that seamlessly integrates two recommendation systems: <br>
    </h5>

    <p  style=' color: #C65BCF; font-family: "serif";'>

        LitCompass: Beyond the title, beyond the author. Your perfect book awaits.
        Craving a new book or revisiting a cherished classic? LitCompass acts as your personal guide, steering you towards hidden gems and timeless tales that resonate with your taste. Share your favorite author or book title, and LitCompass curates a reading list that transcends titles, unlocking literary treasures that align with your reading desires.
        MovieSage: Love that movie? We've got your next obsession.

        Enter MovieSage, your personal movie guru! Feed it a movie title, and MovieSage crafts a unique watchlist. Venture beyond the realm of sequels and remakes to discover fresh narratives that will ignite your passion for film. MovieSage unveils a world of cinematic experiences waiting to be explored.

        Through LitCompass and MovieSage, Storyloom personalizes your storytelling journey. It allows you to explore new genres, rediscover old favorites, and embark on unexpected adventures.

        So, what story will you weave today? have fun
        Let Storyloom be your guide, your literary compass, and your cinematic sage – all woven together to ignite your love for new narratives. Dive deeper, discover further, and get ready to be captivated by the stories Storyloom helps you find.
    </p>
    """,
    unsafe_allow_html=True
)

