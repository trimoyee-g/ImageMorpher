from dotenv import load_dotenv
import streamlit as st
import replicate

def perform_image_animation(image_file):
    try:
        output = replicate.run(
            "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
            input={"input_image": image_file}
        )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def mix_images(image_1, image_2):
    try:
        output = replicate.run(
    "lambdal/image-mixer:23d37d119ed3149e1135564d1cb5551c16dac1026e9deb972df42810a0f68c2f",
    input={"image1": image_1, "image2":image_2}
        )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def edit_image(image_path, prompt, negavtive_prompt):
    try:
         output = replicate.run(
                "logerzhu/ad-inpaint:b1c17d148455c1fda435ababe9ab1e03bc0d917cc3cf4251916f22c45c83c7df",
                input={"image_path": image_path, "prompt": prompt, "negavtive_prompt":negavtive_prompt}
            )
         return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def remove_image_bg(image):
    try:
        output = replicate.run(
        "cjwbw/rembg:fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003",
        input={"image": image}
        )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def generate_image(prompt):
    try:
        output = replicate.run(
    "playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8",
    input={"prompt": prompt}
        )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def generate_prompt(image):
    try:
        output = replicate.run(
    "pharmapsychotic/clip-interrogator:8151e1c9f47e696fa316146a2e35812ccf79cfc9eba05b11c7f450155102af70",
    input={"image": image}
        )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def perform_age_transformation(image):
    try:
        output = replicate.run(
    "yuval-alaluf/sam:9222a21c181b707209ef12b5e0d7e94c994b58f01c7b2fec075d2e892362f13c",
    input={"image": image}
    )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def selfie_to_anime(image):
    try:
        output = replicate.run(
    "netease-gameai/spatchgan-selfie2anime:3b95347ce81b6bfdf4613dd1093b86d75d5effe21c2f1a1fe0ec301ee023d424",
    input={"image": image}
    )
        return output
    except Exception as e:
        error_message = f"An error occurred: {e}" if e else "An unknown error occurred."
        st.error(error_message)

def animation_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    
    st.title("Generate Animation from Image")

    
    st.write("Convert your images into captivating video animations with seamless transitions!")
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Animate'):
            result = perform_image_animation(uploaded_file)
            st.success("Image animation completed!")
            # Display the animated result
            st.video(result)

def mix_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Generate Combined Image")

    
    st.write("Combine two images seamlessly into a stunning composition!")
    uploaded_file_1 = st.file_uploader("Upload 1st image", type=["jpg", "jpeg", "png"])
    uploaded_file_2 = st.file_uploader("Upload 2nd image", type=["jpg", "jpeg", "png"])

    if uploaded_file_1 is not None and uploaded_file_2 is not None:
        st.image(uploaded_file_1, caption='Uploaded 1st Image', use_column_width=True)
        st.image(uploaded_file_2, caption='Uploaded 2nd Image', use_column_width=True)
        if st.button('Mix'):
            result = mix_images(uploaded_file_1, uploaded_file_2)
            st.success("Image mixing completed!")
            # Display the animated result
            st.image(result)

def edit_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Edit and Enhance Image")

    
    st.write("Enhance and edit images with precision guided by your prompts!")
    uploaded_file = st.file_uploader("Uploaded image", type=["jpg", "jpeg", "png"])
    prompt_text = st.text_input("Enter prompt text")
    negavtive_prompt_text = st.text_input("Enter something you do not want in the image")

    if uploaded_file is not None and prompt_text and negavtive_prompt_text:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate'):
            result = edit_image(uploaded_file, prompt_text, negavtive_prompt_text)
            st.success("Image generation completed!")
            # Display the animated result
            st.image(result)

def remove_bg_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Remove Image Background")

    
    st.write("Effortlessly remove backgrounds from images with precision and ease!")
    uploaded_file = st.file_uploader("Uploaded image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None :
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate'):
            result = remove_image_bg(uploaded_file)
            st.success("Background removed!")
            # Display the animated result
            st.image(result)

def image_generation_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Generate Image using Prompt")

    
    st.write("Transform text into vivid visual creations effortlessly!")
    prompt_text = st.text_input("Enter prompt text")

    if prompt_text:
        if st.button('Generate'):
            result = generate_image(prompt_text)
            st.success("Image generation completed!")
            # Display the animated result
            st.image(result)

def prompt_generation_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Generate Prompt using Image")

    
    st.write("Instantly generate imaginative descriptions or narratives from images!")
    uploaded_file = st.file_uploader("Uploaded image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate'):
            result = generate_prompt(uploaded_file)
            st.success("Image generation completed!")
            # Display the animated result
            st.text(result)

def age_transformation_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Generate Age Transformation Animation from Image")

    
    st.write("Experience captivating age transformation animations from a single image input!")
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Animate'):
            result = perform_age_transformation(uploaded_file)
            st.success("Age transformation animation completed!")
            # Display the animated result
            st.video(result)

def selfie_to_anime_page():
    if st.button("[←"):
            st.session_state.page = "Landing Page"
    st.title("Turn Selfie to Anime")

    
    st.write("Turn your selfies into charming anime-style portraits!")
    uploaded_file = st.file_uploader("Uploaded image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None :
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Generate'):
            result = selfie_to_anime(uploaded_file)
            st.success("Background removed!")
            # Display the animated result
            st.image(result)

def landing_page():
    st.title("Welcome to PixelMorpher: Image Alchemy App")
    st.write("Create, Transform, and Unleash Imagination: Your Ultimate Image Wizard App!")
    st.write("")
    st.write("Hello human! How may I help you today?")
    st.write("")
    # Splitting options into two rows using columns
    col1, col2 = st.columns(2)

    with col1:
        if col1.button("Generate Image using Prompt"):
            st.session_state.page = "Image Generation Page"
        if col1.button("Generate Prompt using Image"):
            st.session_state.page = "Prompt Generation Page"
        if col1.button("Generate Animation from Image"):
            st.session_state.page = "Animation Page"
        if col1.button("Generate Age Transformation Animation from Image"):
            st.session_state.page = "Age Transformation Page"

    with col2:
        if col2.button("Remove Image Background"):
            st.session_state.page = "Background Removal Page"
        if col2.button("Turn Selfie to Anime"):
            st.session_state.page = "Selfie To Anime Page"
        if col2.button("Edit and Enhance Image"):
            st.session_state.page = "Edit Page"
        if col2.button("Generate Combined Image"):
            st.session_state.page = "Mix Page"

    
def main():
    load_dotenv()
    
    st.set_page_config(page_title="PixelMorpher: Image Alchemy App")
    # st.write(css, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = "Landing Page"

    if st.session_state.page == "Landing Page":
        landing_page()

    elif st.session_state.page == "Image Generation Page":
        image_generation_page()

    elif st.session_state.page == "Prompt Generation Page":
        prompt_generation_page()
    
    elif st.session_state.page == "Animation Page":
        animation_page()

    elif st.session_state.page == "Age Transformation Page":
        age_transformation_page()

    elif st.session_state.page == "Background Removal Page":
        remove_bg_page()

    elif st.session_state.page == "Selfie To Anime Page":
        selfie_to_anime_page()

    elif st.session_state.page == "Edit Page":
        edit_page()

    elif st.session_state.page == "Mix Page":
        mix_page()

if __name__ == '__main__':
    main()

