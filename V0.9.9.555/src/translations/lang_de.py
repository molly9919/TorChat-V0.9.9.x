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

LANGUAGE_CODE = "de"
LANGUAGE_NAME = "Deutsch"
LANGUAGE_NAME_ENGLISH = "German"
TRANSLATOR_NAMES = ["Bernd Kreuß"]

#buttons
BTN_CANCEL = "Abbrechen"
BTN_OK = "Ok"
BTN_SAVE_AS = "Speichern unter..."
BTN_CLOSE = "Schließen"

#status
ST_AVAILABLE = "Verfügbar"
ST_AWAY = "Abwesend"
ST_EXTENDED_AWAY = "Nicht verfügbar"
ST_OFFLINE = "Offline"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "TorChat anzeigen/verstecken"
MTB_QUIT = "Beenden"

#popup menu
MPOP_CHAT = "Nachricht schreiben..."
MPOP_SEND_FILE = "Datei senden..."
MPOP_EDIT_CONTACT = "Kontakt bearbeiten..."
MPOP_DELETE_CONTACT = "Kontakt löschen..."
MPOP_SHOW_OFFLINE_MESSAGES = "Nachrichten in Warteschlange anzeigen"
MPOP_CLEAR_OFFLINE_MESSAGES = "Nachrichten in Warteschlange löschen"
MPOP_ACTIVATE_LOG = "Aktiviere Mitschnitt in Datei"
MPOP_STOP_LOG = "Stoppe Mitschnitt"
MPOP_DELETE_EXISTING_LOG = "Lösche existierenden Mitschnitt"
MPOP_DELETE_AND_STOP_LOG = "Lösche Mitschnitt und stoppe Mitschneiden"
MPOP_ADD_CONTACT = "Kontakt hinzufügen..."
MPOP_ABOUT = "Über TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "%s fragen..."
MPOP_SETTINGS = "Einstellungen..."
MPOP_EDIT_MY_PROFILE = "Eigenes Profil bearbeiten..."
MPOP_COPY_ID_TO_CLIPBOARD="ID in die Zwischenablage kopieren"

#chat window popup menu
CPOP_COPY = "Kopieren"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Löschen bestätigen"
D_CONFIRM_DELETE_MESSAGE = "Soll dieser Kontakt wirklich gelöscht werden?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Logging ist aktiviert"
D_LOG_WARNING_MESSAGE = "Logging in Datei ist aktiviert!\n\nLogdatei: %s\n\nVergessen Sie nicht, die Logdatei nach Beendigung der Fehlersuche wieder zu löschen, da diese Datei vertrauliche Informationen enthalten könnte."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Port ist bereits belegt"
D_WARN_USED_PORT_MESSAGE = "Eine Anwendung, wahrscheinlich eine andere TorChat-Instanz, verwendet bereits den Port %s:%s. Sie müssen andere Profile mit anderen Ports verwenden, um TorChat mehrmals starten zu können."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Ungelesene Nachrichten"
D_WARN_UNREAD_MESSAGE = "Es liegen noch ungelesene Nachrichten vor. Diese würden unwiderruflich verloren gehen!\n\nMöchten sie TorChat dennoch jetzt beenden?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Buddy ist offline"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Diese Operation ist nicht möglich mit Offline-Buddies"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Mehrere Dateien"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Sie können nicht mit einer Operation mehrere Dateitransfers gleichzeitig auslösen. Starten Sie die Transfers einzeln, oder senden Sie eine Zip-Datei."

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Fehler beim Anlegen der Datei"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Die Datei '%s' konnte nicht erzeugt werden.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: Datei existiert bereits"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Die Datei '%s' existiert bereits.\nÜberschreiben?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Neuen Kontakt anlegen"
DEC_TITLE_EDIT = "Kontakt bearbeiten"
DEC_TORCHAT_ID = "TorChat-ID"
DEC_DISPLAY_NAME = "Angezeigter Name"
DEC_INTRODUCTION = "Kurze Vorstellung"
DEC_MSG_16_CHARACTERS = "Die Adresse muss genau 16 or 56 Zeichen lang sein, nicht %i."
DEC_MSG_ONLY_ALPANUM = "Die Adresse kann nur aus Ziffern und Kleinbuchstaben ohne Umlaute bestehen."
DEC_MSG_ALREADY_ON_LIST = "%s ist bereits auf Ihrer Liste."

# #dialog: edit my profile
DEP_TITLE = "Mein Profil bearbeiten"
DEP_NAME = "Name"
DEP_TEXT = "Text"
DEP_SET_AVATAR = "Bild wählen"
DEP_REMOVE_AVATAR = "Bild löschen"
DEP_AVATAR_SELECT_PNG = "Auswählen einer .png-Datei als Profilbild (wird auf 64*64 skaliert, darf Transparenz enthalten)"
DEP_PNG_FILES = "PNG-Dateien"
DEP_ALL_FILES = "Alle Dateien"
DEP_WARN_TITLE = "Auswahl nicht möglich"
DEP_WARN_IS_ALREADY = "Dies ist bereits ihr aktuelles Profilbild"
DEP_WARN_MUST_BE_PNG = "Bild muss eine .png-Datei sein"

