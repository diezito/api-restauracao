from flask import Flask, request, send_file
from PIL import Image
import requests
import replicate
import io
import os

app = Flask(__name__)

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

@app.route("/restore", methods=["POST"])
def restore_image():
    if "image" not in request.files:
        return {"error": "Imagem não enviada"}, 400

    image_file = request.files["image"]
    image_bytes = image_file.read()

    output_url = replicate.run(
        "sczhou/codeformer:1facb5e4b6db70e56f39849ed60c83778b7b7bfa7c591b3a4fda080aeb5f3adb",
        input={"image": image_bytes},
        api_token=REPLICATE_API_TOKEN
    )

    response = requests.get(output_url)
    return send_file(io.BytesIO(response.content), mimetype="image/png")
