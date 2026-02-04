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

LANGUAGE_CODE = "sv"
LANGUAGE_NAME = "Svenska"
LANGUAGE_NAME_ENGLISH = "Swedish"
TRANSLATOR_NAMES = ["Åke Engelbrektson"]

#buttons
BTN_CANCEL = "Avbryt"
BTN_OK = "OK"
BTN_SAVE_AS = "Spara som..."
BTN_CLOSE = "Stäng"

#status
ST_AVAILABLE = "Tillgänglig"
ST_AWAY = "Frånvarande"
ST_EXTENDED_AWAY = "Utökad frånvaro"
ST_OFFLINE = "Offline"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Visa/Dölj TorChat"
MTB_QUIT = "Avsluta"

#popup menu
MPOP_CHAT = "Chatta..."
MPOP_SEND_FILE = "Sänd fil..."
MPOP_EDIT_CONTACT = "Redigera kontakt..."
MPOP_DELETE_CONTACT = "Ta bort kontakt..."
MPOP_SHOW_OFFLINE_MESSAGES = "Visa köade offline-meddelanden"
MPOP_CLEAR_OFFLINE_MESSAGES = "Rensa köade offline-meddelanden"
MPOP_ACTIVATE_LOG = "Aktivera loggning till fil"
MPOP_STOP_LOG = "Stoppa loggning"
MPOP_DELETE_EXISTING_LOG = "Ta bort befintlig loggfil"
MPOP_DELETE_AND_STOP_LOG = "Ta bort logg och stoppa loggning"
MPOP_ADD_CONTACT = "Lägg till kontakt..."
MPOP_ABOUT = "Om TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Fråga %s..."
MPOP_SETTINGS = "Inställningar..."
MPOP_EDIT_MY_PROFILE = "Redigera min profil..."

#chat window popup menu
CPOP_COPY = "Kopiera"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Bekräfta borttagning"
D_CONFIRM_DELETE_MESSAGE = "Vill du verkligen ta bort den här kontakten?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Loggning är aktiverad"
D_LOG_WARNING_MESSAGE = "Loggning till fil är aktiverad!\n\nLoggfil: %s\n\nGlöm inte att ta bort loggfilen när du har avslutat felsökningen. Loggfilen kan innehålla känslig information."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Porten används redan"
D_WARN_USED_PORT_MESSAGE = "Något, troligen en annan TorChat-instans, lyssnar redan på %s:%s. Du måste skapa en profil till, som använder andra portar, för att kunna starta TorChat en andra gång."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Olästa meddelanden"
D_WARN_UNREAD_MESSAGE = "Det finns olästa meddelanden.\nDom kommer att förloras för alltid!\n\nVill du verkligen avsluta TorChat nu?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Kontakten är offline"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Denna åtgärd fungerat inte med frånkopplade kontakter"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Flera filer"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Du kan inte skicka flera filer i en och samma överföring. Skicka filerna en och en, eller packettera dom i en zip-fil"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Kan inte spara fil"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Filen '%s' kunde inte skapas.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: Filen finns redan"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Filen '%s' finns redan.\nVill du byta ut den?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Lägg till ny kontakt"
DEC_TITLE_EDIT = "Redigera kontakt"
DEC_TORCHAT_ID = "TorChat-ID"
DEC_DISPLAY_NAME = "Visningsnamn"
DEC_INTRODUCTION = "Introduktion"
DEC_MSG_16_CHARACTERS = "Adressen måste vara 16 or 56 tecken lång, inte %i."
DEC_MSG_ONLY_ALPANUM = "Adressen kan bara bestå av siffror och små bokstäver"
DEC_MSG_ALREADY_ON_LIST = "%s finns redan i din lista"

#dialog: edit my profile
DEP_TITLE = "Redigera min profil"
DEP_NAME = "Namn"
DEP_TEXT = "Text"
DEP_SET_AVATAR = "Ange avatar"
DEP_REMOVE_AVATAR = "Ta bort avatar"
DEP_AVATAR_SELECT_PNG = "Välj en .png-fil som din avatar (kommer att skalas om till 64x64px, får innehålla transparens)"
DEP_PNG_FILES = "PNG-filer"
DEP_ALL_FILES = "Alla filer"
DEP_WARN_TITLE = "Filen kan inte användas som avatar"
DEP_WARN_IS_ALREADY = "Den här bilden är redan din avatar"
DEP_WARN_MUST_BE_PNG = "Avataren måste vara en .png-fil"

#file transfer window
DFT_FILE_OPEN_TITLE = "Sänd fil till %s"
DFT_FILE_SAVE_TITLE = "Spara fil från %s"
DFT_SEND = "Sänder %s\ntill %s\n%04.1f%% (%i av %i byte)"
DFT_RECEIVE = "Tar emot %s\nfrån %s\n%04.1f%% (%i av %i byte)"
DFT_WAITING = "väntar på anslutning"
DFT_STARTING = "startar överföring"
DFT_ABORTED = "överföring avbruten"
DFT_COMPLETE = "överföring slutförd"
DFT_ERROR = "fel"

#settings dialaog
DSET_TITLE = "TorChat konfiguration"
DSET_NET_TITLE = "Nätverk"
DSET_NET_ACTIVE = "aktiv"
DSET_NET_INACTIVE = "inaktiv"
DSET_NET_TOR_ADDRESS = "Tor proxy-adress"
DSET_NET_TOR_SOCKS = "Socks-port"
DSET_NET_TOR_CONTROL = "Kontrollport"
DSET_NET_OWN_HOSTNAME = "Eget TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Lyssningsgränssnitt"
DSET_NET_LISTEN_PORT = "Lyssningsport"
DSET_GUI_TITLE = "Användargränssnitt"
DSET_GUI_LANGUAGE = "Språk"
DSET_GUI_OPEN_MAIN_HIDDEN = "Starta minimerad"
DSET_GUI_OPEN_CHAT_HIDDEN = "Öppna inte nya fönster automatiskt"
DSET_GUI_NOTIFICATION_POPUP = "Popupmeddelande"
DSET_GUI_NOTIFICATION_METHOD = "Meddelandemetod"
DSET_GUI_FLASH_WINDOW = "Blinka med fönster vid nytt meddelande"
DSET_MISC_TITLE = "Diverse"
DSET_MISC_TEMP_IN_DATA = "Lagra temporära filer i programmappen"
DSET_MISC_TEMP_CUSTOM_DIR = "Temp-mapp (lämnas tom för systemstandard)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "Fördröjda meddelanden som väntar på att skickas "
NOTICE_DELAYED_MSG_SENT = "fördröjda meddelanden har skickats"
NOTICE_DELAYED = "fördröjd"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: köade meddelanden"
MSG_OFFLINE_EMPTY = "det finns inga (fler) köade meddelanden för %s"
MSG_OFFLINE_QUEUED = "köade offline-meddelanden för %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Kontakten är offline"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Ansluten, väntar på svarsanslutning..."
BPOP_CLIENT_SOFTWARE = "Klient: %s V%s"

#logging of conversations to file
LOG_HEADER = "Den här loggfilen är inte signerad och har inga kända exempelfall"
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
LOG_STARTED = "Loggning startad"
LOG_STOPPED = "Loggning stoppad"
LOG_DELETED = "Loggfiler har tagits bort"
LOG_IS_ACTIVATED = "Loggning till fil är aktiverad:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Loggning är stoppad men gamla loggfiler finns kvar:\n%s"


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
ABOUT_TITLE = "Om TorChat"
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
