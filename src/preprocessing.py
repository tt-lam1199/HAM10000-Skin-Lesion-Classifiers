def image_to_array(example, size=(32, 32)):
    """Convert a Hugging Face/Pillow image to a normalized RGB array."""
    image = example["image"].convert("RGB").resize(size)
    return np.asarray(image, dtype=np.float32) / 255.0