
import os
import pytesseract
from PIL import Image   
from flask import current_app


class OcrControler: 


    def __init__(self, file_name ):
        self.file_name = file_name
        

    def get_page_number(self, image_name):
        return image_name.split('_')[-1].split('.')[0]

    def get_sorted_images(self, images):
        sorted_images = sorted(images, key=lambda image: int(self.get_page_number(image)))
        
        return sorted_images

    def convert(self):
        input_path = current_app.config['INPUT_PATH']
        output_path = current_app.config['OUTPUT_PATH']
        output_path = output_path+ '/' + self.file_name
        os.makedirs(output_path, exist_ok=True)
        images = os.listdir(input_path + '/' + self.file_name)
        sorted_images = self.get_sorted_images(images)
        with open(f'{output_path}/{self.file_name}.txt', 'w') as f:
            for image in sorted_images:
                img = Image.open(f'{input_path}/{self.file_name}/{image}')
                text = pytesseract.image_to_string(img, lang='por')
                page_number = self.get_page_number(image)
                
                f.write(f'{page_number} \n {text}')
                os.remove(f'{input_path}/{self.file_name}/{image}')
                print(f'Página {page_number} convertida com sucesso!')
        os.removedirs(f'{input_path}/{self.file_name}')
        print('Conversão finalizada!')