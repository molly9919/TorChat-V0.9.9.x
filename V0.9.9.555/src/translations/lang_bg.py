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

LANGUAGE_CODE = "bg"
LANGUAGE_NAME = "Български"
LANGUAGE_NAME_ENGLISH = "Bulgarian"
TRANSLATOR_NAMES = ["Asen Anastassov smaragdus@gmail.com"]

#buttons
BTN_CANCEL = "Отмяна"
BTN_OK = "Добре"
BTN_SAVE_AS = "Запазване като..."
BTN_CLOSE = "Затваряне"

#status
ST_AVAILABLE = "на линия"
ST_AWAY = "отсъстващ"
ST_EXTENDED_AWAY = "недостъпен"
ST_OFFLINE = "извън линия"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Показване/Скриване на TorChat"
MTB_QUIT = "Напускане"

#popup menu
MPOP_CHAT = "Чат..."
MPOP_SEND_FILE = "Изпращане на файл..."
MPOP_EDIT_CONTACT = "Редактиране на контакт..."
MPOP_DELETE_CONTACT = "Изтриване на контакт..."
MPOP_SHOW_OFFLINE_MESSAGES = "Показване на неизпратени офлайн съобщения"
MPOP_CLEAR_OFFLINE_MESSAGES = "Премахване на неизпратени офлайн съобщения"
# MPOP_ACTIVATE_LOG = u"Activate logging to file"
# MPOP_STOP_LOG = u"Stop logging"
# MPOP_DELETE_EXISTING_LOG = u"Delete existing log file"
# MPOP_DELETE_AND_STOP_LOG = u"Delete log and stop logging"
MPOP_ADD_CONTACT = "Прибавяне на контакт..."
MPOP_ABOUT = "Относно TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Попитайте %s..."
MPOP_SETTINGS = "Настройки..."
# MPOP_EDIT_MY_PROFILE = u"Edit my profile..."

#chat window popup menu
CPOP_COPY = "Копиране"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Потвърждаване на изтриване"
D_CONFIRM_DELETE_MESSAGE = "Наистина ли желаете да изтриете този контакт?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: Дневник активен"
D_LOG_WARNING_MESSAGE = "Запазване на дневник във файл активирано!\n\nLog File: %s\n\nНе забравяйте да изтриете файла с дневника след като приключите анализа на грешките, защото той може да съдържа поверителна информация."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Портът е вече в употреба"
D_WARN_USED_PORT_MESSAGE = "Нещо, вероятно второ копие на TorChat вече ползва %s:%s. Трябва да създадете нов профил ползващ други портове, за да  можете да стартирате второ копие на TorChat."

#warnig about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Непрочетени съобщения"
D_WARN_UNREAD_MESSAGE = "Има непрочетени съобщения.\nТе ще бъдат загубени безвъзвратно!\n\nНаистина ли желаете да напуснете TorChat сега?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Контактът не е на линия"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Тази операция не е възможна с контакти извън линия"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Няколко файла"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Не можете да изпратите няколко файла едновременно. Изпратете ги поотделно или като zip-файл."

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Грешка при запазване на файла"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Файлът '%s' не може да бъде създаден.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: Файлът съществува"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Файлът '%s' вече съществува.\nЖелаете ли да го замените?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Добавяне на нов контакт"
DEC_TITLE_EDIT = "Редактиране на контакт"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Име"
DEC_INTRODUCTION = "Въведение"
DEC_MSG_16_CHARACTERS = "Адресът трябва да се състои от 16 or 56 символа, не %i."
DEC_MSG_ONLY_ALPANUM = "Адресът трябва да се състои единствено от цифри и малки букви."
DEC_MSG_ALREADY_ON_LIST = "%s е вече във вашия списък"

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
DFT_FILE_OPEN_TITLE = "Изпращане на файл до %s"
DFT_FILE_SAVE_TITLE = "Запазване на файл от %s"
DFT_SEND = "Изпращане на %s\nto %s\n%04.1f%% (%i of %i байта)"
DFT_RECEIVE = "Получаване на %s\nfrom %s\n%04.1f%% (%i of %i байта)"
# DFT_WAITING = u"waiting for connection"
# DFT_STARTING = u"starting transfer"
# DFT_ABORTED = u"transfer aborted"
# DFT_COMPLETE = u"transfer complete"
# DFT_ERROR = u"error"

#settings dialaog
DSET_TITLE = "Конфигуриране на TorChat"
DSET_NET_TITLE = "Мрежа"
DSET_NET_ACTIVE = "Активна"
DSET_NET_INACTIVE = "Неактивна"
DSET_NET_TOR_ADDRESS = "Адрес на Tor прокси"
DSET_NET_TOR_SOCKS = "Socks порт"
DSET_NET_TOR_CONTROL = "Контролен порт"
DSET_NET_OWN_HOSTNAME = "Собствено TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Интерфейс за прослушване"
DSET_NET_LISTEN_PORT = "Порт за прослушване"
DSET_GUI_TITLE = "Потребителски интерфейс"
DSET_GUI_LANGUAGE = "Език"
DSET_GUI_OPEN_MAIN_HIDDEN = "Стартиране с минимизиран главен прозорец"
DSET_GUI_OPEN_CHAT_HIDDEN = "Нови прозорци не се отварят автоматично"
DSET_GUI_NOTIFICATION_POPUP = "Изскачащо известяване"
# DSET_GUI_NOTIFICATION_METHOD = u"Notification method"
DSET_GUI_FLASH_WINDOW = "Пробягващ прозорец при получаване на ново съобщение"
DSET_MISC_TITLE = "Разни"
DSET_MISC_TEMP_IN_DATA = "Съхраняване на временни файлове в директория с данни"
DSET_MISC_TEMP_CUSTOM_DIR = "Временна директория (празна по подразбиране за ОС)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "забавени съобщения, чакащи да бъдат изпратени"
NOTICE_DELAYED_MSG_SENT = "забавени съобщения изпратени"
NOTICE_DELAYED = "забавени"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: съобщения на опашка"
MSG_OFFLINE_EMPTY = "няма (повече) съобщения на опашка за %s"
MSG_OFFLINE_QUEUED = "офлайн съобщения на опашка за %s:\n\n%s"

# #buddy list mouse hover popup
# BPOP_BUDDY_IS_OFFLINE = u"Buddy is offline"
# BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Connected, awaiting return connection..."
# BPOP_CLIENT_SOFTWARE = u"Client: %s %s"

# #logging of conversations to file
LOG_HEADER = "This log file is not digitally signed and has no cogency of proof of anything."
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
# LOG_HEADERQ9 = u"may superintend, that all will be done for the best." -- Thomas Jefferson"
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
TorChat се разпространява с надеждата, че ще бъде от полза, \
но БЕЗ НИКАКВИ ГАРАНЦИИ; без дори косвена \
гаранция за ПРИГОДНОСТ ЗА ОПРЕДЕЛЕНА ЦЕЛ. \
Вижте GNU General Public License за повече подробности.
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
