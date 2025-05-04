from flask import Flask, request, send_file
from PIL import Image, ImageEnhance
import io
import os

app = Flask(__name__)

@app.route('/restaurar', methods=['POST'])
def restaurar():
    file = request.files['foto']
    image = Image.open(file.stream)
    image = image.convert('RGB')
    image = ImageEnhance.Sharpness(image).enhance(2.0)

    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)