#file transfer window
DFT_FILE_OPEN_TITLE = "Sende Datei an %s"
DFT_FILE_SAVE_TITLE = "Speichere Datei von %s"
DFT_SEND = "Sende %s\nan %s\n%04.1f%% (%i von %i Bytes)"
DFT_RECEIVE = "Empfange %s\nvon %s\n%04.1f%% (%i von %i Bytes)"
DFT_WAITING = "Warte auf Verbindung"
DFT_STARTING = "Starte Transfer"
DFT_ABORTED = "Transfer abgebrochen"
DFT_COMPLETE = "Transfer vollständig"
DFT_ERROR = "Fehler"

#settings dialaog
DSET_TITLE = "TorChat Konfiguration"
DSET_NET_TITLE = "Netzwerk"
DSET_NET_ACTIVE = "aktiv"
DSET_NET_INACTIVE = "inaktiv"
DSET_NET_TOR_ADDRESS = "Tor-Proxy Adresse"
DSET_NET_TOR_SOCKS = "Socks Port"
DSET_NET_TOR_CONTROL = "Control Port"
DSET_NET_OWN_HOSTNAME = "Eigene TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Binden an Adapter"
DSET_NET_LISTEN_PORT = "Binden an Port"
DSET_GUI_TITLE = "Benutzeroberfläche"
DSET_GUI_LANGUAGE = "Sprache"
DSET_GUI_OPEN_MAIN_HIDDEN = "Starte mit minimiertem Hauptfenster"
DSET_GUI_OPEN_CHAT_HIDDEN = "Öffne neue Fenster nicht automatisch"
DSET_GUI_NOTIFICATION_POPUP = "Benachrichtigungs-PopUp"
DSET_GUI_NOTIFICATION_METHOD = "Benachrichtigungsmethode"
DSET_GUI_FLASH_WINDOW = "Blinkender Fenstertitel bei neuer Nachricht"
DSET_MISC_TITLE = "Verschiedenes"
DSET_MISC_TEMP_IN_DATA = "Temporäre Dateien im Datenverzeichnis"
DSET_MISC_TEMP_CUSTOM_DIR = "Verzeichnis für temporäre Dateien (leer lassen für OS-Default)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "Verzögerte Nachrichten in der Sendewarteschlange"
NOTICE_DELAYED_MSG_SENT = "Verzögerte Nachrichten wurden gesendet"
NOTICE_DELAYED = "Verzögert"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: Ungesendete Nachrichten"
MSG_OFFLINE_EMPTY = "Es liegen keine ungesendeten Nachrichten (mehr) für %s vor"
MSG_OFFLINE_QUEUED = "Ungesendete Nachrichten für %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Buddy ist offline"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Verbunden, erwarte Rückverbindung..."
BPOP_CLIENT_SOFTWARE = "Client: %s V%s"

#logging of conversations to file
LOG_HEADER = "Dieser Mitschnitt ist nicht signiert und beinhaltet keine Beweiskraft"
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
LOG_STARTED = "Mitschneiden gestartet"
LOG_STOPPED = "Mitschneiden gestoppt"
LOG_DELETED = "Mitschnitt gelöscht"
LOG_IS_ACTIVATED = "Mitschneiden ist aktiviert:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Mitschneiden ist gestoppt aber ein alter Mitschnitt existiert noch:\n%s"


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
" ""

#about box
ABOUT_TITLE = "Über TorChat"
ABOUT_TEXT = """TorChat %(version)s (svn: r%(svn)s)\
  %(copyright)s\
\
Laufzeitumgebung:\
  Python: %(python)s\
  wx: %(wx)s\
\
Dieses Programm ist freie Software. Sie können es unter den \
Bedingungen der GNU General Public License, wie von der \
Free Software Foundation veröffentlicht, weitergeben und/oder \
modifizieren, entweder gemäß Version 3 der Lizenz oder \
(nach Ihrer Option) jeder späteren Version.\
\
Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, \
daß es Ihnen von Nutzen sein wird, aber OHNE IRGENDEINE GARANTIE, \
sogar ohne die implizite Garantie der MARKTREIFE oder der \
VERWENDBARKEIT FÜR EINEN BESTIMMTEN ZWECK. Details finden Sie \
in der GNU General Public License.\
\
Sie sollten ein Exemplar der GNU General Public License zusammen \
mit diesem Programm erhalten haben. Falls nicht, siehe \
<http://www.gnu.org/licenses/>.\
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
