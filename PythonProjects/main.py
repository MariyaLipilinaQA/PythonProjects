from email import message
from urllib import response
import requests

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '94e34472e3ff3042981a55aa0df85b45'
HEADR= {'Content-Type':'application/json','trainer_token':TOKEN}

body_registration= {
    "trainer_token": TOKEN,
    "email": "mari.lipilina@mail.ru",
    "password": "Iloveqa777"
}
body_confirmation={
    "trainer_token": TOKEN
}

body_create= {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_change_name= {
    "pokemon_id": "327472",
    "name": "Бабочка",
    "photo_id": 12
}

body_pokeboll={
    "pokemon_id": "327348"
}

'''response=requests.post(url=f'{URL}/trainers/reg', headers=HEADR, json= body_registration)
print(response.text)'''

'''response_confirmation=requests.post(url=f'{URL}/trainers/confirm_email',headers=HEADR, json=body_confirmation)
print(response_confirmation.text)'''

'''response_create =  requests.post(url=f'{URL}/pokemons',headers=HEADR, json=body_create)
print(response_create.text)
'''
'''message = response_create. json()['message']
print(message)'''

'''response=requests.put(url=f'{URL}/pokemons',headers=HEADR, json=body_change_name)
print(response.text)'''

response_pokeboll=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADR, json=body_pokeboll)
print(response_pokeboll.text)