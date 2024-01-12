import streamlit as st

def home_page():
    st.title("Home Page")
    st.subheader("Welcome! This Web App is an application where you can start with image prediction.")
    st.subheader("Please continue to the next page if you wish to test Classification Model!")


    # Add information about flower classes
    st.markdown("Here are 20 classes of flowers that you will find interesting:")

    # Dictionary with flower classes and captions
    flower_info = {
        "Tulip": "Beautiful and vibrant tulips.",
        "Orchids": "Exotic and diverse orchid species.",
        "Peonies": "Soft and delicate peonies in various colors.",
        "Hydrangeas": "Clusters of hydrangea flowers in different hues.",
        "Lilies": "Elegant and fragrant lilies.",
        "Gardenias": "White and fragrant gardenia blooms.",
        "Garden Roses": "Classic and romantic garden roses.",
        "Daisies": "Simple and cheerful daisies.",
        "Hibiscus": "Tropical and vibrant hibiscus flowers.",
        "Bougainvillea": "Colorful and ornamental bougainvillea vines.",
        "Sunflower": "Bright and cheerful sunflowers.",
        "Marigold": "Traditional and festive marigold flowers.",
        "Lavender": "Fragrant and calming lavender plants.",
        "Chrysanthemum": "Various varieties of chrysanthemums.",
        "Lotus": "Sacred and symbolic lotus flowers.",
        "Frangipani": "Tropical and fragrant frangipani blooms.",
        "Jasmine": "Sweet-scented and delicate jasmine flowers.",
        "Ixora": "Clusters of vibrant ixora blooms.",
        "Lantana": "Color-changing lantana flowers.",
        "Snapdragon": "Snapdragon flowers with a unique shape."
    }

   # Display flower classes with customized styling
    for flower_class, caption in flower_info.items():
        st.header(flower_class)
        st.markdown(f"<p style='color: #009688; font-size: 16px; font-weight: bold;'>{caption}</p>", unsafe_allow_html=True)
        st.write("---")

    # st.button("Next", on_click=project_page)

# if __name__ == "__main__":
#     main()

    