import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Guts Image Processor", layout="wide")

# Title
st.title("Guts Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    path = r'C:\Users\dines\VS codes\image analysis\myimage.jpg'
    return Image.open(path).convert("RGB")

# Load and display image
guts = load_image()
st.image(guts, caption="Original Guts Image", use_container_width=True)

# Convert to NumPy array
guts_np = np.array(guts)
R, G, B = guts_np[:, :, 0], guts_np[:, :, 1], guts_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(guts_np)
green_img = np.zeros_like(guts_np)
blue_img = np.zeros_like(guts_np)

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

guts_gray = guts.convert("L")
guts_gray_np = np.array(guts_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(guts_gray_np, cmap=colormap)
plt.axis("off")

st.pyplot(fig)