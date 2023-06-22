from flask_restful import Resource
from flask import request, current_app
import os
from resources.controles.ocr_controler import OcrControler


class OCR(Resource):
    def get(self):
        file_name = request.get_json()['file_name']
        input_path = f'{current_app.config["INPUT_PATH"]}/{file_name}'
        output_path = f'{current_app.config["OUTPUT_PATH"]}/{file_name}'
        
        ocr_service = OcrControler(file_name)
        
        ocr_service.convert()
        

        
        
        return 'Hello World!'