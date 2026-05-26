import numpy as np
from PIL import Image
from google import genai
from dotenv import load_dotenv
import json
import sys
import os

if 'paddleocr' not in sys.modules:
    from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True)

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = genai.Client(api_key=API_KEY)

def predict(image):
    image = Image.open(image)
    image = np.array(image)

    predicted = ocr.predict(image)

    texts = []
    for res in predicted:
        texts = res['rec_texts']

    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=f'''
        {texts}
        Extract only the item name (without item code), quantity, and price from the data above and make it into a structured json data.
        Example: ["item_name": ..., "quantity": ..., "price": ...]
        If there are discounts, directly apply it to the price. Don't need to write the discount information.
        If the item name is not separated properly, separate it with whitespace.
        '''
    )

    result = response.text
    result = result.replace('```json', '').replace('```', '').strip()
    result = json.loads(result)

    return result