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

LANGUAGE_CODE = "hu"
LANGUAGE_NAME = "Magyar"
LANGUAGE_NAME_ENGLISH = "Hungarian"
TRANSLATOR_NAMES = ["d4n3sz"]

#buttons
BTN_CANCEL = "Mégse"
BTN_OK = "Ok"
BTN_SAVE_AS = "Mentés másként..."
BTN_CLOSE = "Bezár"

#status
ST_AVAILABLE = "Elérhető"
ST_AWAY = "Rögtön jövök"
ST_EXTENDED_AWAY = "Nincs a gépnél"
ST_OFFLINE = "Kapcsolat nélkül"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Mutat/Rejt TorChat"
MTB_QUIT = "Kilépés"

#popup menu
MPOP_CHAT = "Chat..."
MPOP_SEND_FILE = "Fájl küldés..."
MPOP_EDIT_CONTACT = "Partner szerkesztése..."
MPOP_DELETE_CONTACT = "Partner törlése..."
MPOP_SHOW_OFFLINE_MESSAGES = "Offline ki küldött üzenetek mutatása"
MPOP_CLEAR_OFFLINE_MESSAGES = "Offline kiküldött üzenetek törlése"
# MPOP_ACTIVATE_LOG = u"Activate logging to file"
# MPOP_STOP_LOG = u"Stop logging"
# MPOP_DELETE_EXISTING_LOG = u"Delete existing log file"
# MPOP_DELETE_AND_STOP_LOG = u"Delete log and stop logging"
MPOP_ADD_CONTACT = "Partner hozzáadása..."
MPOP_ABOUT = "A TorChat-ról"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Kérdezd %s..."
MPOP_SETTINGS = "Beállítások..."
# MPOP_EDIT_MY_PROFILE = u"Edit my profile..."

#chat window popup menu
CPOP_COPY = "Másolás"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Törlés megerősítése"
D_CONFIRM_DELETE_MESSAGE = "Valóban törölni akarod?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Logolás aktív"
D_LOG_WARNING_MESSAGE = "Logolás mentése fájlba bekapcsolva!\n\nLog Fájl: %s\n\nNe felejtsd el törölni a log fájlt, ha befejezted a hibakeresést,mert személyes információkat is tartalmazhat."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: A port már használatban van"
D_WARN_USED_PORT_MESSAGE = "Valószínűleg már egy másik TorChat fut itt:  %s:%s. Csinálj egy másik profilt más porttal, hogy el tudj indítani egy másik TorChat-et!"

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Olvasatlan üzenet"
D_WARN_UNREAD_MESSAGE = "Olvasatlan üzeneted van.\nEl fog veszni véglegesen!\n\nBiztosan ki akarsz lépni a TorChat-ból?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Partner nincs kapcsolódva"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Ezt a műveleted nem lehet végrehajtani kapcsolat nélküli partnerrel"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Sok fájl"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Nem tudsz egyszerre több fájlt küldeni. Küldd el a fájlokat egyenként, vagy használj tömörítést (pl. zip)"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Hiba a fájl mentése közben"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "A '%s' fájl létrehozása sikertelen.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: A fájl már létezik"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "A '%s' már létezik.\nFelülírod?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Új partner hozzáadása"
DEC_TITLE_EDIT = "Partner szerkesztése"
DEC_TORCHAT_ID = "TorChat azonosító"
DEC_DISPLAY_NAME = "Megjelenített név"
DEC_INTRODUCTION = "Bemutatkozás"
DEC_MSG_16_CHARACTERS = "Az azonosító 16 or 56 karakter hosszú lehet, nem %i."
DEC_MSG_ONLY_ALPANUM = "Az azonosító csak számokat és az angol abc betüit tartalmazhatja"
DEC_MSG_ALREADY_ON_LIST = "%s már a listádban van"

