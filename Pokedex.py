"""
This script helps someone to test the consumption of APIS and can play by sending as parameters 
a name of some pokemon or the number and get information about it.
"""

from http import HTTPStatus, client

import json

URLPOKEDEX = "pokeapi.co"

def getInfoPokemon(keyword):
    request = client.HTTPSConnection(URLPOKEDEX)
    request.request("GET", "/api/v2/pokemon/{}".format(keyword))
    response = request.getresponse()
    if response.status == HTTPStatus.OK:
        pokemonInfo = json.loads(response.read().decode("utf-8"))
        print("Name : {}".format(pokemonInfo["name"]))
        print("Type : {}".format(pokemonInfo["types"]))
    else:
        print("Pokemon no found.")

getInfoPokemon(2)
