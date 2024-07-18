import requests
from config import EDAMAM_APPLICATION_ID, EDAMAM_APPLICATION_KEY

def search_recipes(cuisine_type, meal_type):

    url = f'https://api.edamam.com/search?q=&app_id={EDAMAM_APPLICATION_ID}&app_key={EDAMAM_APPLICATION_KEY}&cuisineType={cuisine_type}&mealType={meal_type}'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('hits', [])
    else:
        return None
