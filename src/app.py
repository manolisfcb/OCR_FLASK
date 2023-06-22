from flask import Flask
from PIL import Image
import pytesseract
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/convertir')
def convertir():
    img = Image.open('src/input/AFContrato_OD 00000000010128966109_1/AFContrato_OD 00000000010128966109_1_page_1.tiff')
    text = pytesseract.image_to_string(img, lang='por')
    return text

from resources.OCR import OCR

api.add_resource(OCR, '/ocr')

if __name__ == '__main__':
    app.run(debug=True)