# #dialog: edit my profile
# DEP_TITLE = u"Edit my profile"
# DEP_NAME = u"Name"
# DEP_TEXT = u"Text"
# DEP_SET_AVATAR = u"Set Avatar"
# DEP_REMOVE_AVATAR = u"Remove Avatar"
# DEP_AVATAR_SELECT_PNG = u"Select .PNG file to use as your avatar (will be scaled to 64*64, may contain transparency)"
# DEP_PNG_FILES = u"PNG files"
# DEP_ALL_FILES = u"All files"
# DEP_WARN_TITLE = u"Avatar selection not possible"
# DEP_WARN_IS_ALREADY = u"This is already the current avatar"
# DEP_WARN_MUST_BE_PNG = u"The avatar must be a .png file"

#file transfer window
DFT_FILE_OPEN_TITLE = "Fájl küldése %s számára"
DFT_FILE_SAVE_TITLE = "Fájl mentése %s-től"
DFT_SEND = "Külédes %s\n %s-nak\n%04.1f%% (%i kész %i bájtból)"
DFT_RECEIVE = "Fogadás  %s\n %s-től\n%04.1f%% (%i kész %i bájtból)"
# DFT_WAITING = u"waiting for connection"
# DFT_STARTING = u"starting transfer"
# DFT_ABORTED = u"transfer aborted"
# DFT_COMPLETE = u"transfer complete"
# DFT_ERROR = u"error"

#settings dialaog
DSET_TITLE = "TorChat beállítások"
DSET_NET_TITLE = "Hálózat"
DSET_NET_ACTIVE = "aktív"
DSET_NET_INACTIVE = "inaktív"
DSET_NET_TOR_ADDRESS = "Tor proxy cím"
DSET_NET_TOR_SOCKS = "Socks port"
DSET_NET_TOR_CONTROL = "Control port"
DSET_NET_OWN_HOSTNAME = "Saját TorChat-azonosító"
DSET_NET_LISTEN_INTERFACE = "Figyelő cím"
DSET_NET_LISTEN_PORT = "Figyelő port"
DSET_GUI_TITLE = "Felhasználói felület"
DSET_GUI_LANGUAGE = "Nyelv"
DSET_GUI_OPEN_MAIN_HIDDEN = "Indítás minimalizált ablakkal"
DSET_GUI_OPEN_CHAT_HIDDEN = "Ne nyisson automatikusan új ablakokat"
DSET_GUI_NOTIFICATION_POPUP = "Felugró figyelmeztetések"
# DSET_GUI_NOTIFICATION_METHOD = u"Notification method"
DSET_GUI_FLASH_WINDOW = "Ablak címének villogtatása új üzenet érkezésekor"
DSET_MISC_TITLE = "Egyebek"
DSET_MISC_TEMP_IN_DATA = "Ideiglenes fájlok tárolása a saját könyvtárban"
DSET_MISC_TEMP_CUSTOM_DIR = "Ideiglenes könyvtár (ha üres, akkor az op.rendszer alapértelmezett könyvtára)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "várakozó üzenetek küldése"
NOTICE_DELAYED_MSG_SENT = "várakozó üzenetek elküldve"
NOTICE_DELAYED = "várakozik/késleltetett"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: várakozó üzenetek"
MSG_OFFLINE_EMPTY = "nincs (több) várakozó üzenet %s felöl"
MSG_OFFLINE_QUEUED = "várakozó offline üzenet %s felöl:\n\n%s"

# #buddy list mouse hover popup
# BPOP_BUDDY_IS_OFFLINE = u"Buddy is offline"
# BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Connected, awaiting return connection..."
# BPOP_CLIENT_SOFTWARE = u"Client: %s V%s"

# #logging of conversations to file
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
# LOG_STARTED = u"Logging started"
# LOG_STOPPED = u"Logging stopped"
# LOG_DELETED = u"Log files have been deleted"
# LOG_IS_ACTIVATED = u"Logging to file is activated:\n%s"
# LOG_IS_STOPPED_OLD_LOG_FOUND = u"Logging is stopped but old log file still exists:\n%s"


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
ABOUT_TITLE = "A TorChat-ról"
ABOUT_TEXT = " ""TorChat %(version)s (svn: r%(svn)s)\
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
"" " 
