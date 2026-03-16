from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

model = tf.keras.models.load_model("cat_dog_model.keras")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET","POST"])
def predict():

    if request.method == "POST":

        file = request.files["file"]
        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        img = image.load_img(filepath, target_size=(224,224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)

        prob = prediction[0][0]

        dog_prob = round(prob*100,2)
        cat_prob = round((1-prob)*100,2)

        if prob > 0.5:
            result = "Dog 🐶"
        else:
            result = "Cat 🐱"

        accuracy = max(dog_prob,cat_prob)

        return render_template(
            "predict.html",
            result=result,
            image=filepath,
            dog_prob=dog_prob,
            cat_prob=cat_prob,
            accuracy=accuracy
        )

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)