# # -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2010 Bernd Kreuss <prof7bit@gmail.com>                  #
#   Modifications and updates Copyright                                      #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = "it"
LANGUAGE_NAME = "Italiano"
LANGUAGE_NAME_ENGLISH = "Italian"
TRANSLATOR_NAMES = ["HostFat"]

#buttons
BTN_CANCEL = "Annulla"
BTN_OK = "Ok"
BTN_SAVE_AS = "Salva come..."
BTN_CLOSE = "Chiudi"

#status
ST_AVAILABLE = "Disponibile"
ST_AWAY = "Indisposto / lontano"
ST_EXTENDED_AWAY = "Molto indisposto / lontano"
ST_OFFLINE = "Non connesso"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Mostra/Nascondi TorChat"
MTB_QUIT = "Esci"

#popup menu
MPOP_CHAT = "Chat..."
MPOP_SEND_FILE = "Invia file..."
MPOP_EDIT_CONTACT = "Modifica contatto..."
MPOP_DELETE_CONTACT = "Cancella contatto..."
MPOP_SHOW_OFFLINE_MESSAGES = "Mostra i messaggi offline in attesa"
MPOP_CLEAR_OFFLINE_MESSAGES = "Cancella i messaggi offline in attesa"
MPOP_ACTIVATE_LOG = "Attiva il salvataggio log su file"
MPOP_STOP_LOG = "Ferma salvataggio log"
MPOP_DELETE_EXISTING_LOG = "Elimina file log esistente"
MPOP_DELETE_AND_STOP_LOG = "Cancella log e smetti di salvare"
MPOP_ADD_CONTACT = "Aggiungi contatto..."
MPOP_ABOUT = "About TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Chiedi %s..."
MPOP_SETTINGS = "Impostazioni..."
MPOP_EDIT_MY_PROFILE = "Modifica il mio profilo..."

#chat window popup menu
CPOP_COPY = "Copia"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Conferma cancellazione"
D_CONFIRM_DELETE_MESSAGE = "Vuoi veramente cancellare questo contatto?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Salvataggio log attivo"
D_LOG_WARNING_MESSAGE = "Salvataggio log su file attivato!\n\nLog File: %s\n\nRicordati di cancellare il file log quando hai finito il debugging il file log potrebbe contenere informazioni sensibili."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Porta già in uso"
D_WARN_USED_PORT_MESSAGE = "Qualcosa, probabilmente c'è un altro TorChat in esecuzione, è già in ascolto su %s:%s. Devi creare un altro profilo che usi porte differenti per poter avviare TorChat una seconda volta."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Messaggi non letti"
D_WARN_UNREAD_MESSAGE = "Sono presenti messaggi non letti.\nVerranno persi per sempre!\n\nVuoi veramente uscire ora da TorChat?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: L'utente è scollegato"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Questa operazione non è possibile con utenti scollegati"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: File multipli"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Non dovresti avviare trasferimenti multipli di file in un'unica operazione. Invia trasferimenti singoli individualmente oppure inviali zippati"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Errore salvataggio file"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Non è stato possibile creare il file '%s'.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: File esistente"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Il file '%s' esiste già.\nSovrascriverlo?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Aggiungi nuovo contatto"
DEC_TITLE_EDIT = "Modifica contatto"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Mostra nome"
DEC_INTRODUCTION = "Introduzione"
DEC_MSG_16_CHARACTERS = "L'indirizzo deve essere lungo 16 or 56 caratteri, non %i."
DEC_MSG_ONLY_ALPANUM = "L'indirizzo può contenere solo numeri e caratteri in minuscolo."
DEC_MSG_ALREADY_ON_LIST = "%s è già nella tua lista."

