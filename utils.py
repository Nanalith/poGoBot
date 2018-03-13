import datetime
from utils import *
from data import *
import re
import unidecode

#function hors loop
def isNotBot(m):
    """prend en entree un discord.on_message
    renvoit 1 si l'auteur n'est pas un bot 0 sinon"""
    return m.author.bot != True
def isRappelCommand(m):
    """ renvoit 1 si c'est un rappel de commande 0 sinon"""
    return m.content.startswith("Comme je suis sympa je te redonne la commande que tu as essayé de taper :")
def isFuture(temps, ref=datetime.datetime.now()):
    """ prend en entree un heure au format %H:%M et test si elle appartien au future du now en entrée
    renvoit 1 si oui
    renvoit 0 si la date n'est pas au bon format ou si l'heure est dans le passée"""
    assert isinstance(ref, datetime.datetime)
    assert isinstance(temps, datetime.datetime)

    return temps > ref
def isPast(temps, ref=datetime.datetime.now()):
    """ prend en entree un heure au format %H:%M et test si elle appartien au passé du now en entrée
    renvoit 1 si oui
    renvoit 0 si la date n'est pas au bon format ou si l'heure est dans le passée"""
    assert isinstance(ref, datetime.datetime)
    assert isinstance(temps, datetime.datetime)

    return temps < ref
def isPokemon(pokeName):
    """prend en entré un nom de pokemon ou un oeuf
    renvoit 1 si'il existe dans le pokedex
    0 sinon"""
    RegexOeuf = re.compile(r"T[0-9]")
    if RegexOeuf.match(str(pokeName)): return 1

    for ip, pokemon in enumerate(pokedex):
        for nom in pokemon.values():
            if nom == str(pokeName).lower(): return 1
            
    return 0
def lirePokeName(pokeName):
    """ Permet de lire le pokéName donné en entrée grace au dictionnaire de poketrad. Il pourra chercher en français et en anglais
    retourne le numero du pokemon ou le niveau de l'oeuf (negatif)
    retourne 0 si il n'existe pas"""
    RegexOeuf = re.compile(r"t[0-9]")
    if RegexOeuf.match(str(pokeName)):
        num = pokeName[1:]
        if int(num):
            num = int(num)
            if num < 6 and num > 0: return -num

    for ip, pokemon in enumerate(pokedex):
        for nom in pokemon.values():
            if nom == str(pokeName).lower():
                    return ip+1
    return 0
def lirePokeId(pokeId):
    """ permet de lire un pokeId et renvoit le nom du pokemon ou de l'oeuf
    retourn le nom de l'oeuf ou du pokemon
    0 sinon"""
    if pokeId < 0:
        return str("T%i" %(-pokeId))
    elif pokeId > 0 and pokeId < len(pokedex):
        return pokedex[pokeId-1]["fr"]
    else: return 0
def isTeam(team):
    """verifie si la team appartien au dictionnaire
    renvoit le teamName si oui, 0 sinon"""
    if not isinstance(team, str): return 0

    for teamName, trad in teamdex.items():
        if team == trad["fr"]: return teamName

    return 0
def isUniquePlace(battlePlace, cRaids):
    """retourne 1 si l'endroit n'a jamais été utilisé 0 sinon"""
    if not isinstance(battlePlace, str): return 0
    for cCurrent in cRaids.values():
        if battlePlace == cCurrent.raid.battlePlace: return 0

    return 1
def isOeufName(pokeName):
    """retourne 1 si c'est un nom d'oeuf, O sinon"""
    if isinstance(pokeName, str):
        regexOeuf = re.compile(r"t[0-9]")
        regexEx = re.compile(r"tex")
        if regexOeuf.match(pokeName) or regexEx.match(pokeName): return 1
    return 0
def rappelCommand(commandName):
    """envoi à l'utilisateur un message permettant de reexpliquer la commande"""
    return str("Comme je suis sympa je te redonne la commande que tu as essayé de taper :\n %s" %commandex[commandName])
def getTimeStr(time, label):
    """return the str corresponding to the time at (%H:%M) format with the appropriate label"""

    if time == 0:
        temps = str("%s: ? \n" %label)
    else:
        assert isinstance(time, datetime.datetime)
        temps = str("%s: %s \n" %(label, time.strftime("%H:%M")))

    return temps
def isHour(time):
    """renvoit 1 si l'heure est au bon format pour etre transformé en heure, 0 sinon"""
    try:
        assert isinstance(time, str)

        regex = re.compile(r"[0-9]*:[0-9]*")
        assert regex.match(time)

        args = time.split(":")
        assert len(args) == 2 and isinstance(int(args[0]), int) and isinstance(int(args[1]), int)

        heure = int(args[0])
        minute = int(args[1])
        assert heure < 24 and heure >= 0
        assert minute < 60 and minute >= 0

    except AssertionError:
        return 0

    return 1
def convertTime(time):
    args = time.split(":")
    time = datetime.datetime.now()
    time = time.replace(hour=int(args[0]), minute=int(args[1]), second=0)

    return time

if __name__=="__main__":
    #debut des test unitaires
    pass
