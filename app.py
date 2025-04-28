
from flask import Flask, request, send_file
from PIL import Image, ImageEnhance
import io

app = Flask(__name__)

@app.route('/restaurar', methods=['POST'])
def restaurar():
    file = request.files['imagem']
    img = Image.open(file.stream)

    # Ajustes de restauração simulada
    img = img.convert('RGB')
    sharpness = ImageEnhance.Sharpness(img).enhance(2.0)
    contrast = ImageEnhance.Contrast(sharpness).enhance(1.5)
    brightness = ImageEnhance.Brightness(contrast).enhance(1.2)

    # Salvar em memória e devolver
    img_io = io.BytesIO()
    brightness.save(img_io, 'JPEG', quality=85)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
