# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2010 Bernd Kreuss <prof7bit@gmail.com>                  #
#   Modifications and updates Copyright                                      #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = "fr"
LANGUAGE_NAME = "Français"
LANGUAGE_NAME_ENGLISH = "French"
TRANSLATOR_NAMES = ["vitisch", "Pierre Abbat"]

#buttons
BTN_CANCEL = "Annuler"
BTN_OK = "Ok"
BTN_SAVE_AS = "Save as..."
BTN_CLOSE = "Fermer"

#status
ST_AVAILABLE = "Disponible"
ST_AWAY = "Absent"
ST_EXTENDED_AWAY = "Absent pour longtemps"
ST_OFFLINE = "Déconnecté"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Montrer/Cacher TorChat"
MTB_QUIT = "Arrêtez"

#popup menu
MPOP_CHAT = "Chat..."
MPOP_SEND_FILE = "Envoyer un fichier..."
MPOP_EDIT_CONTACT = "Rediger contact..."
MPOP_DELETE_CONTACT = "Supprimer contact..."
MPOP_SHOW_OFFLINE_MESSAGES = "Montrer les messages hors-ligne"
MPOP_CLEAR_OFFLINE_MESSAGES = "Effacer les messages hors-ligne"
MPOP_ACTIVATE_LOG = "Activer le fichier d'archivage"
MPOP_STOP_LOG = "Désactiver l'archivage"
MPOP_DELETE_EXISTING_LOG = "Supprimer le fichier d'archivage"
MPOP_DELETE_AND_STOP_LOG = "Cesser d'archiver et supprimer le fichier"
MPOP_ADD_CONTACT = "Ajouter un contact..."
MPOP_ABOUT = "À propos..."
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Demandez %s..."
MPOP_SETTINGS = "Paramètres..."
MPOP_EDIT_MY_PROFILE = "Modifier mon profil..."

# #chat window popup menu
CPOP_COPY = "Copier"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Confirmez la supression"
D_CONFIRM_DELETE_MESSAGE = "Êtes-vous sûr de vouloir supprimer le contact?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Archivage est actif"
D_LOG_WARNING_MESSAGE = "L'archivage au fichier est activé!!\n\nFicher d'archivage: %s\n\nRappelez-vous de supprimer le ficher d'archivage si vous avez fini la correction parce que le ficher d'archivage peut contenir l'information sensible."

# #warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Port déjà occupé"
D_WARN_USED_PORT_MESSAGE = "Quelque chose, probablement une autre instance de TorChat, écoute déjà à %s:%s. Vous devez créer un autre profil qui utilise des autres ports pour pouvoir commencer TorChat une autre fois."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Messages non lus"
D_WARN_UNREAD_MESSAGE = "Il y a des messages non lus.\nIls seront perdus pour toujours!\n\nVoulez-vous vraiment sortir maintenant?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Copain hors ligne"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Cette opération n'est pas possible quand le copain est hors ligne"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Plusieurs fichiers"
D_WARN_FILE_ONLY_ONE_MESSAGE = "On ne peut pas transférer plusieurs fichiers en une seule opération. Commencez les transferts individualement ou envoyez un fichier zip ou tar"

# #warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Erreur sauvant fichier"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Le fichier '%s' ne peut pas être créé.\n\n%s"

# #warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: Fichier existe"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Le fichier '%s' existe déjà.\nSurécrire?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Ajouter un nouveau contact"
DEC_TITLE_EDIT = "Modifier le contact"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Nom d'utilisateur"
DEC_INTRODUCTION = "Introduction"
DEC_MSG_16_CHARACTERS = "L'adresse doit avoir 16 or 56 caractères, pas %i."
DEC_MSG_ONLY_ALPANUM = "L'adresse doit seulement contenir des nombres et des lettres minuscule."
DEC_MSG_ALREADY_ON_LIST = "%s est déjà sur votre liste."

# #dialog: edit my profile
DEP_TITLE = "Modifier mon profil"
DEP_NAME = "Nom"
DEP_TEXT = "Texte"
# DEP_SET_AVATAR = u"Set Avatar"
# DEP_REMOVE_AVATAR = u"Remove Avatar"
DEP_AVATAR_SELECT_PNG = "Sélectionner fichier .PNG pour votre avatar (agrandi ou réduit à 64*64, peut contenir transparence)"
DEP_PNG_FILES = "Fichiers PNG"
DEP_ALL_FILES = "Tous fichiers"
DEP_WARN_TITLE = "Sélection d'avatar impossible"
DEP_WARN_IS_ALREADY = "C'est déjá l'avatar actuel"
DEP_WARN_MUST_BE_PNG = "L'avatar doit être un fichier .png"

#file transfer window
DFT_FILE_OPEN_TITLE = "Envoyer fichier à %s"
DFT_FILE_SAVE_TITLE = "Sauver fichier de %s"
DFT_SEND = "Envoyer %s\nà %s\n%04.1f%% (%i de %i octets)"
DFT_RECEIVE = "Recevoir %s\nde %s\n%04.1f%% (%i de %i octets)"
DFT_WAITING = "attendant connexion"
DFT_STARTING = "commençant transfert"
DFT_ABORTED = "transfert avorté"
DFT_COMPLETE = "transfert complet"
DFT_ERROR = "erreur"

