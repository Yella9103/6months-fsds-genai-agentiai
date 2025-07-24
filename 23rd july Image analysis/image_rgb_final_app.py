import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Image Processor", layout="wide")

# Title
st.title("Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    url = "https://st1.latestly.com/wp-content/uploads/2025/05/Virat-Kohli-Wallpapers-in-Test-Format-14.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

# Load and display image
virat = load_image()
st.image(virat, caption="Original Image", use_container_width=True)

# Convert to NumPy array
virat_np = np.array(virat)
R, G, B = virat_np[:, :, 0], virat_np[:, :, 1], virat_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(virat_np)
green_img = np.zeros_like(virat_np)
blue_img = np.zeros_like(virat_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

virat_gray = virat.convert("L")
virat_gray_np = np.array(virat_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(virat_gray_np, cmap=colormap)
plt.axis("off")

#DO NOT USE : plt.show()
#USE THIS INSTEAD:
st.pyplot(fig)