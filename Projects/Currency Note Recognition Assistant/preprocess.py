
def preprocess_image(image_path):

    img = load_img(image_path, target_size=(224,224))

    img_array = img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array
