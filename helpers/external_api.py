import requests

CONST_API_URL = "https://lasalle-frenchverb-api-afpnl.ondigitalocean.app/v1/api"
CONST_API_URL_VERB = CONST_API_URL + "/verb"
CONST_API_URL_VERB_RANDOM = CONST_API_URL + "/verb/random"
CONST_DICT_TOKEN = {'token':'278ef2169b144e879aec4f48383dce28e654a009cacf46f8b6c03bbc9a4b9d11'}

def get_verb_from_api(verb):
    return requests.get(CONST_API_URL_VERB, headers=CONST_DICT_TOKEN, json={'verb':verb})

def get_random_from_api(quantity):
    return requests.get(CONST_API_URL_VERB_RANDOM, headers=CONST_DICT_TOKEN, json={'quantity':quantity})