#dialog: edit my profile
DEP_TITLE = "Modifca il mio profilo"
DEP_NAME = "Nome"
DEP_TEXT = "Testo"
DEP_SET_AVATAR = "Imposta Avatar"
DEP_REMOVE_AVATAR = "Rimuovi Avatar"
DEP_AVATAR_SELECT_PNG = "Seleziona file .PNG da usare come avatar (verà scalato a 64*64, può contenere trasparenze)"
DEP_PNG_FILES = "File PNG"
DEP_ALL_FILES = "Tutti i file"
DEP_WARN_TITLE = "Impossibile selezionare Avatar"
DEP_WARN_IS_ALREADY = "Questo è già l'avatar corrente"
DEP_WARN_MUST_BE_PNG = "L'avatar deve essere un file .png"

#file transfer window
DFT_FILE_OPEN_TITLE = "Invia file a %s"
DFT_FILE_SAVE_TITLE = "Salva file da %s"
DFT_SEND = "Inviando %s\na %s\n%04.1f%% (%i di %i bytes)"
DFT_RECEIVE = "Ricevendo %s\nda %s\n%04.1f%% (%i di %i bytes)"
DFT_WAITING = "in attesa di connessione"
DFT_STARTING = "avvio trasferimento"
DFT_ABORTED = "trasferimento inconcluso"
DFT_COMPLETE = "trasferimento completato"
DFT_ERROR = "errore"

#settings dialaog
DSET_TITLE = "Configurazione TorChat"
DSET_NET_TITLE = "Network"
DSET_NET_ACTIVE = "attivo"
DSET_NET_INACTIVE = "inattivo"
DSET_NET_TOR_ADDRESS = "Indirizzo proxy Tor"
DSET_NET_TOR_SOCKS = "Porta Socks"
DSET_NET_TOR_CONTROL = "Porta di controllo"
DSET_NET_OWN_HOSTNAME = "Il proprio TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Interfaccia in ascolto"
DSET_NET_LISTEN_PORT = "Porta in ascolto"
DSET_GUI_TITLE = "Interfaccia utente"
DSET_GUI_LANGUAGE = "Lingua"
DSET_GUI_OPEN_MAIN_HIDDEN = "Avvia con finestra minimizzata"
DSET_GUI_OPEN_CHAT_HIDDEN = "Non aprire automaticamente nuove finestre"
DSET_GUI_NOTIFICATION_POPUP = "Notifica pop-up"
DSET_GUI_NOTIFICATION_METHOD = "Metodo di notifica"
DSET_GUI_FLASH_WINDOW = "Titolo finestra lampeggiante con nuovi messaggi"
DSET_MISC_TITLE = "Varie"
DSET_MISC_TEMP_IN_DATA = "Salva file temporanei nella cartella data"
DSET_MISC_TEMP_CUSTOM_DIR = "Cartella temporanea (lascia vuoto per la default dell'OS)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "messaggi in ritardo in attesa di essere inviati"
NOTICE_DELAYED_MSG_SENT = "messaggi in ritardo sono stati inviati"
NOTICE_DELAYED = "ritardato"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: messaggi in attesa"
MSG_OFFLINE_EMPTY = "non ci sono (ulteriori) messaggi in attesa per %s"
MSG_OFFLINE_QUEUED = "messaggi offline in attesa per %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Contatto non connesso"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Collegato, in attesa di connessione di ritorno..."
BPOP_CLIENT_SOFTWARE = "Client: %s V%s"

#logging of conversations to file
LOG_HEADER = "Questo file log non è firmato e non è valido come prova"
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
LOG_STARTED = "Salvataggio log avviato"
LOG_STOPPED = "Salvataggio log fermato"
LOG_DELETED = "I file log sono stati cancellati"
LOG_IS_ACTIVATED = "Salvataggio log su file è stato attivato:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Il salvataggio è stato fermato ma il vecchio file log è ancora presente:\n%s"


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
ABOUT_TITLE = "About TorChat"
ABOUT_TEXT = """TorChat %(version)s (build: r%(svn)s)\
  %(copyright)s\
\
Runtime environment:\
  Python: %(python)s\
  wx: %(wx)s\
\
TorChat is free software: you can redistribute it and/or \
modify it under the terms of the GNU General Public \
License as published by the Free Software Foundation, \
either version 3 of the License, or (at your option) \
any later version.\
\
TorChat is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied \
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \
See the GNU General Public License for more details.\
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
