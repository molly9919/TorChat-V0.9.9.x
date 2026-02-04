# -*- coding: UTF-8 -*-

##############################################################################
#                                                                            #
# Copyright (c) 2007-2013 Bernd Kreuss <prof7bit@gmail.com>                  #
#   Modifications and updates Copyright                                      #
# Copyright (c) 2014-2019  M. Weigand       <doctortor@use.startmail.com>    #
#                                                                            #
# Translation file for TorChat                                               #
#                                                                            #
##############################################################################

LANGUAGE_CODE = "en"
LANGUAGE_NAME = "English"
LANGUAGE_NAME_ENGLISH = "English"
TRANSLATOR_NAMES = []

#buttons
BTN_CANCEL = "Cancel"
BTN_OK = "Ok"
BTN_SAVE_AS = "Save as..."
BTN_CLOSE = "Close"

#status
ST_AVAILABLE = "Available"
ST_AWAY = "Away"
ST_EXTENDED_AWAY = "Extended away"
ST_OFFLINE = "Offline"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Show/Hide TorChat"
MTB_QUIT = "Quit"

#popup menu
MPOP_CHAT = "Chat..."
MPOP_SEND_FILE = "Send file..."
MPOP_EDIT_CONTACT = "Edit contact..."
MPOP_DELETE_CONTACT = "Delete contact..."
MPOP_SHOW_OFFLINE_MESSAGES = "Show queued offline messages"
MPOP_CLEAR_OFFLINE_MESSAGES = "Clear queued offline messages"
MPOP_ACTIVATE_LOG = "Activate logging to file"
MPOP_STOP_LOG = "Stop logging"
MPOP_DELETE_EXISTING_LOG = "Delete existing log file"
MPOP_DELETE_AND_STOP_LOG = "Delete log and stop logging"
MPOP_ADD_CONTACT = "Add contact..."
MPOP_ABOUT = "About TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Ask %s..."
MPOP_SETTINGS = "Settings..."
MPOP_EDIT_MY_PROFILE = "Edit my profile..."
MPOP_COPY_ID_TO_CLIPBOARD="Copy ID to clipboard"

#chat window popup menu
CPOP_COPY = "Copy to Clipboard"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Confirm deletion"
D_CONFIRM_DELETE_MESSAGE = "Really delete this contact?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Logging is active"
D_LOG_WARNING_MESSAGE = "Logging to file is activated!\n\nLog File: %s\n\nRemember to delete the log file if you have finished debugging because the log file may contain sensitive information."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Port already in use"
D_WARN_USED_PORT_MESSAGE = "Something, probably another TorChat instance, is already listening at %s:%s. You must create another profile using different ports to be able to start TorChat a second time."

#warnig about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Unread messages"
D_WARN_UNREAD_MESSAGE = "There are unread messages.\nThey will be lost forever!\n\nDo you really want to exit TorChat now?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Buddy is offline"
D_WARN_BUDDY_OFFLINE_MESSAGE = "This operation is not possible with offline buddies"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Multiple files"
D_WARN_FILE_ONLY_ONE_MESSAGE = "You may not start multiple file transfers with one operation. Start the transfers individually or send a zip-file instead"

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Error saving file"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "The file '%s' could not be created.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: File exists"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "The file '%s' already exists.\nOverwrite it?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Add new contact"
DEC_TITLE_EDIT = "Edit contact"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Display name"
DEC_INTRODUCTION = "Introduction"
DEC_MSG_16_CHARACTERS = "The address must be 16 or 56 characters long, not %i."
DEC_MSG_ONLY_ALPANUM = "The address must only contain numbers and lowercase letters"
DEC_MSG_ALREADY_ON_LIST = "%s is already on your list"

#dialog: edit my profile
DEP_TITLE = "Edit my profile"
DEP_NAME = "Name"
DEP_TEXT = "Text"
DEP_SET_AVATAR = "Set Avatar"
DEP_REMOVE_AVATAR = "Remove Avatar"
DEP_AVATAR_SELECT_PNG = "Select .PNG file to use as your avatar (will be scaled to 64*64, may contain transparency)"
DEP_PNG_FILES = "PNG files"
DEP_ALL_FILES = "All files"
DEP_WARN_TITLE = "Avatar selection not possible"
DEP_WARN_IS_ALREADY = "This is already the current avatar"
DEP_WARN_MUST_BE_PNG = "The avatar must be a .png file"