#settings dialaog
DSET_TITLE = "Configuration de TorChat"
DSET_NET_TITLE = "Réseau"
DSET_NET_ACTIVE = "actif"
DSET_NET_INACTIVE = "inactif"
DSET_NET_TOR_ADDRESS = "Adresse de procuration pour Tor"
DSET_NET_TOR_SOCKS = "Port de SOCKS"
DSET_NET_TOR_CONTROL = "Port de commande"
DSET_NET_OWN_HOSTNAME = "Mon TorChat ID"
DSET_NET_LISTEN_INTERFACE = "Interface d'écouter"
DSET_NET_LISTEN_PORT = "Port d'écouter"
DSET_GUI_TITLE = "Interface d'utilisateur"
DSET_GUI_LANGUAGE = "Langue"
DSET_GUI_OPEN_MAIN_HIDDEN = "Commencer avec fenêtre principale minimalisée"
DSET_GUI_OPEN_CHAT_HIDDEN = "Ne pas ouvrir automatiquement des nouvelles fenêtres"
DSET_GUI_NOTIFICATION_POPUP = "Notification surgissante"
# DSET_GUI_NOTIFICATION_METHOD = u"Notification method"
DSET_GUI_FLASH_WINDOW = "Clignoter titre de fenêtre à un nouveau message"
DSET_MISC_TITLE = "Misc"
DSET_MISC_TEMP_IN_DATA = "Cacher fichiers temporaires dans le directoir de données"
DSET_MISC_TEMP_CUSTOM_DIR = "Directoire temporaire (laissez vide pour défaut de SE)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "messages retardés attendant pour être envoyé"
NOTICE_DELAYED_MSG_SENT = "messages retardés ont été envoyés"
NOTICE_DELAYED = "retardé"

# #messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: messages en queue"
MSG_OFFLINE_EMPTY = "pas de messages en queue pour %s"
MSG_OFFLINE_QUEUED = "messages en queue pour %s hors ligne:\n\n%s"

# #buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Copain est hors ligne"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Connexion aller, attendant connexion retour..."
BPOP_CLIENT_SOFTWARE = "Client: %s V%s"

# #logging of conversations to file
LOG_HEADER = "Ce fichier d'archive n'es pas signé et n'a pas de cogence de preuve."
# LOG_HEADER1 = u"Note to the criminal & corrupt agents of law enforcement:"
# LOG_HEADER2 = u"(A fake chat log file is easily created by setting computer time to a suitable creation date"
# LOG_HEADER3 = u"- then creating the file with a text editor, thereby establishing a file creation time. Next,"
# LOG_HEADER4 = u"- fill the file with the evidence / fake conversations / incriminating evidence. When satified,"
# LOG_HEADER5 = u"- set the computer time to a suitable / incriminating last conversation time and make a small"
# LOG_HEADER6 = u"- change to the log file and save. Thus establishing the modification date. You now have a"
# LOG_HEADER7 = u"- chat log file, completely acceptable to the US DOJ & FBI as the evidence to convict."
# LOG_HEADER8 = u"- It is so easy to be a corrupt government agent, creating evidence & putting people away!)"
# LOG_HEADERQ1 = u" ""The way to have safe government is not to trust it all to the one, but to divide it "
# LOG_HEADERQ2 = u"among the many, distributing to everyone exactly the functions in which he is competent..."
# LOG_HEADERQ3 = u"To let the National Government be entrusted with the defense of the nation, and its foreign "
# LOG_HEADERQ4 = u"and federal relations... The State Governments with the Civil Rights, Laws, Police and "
# LOG_HEADERQ5 = u"administration of what concerns the State generally. The Counties with the local concerns, "
# LOG_HEADERQ6 = u"and each ward direct the interests within itself. It is by dividing and subdividing these "
# LOG_HEADERQ7 = u"Republics from the great national one down through all its subordinations until it ends in "
# LOG_HEADERQ8 = u"the administration of everyman's farm by himself, by placing under everyone what his own eye "
# LOG_HEADERQ9 = u"may superintend, that all will be done for the best."" -- Thomas Jefferson"
LOG_STARTED = "Commence à archiver"
LOG_STOPPED = "Cesse d'archiver"
LOG_DELETED = "Supprime les fichiers d'archive"
LOG_IS_ACTIVATED = "Active l'archive à fichier:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Désactive l'archive mais le fichier existe encore:\n%s"


#TipJar box
TIPJAR_TITLE = "TorChat Bitcoin Tip-Jar"
TIPJAR_TEXT = " "" Please Help support future development and maintenance of TorChat  \
\
    Bitcoin tip-jar:  -- %(tipjar)s -- \
\
          Thank You!!\
\
\
Copy the TorChat Bitcoin Tip-Jar address to the clipboard?\
"" "

#about box
ABOUT_TITLE = "À propos de TorChat"
ABOUT_TEXT = """TorChat %(version)s (svn: r%(svn)s)\
  %(copyright)s\
\
Environnement de marche:\
  Python: %(python)s\
  wx: %(wx)s\
\
TorChat est un logiciel libre: vous pouvez le redistribuer et/ou \
modifier sous les termes de la GNU General Public \
License publié par la Free Software Foundation, \
soit version 3 de la License, ou (à votre option) \
une version postérieure.\
\
TorChat est distribué en espérant qu'il soit utile, \
mais SANS AUCUNE GARANTIE; ni même la garantie \
implicite de MARCHANTABILITÉ or APTITUDE À PROPOS PARTICULIER. \
Voir la GNU General Public License pour plus de détails.\
\
*\
\
Please Help support future development and maintenance of TorChat  \
 ---\
 --- Bitcoin tip-jar:  -- %(tipjar)s -- \
 ---\
<your generosity will help keep the TorChat updates flowing> \
\
\
""" 
