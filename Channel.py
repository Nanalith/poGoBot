class ChannelRaid:
    """Classe definissant le contenu en cours des channels de raid:
    - NB_CHANNEL: nombre de channel construites par le bot
    - id: numero du cannal
    - raid: descripsion du raid en cours, si raid = 0 alors c'est vide
    - com: l'objet discord.channel qui permet de communiquer simplement avec le rest du forum
    - pinMsg: message decrivant le raid de la channel (c'est plus simple que de le chercher)
    - listMsg"""

    nb_channel = 0

    def __init__(self, com):
        """initialisation d'une channel avec pour seul information son ID, le raid est initialisé à 0"""
        ChannelRaid.nb_channel += 1
        self.raid = 0
        self.id = ChannelRaid.nb_channel
        self.com = com
        self.pinMsg = 0
        self.listMsg = 0


    def ajouterRaid(self, raid):
        """ajoute un raid dans une channel libre
        retourne le raid si l'ajout a marché
        retourn 0 sinon"""
        if self.raid == 0:
            self.raid = raid
            raid.id = self.id
            return self

        return 0

    def retirerRaid(self):
        """retirer le raid en cour dans la channel"""
        if self.raid != 0:
            self.raid = 0
        return 1

    def channelLibre(channels):
        """renvoit la channel de plus petit numero libre pour ajouter un nouveau canal
        renvoit 0 sinon"""
        for channel in channels.values():
            if channel.raid == 0:
                return channel
        return 0

    def isRaid(self):
        """renvoit 1 si un raid est présent 0 sinon"""
        if self.raid == 0:
            return 0
        else:
            return 1

    def updateChannelList(channels):
        """retourne un message contenant les carracteristique des channels"""
        message = 0
        for channel in channels.values():
            if channel.raid == 0:
                message += str("Pas de raid en cours sur #raid-%i \n" %(channel.id))
            else:
                message += channel.raid.afficherList()

        return message
