import requests


def species():
    """ Return pokemon by species
    >>> type(species()) == type(list())
    True
    """
    RESPONSE = requests.get("https://pokeapi.co/api/v2/pokemon-species/")

    if RESPONSE.status_code == 200:
        payload = RESPONSE.json()
        return payload["results"]
