import os
import json
import random
import requests
import tempfile
from tqdm import tqdm
from django.core.files import File
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECommerceDjango.settings')
import django
django.setup()

from webstore.models import Category, Products

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data["products"]

def save_image_from_url(url):
    response = requests.get(url)
    img_temp = tempfile.NamedTemporaryFile(delete=True)
    img_temp.write(response.content)
    img_temp.flush()

    img = File(img_temp)
    return img

def populate_db(json_data):
    # Shuffle the JSON data to randomize the order of products
    random.shuffle(json_data)

    for product_data in tqdm(json_data, desc="Populating Database"):
        category, _ = Category.objects.get_or_create(name=product_data["category"])
        product = Products(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            category=category,
        )
        image = save_image_from_url(product_data["image"])
        product.image.save(f"{product.name}_image.jpg", image, save=True)

if __name__ == '__main__':
    json_data = load_json_data('products.json')
    populate_db(json_data)
