#Chanceller Waters
#Module 9 : API
#the purpose of this code is to retrieve display and format data using pokeapi
import requests

base_url = "http://pokeapi.co/api/v2/"


def get_pokemon_info(name_or_id):
    """retrieves pokemon info for a given pokemon name or id"""

    #specifc URL for Pokemon given its name or id in pokedex
    url = f"{base_url}pokemon/{name_or_id}"

    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"failed to retrieve pokemon info for {name_or_id}. Status code: {response.status_code}")
        return (None)


pokemon_name = "eevee"
eevee_data = get_pokemon_info(pokemon_name)

if eevee_data:
    print(f"Name:{eevee_data['name'].capitalize()}")
    print(f"ID:{eevee_data['id']}")

    types = [type_info['type']['name'].capitalize() for type_info in eevee_data['types']]
    print(f"Type(s):{','.join(types)}")
    #upon retrieval of Eevee's height and weight  further conversion is needed to display them in familiar units
    print(f"Height:{eevee_data['height']} decimetres")
    print(f"Weight:{eevee_data['weight']} hectograms")