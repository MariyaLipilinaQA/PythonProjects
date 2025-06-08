import requests
import pytest

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= 'Введите свой токен'
HEADR= {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '33372'

def test_status_code():
    respons=requests.get(url=f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID})
    assert respons.status_code==200 

def test_part_of_response():
        response_get=requests.get(url=f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["name"]=='Бульбазавр'


@pytest.mark.parametrize('key,value',[('name,Бульбазав'),('trainer_id', TRAINER_ID),('id', '327472')])
def test_parametrize(key,value):
 response_parametrize=requests.get(url=f'{URL}/pokemons',params={'trainer_id' : TRAINER_ID})     
 assert response_parametrize.json()['data'][0][key]==value

       