#file transfer window
DFT_FILE_OPEN_TITLE = "Send file to %s"
DFT_FILE_SAVE_TITLE = "Save file from %s"
DFT_SEND = "Sending %s\nto %s\n%04.1f%% (%i of %i bytes)"
DFT_RECEIVE = "Receiving %s\nfrom %s\n%04.1f%% (%i of %i bytes)"
DFT_WAITING = "waiting for connection"
DFT_STARTING = "starting transfer"
DFT_ABORTED = "transfer aborted"
DFT_COMPLETE = "transfer complete"
DFT_ERROR = "error"

#settings dialaog
DSET_TITLE = "TorChat configuration"
DSET_NET_TITLE = "Network"
DSET_NET_ACTIVE = "active"
DSET_NET_INACTIVE = "inactive"
DSET_NET_TOR_ADDRESS = "Tor proxy address"
DSET_NET_TOR_SOCKS = "Socks port"
DSET_NET_TOR_CONTROL = "Control port"
DSET_NET_OWN_HOSTNAME = "Own TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Listen interface"
DSET_NET_LISTEN_PORT = "Listen port"
DSET_GUI_TITLE = "User interface"
DSET_GUI_LANGUAGE = "Language"
DSET_GUI_OPEN_MAIN_HIDDEN = "Start with minimized main window"
DSET_GUI_OPEN_CHAT_HIDDEN = "Don't automatically open new windows"
DSET_GUI_NOTIFICATION_POPUP = "Notification pop-up"
DSET_GUI_NOTIFICATION_METHOD = "Notification method"
DSET_GUI_FLASH_WINDOW = "Flash window title on new message"
DSET_MISC_TITLE = "Misc"
DSET_MISC_TEMP_IN_DATA = "Store temporary files inside data directory"
DSET_MISC_TEMP_CUSTOM_DIR = "Temporary directory (leave empty for OS-default)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "delayed messages waiting to be sent"
NOTICE_DELAYED_MSG_SENT = "delayed messages have been sent"
NOTICE_DELAYED = "delayed"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: queued messages"
MSG_OFFLINE_EMPTY = "there are no (more) queued messages for %s"
MSG_OFFLINE_QUEUED = "queued offline messages for %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Buddy is offline"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Connected, awaiting return connection..."
BPOP_CLIENT_SOFTWARE = "Client: %s V%s"

#logging of conversations to file
LOG_HEADER = "This log file is not digitally signed and has no cogency of proof of anything."
LOG_HEADER1 = "Note to the criminal & corrupt agents of law enforcement:"
LOG_HEADER2 = "(A fake chat log file is easily created by setting computer time to a suitable creation date"
LOG_HEADER3 = "- then creating the file with a text editor, thereby establishing a file creation time. Next,"
LOG_HEADER4 = "- fill the file with the evidence / fake conversations / incriminating evidence. When satisfied,"
LOG_HEADER5 = "- set the computer time to a suitable / incriminating last conversation time and make a small"
LOG_HEADER6 = "- change to the log file and save. Thus establishing the modification date. You now have a"
LOG_HEADER7 = "- chat log file, completely acceptable to the US DOJ & FBI as the evidence to convict."
LOG_HEADER8 = "- It is so easy to be a corrupt government agent, creating evidence & putting people away!)"
LOG_HEADERQ1 = " ""The way to have safe government is not to trust it all to the one, but to divide it "
LOG_HEADERQ2 = "among the many, distributing to everyone exactly the functions in which he is competent..."
LOG_HEADERQ3 = "To let the National Government be entrusted with the defense of the nation, and its foreign "
LOG_HEADERQ4 = "and federal relations... The State Governments with the Civil Rights, Laws, Police and "
LOG_HEADERQ5 = "administration of what concerns the State generally. The Counties with the local concerns, "
LOG_HEADERQ6 = "and each ward direct the interests within itself. It is by dividing and subdividing these "
LOG_HEADERQ7 = "Republics from the great national one down through all its subordinations until it ends in "
LOG_HEADERQ8 = "the administration of everyman's farm by himself, by placing under everyone what his own eye "
LOG_HEADERQ9 = "may superintend, that all will be done for the best."" -- Thomas Jefferson"
LOG_STARTED = "Logging started"
LOG_STOPPED = "Logging stopped"
LOG_DELETED = "Log files have been deleted"
LOG_IS_ACTIVATED = "Logging to file is activated:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Logging is stopped but old log file still exists:\n%s"

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
"""

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
any later version.

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
