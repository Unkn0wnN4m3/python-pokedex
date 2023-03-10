import logging

from pokedex import species

# NOTE: logging messages
# INFO -> 10
# DEBUG -> 20
# WARNING -> 30
# ERROR -> 40
# CRITICAL -> 50

if __name__ == '__main__':
    pokemon_species = species()
    logging.debug(pokemon_species)
