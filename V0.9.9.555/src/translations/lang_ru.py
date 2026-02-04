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

LANGUAGE_CODE = "ru"
LANGUAGE_NAME = "Русский"
LANGUAGE_NAME_ENGLISH = "Russian"
TRANSLATOR_NAMES = ["SB14.org, RusInfo.cc"]

#buttons
BTN_CANCEL = "Отмена"
BTN_OK = "Да"
BTN_SAVE_AS = "Сохранить как..."
BTN_CLOSE = "Закрыть"

#status
ST_AVAILABLE = "В сети"
ST_AWAY = "Отсутствую"
ST_EXTENDED_AWAY = "Недоступен"
ST_OFFLINE = "Отключен"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Показать/Скрыть TorChat"
MTB_QUIT = "Выход"

#popup menu
MPOP_CHAT = "Чат..."
MPOP_SEND_FILE = "Послать файл..."
MPOP_EDIT_CONTACT = "Редактировать контакт..."
MPOP_DELETE_CONTACT = "Удалить контакт..."
MPOP_SHOW_OFFLINE_MESSAGES = "Показать очередь оффлайн сообщений"
MPOP_CLEAR_OFFLINE_MESSAGES = "Очистить очередь оффлайн сообщений"
MPOP_ACTIVATE_LOG = "Задействовать ведение лога"
MPOP_STOP_LOG = "Остановить ведение лога"
MPOP_DELETE_EXISTING_LOG = "Удалить существующий лог-файл"
MPOP_DELETE_AND_STOP_LOG = "Удалить лог и остановить логгирование"
MPOP_ADD_CONTACT = "Добавить контакт"
MPOP_ABOUT = "О программе TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Спросить %s..."
MPOP_SETTINGS = "Установки..."
MPOP_EDIT_MY_PROFILE = "Редактировать мой профиль..."

#chat window popup menu
CPOP_COPY = "Копировать"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Подтвердить удаление"
D_CONFIRM_DELETE_MESSAGE = "Действительно удалить этот контакт?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "Ведение лога TorChat активно"
D_LOG_WARNING_MESSAGE = "Запись лога в файл включена!\n\nLog File: %s\n\nПомните, что нужно удалить лог-файл, когда вы закончите отладку. Этот файл может содержать потенциально опасную важную информацию."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Порт занят"
D_WARN_USED_PORT_MESSAGE = "Какое-то приложение, скорее всего другой экземпляр TorChat, уже использует %s:%s. Вы должны создать еще один профиль с использованием других портов, чтобы запускать несколько экземпляров TorChat одновременно."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Непрочитанные сообщения"
D_WARN_UNREAD_MESSAGE = "У вас есть непрочитанные сообщения.\nОни будут утеряны навсегда!\n\nВы действительно хотите выйти из TorChat сейчас?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Контакт не в сети"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Это операция невозможна, если контакт не в сети"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Несколько файлов"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Вы не можете передавать несколько файлов одновременно. Посылайте файлы по одному или используйте архивы."

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Невозможно сохранить файл"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "Файл '%s' не может быть создан.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: Файл существует"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "Файл '%s' уже есть.\nПерезаписать?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Добавить контакт"
DEC_TITLE_EDIT = "Редактировать контакт"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Отображаемое имя"
DEC_INTRODUCTION = "Текст приветствия"
DEC_MSG_16_CHARACTERS = "Адрес должен быть длиной 16 or 56 символов, а не %i."
DEC_MSG_ONLY_ALPANUM = "Адрес может содержать только цифры и буквы в нижнем регистре"
DEC_MSG_ALREADY_ON_LIST = "%s уже в списке"

#dialog: edit my profile
DEP_TITLE = "Редактировать профиль"
DEP_NAME = "Имя"
DEP_TEXT = "Текст"
DEP_SET_AVATAR = "Установить аватар"
DEP_REMOVE_AVATAR = "Убрать аватар"
DEP_AVATAR_SELECT_PNG = "Выберите .PNG файл для аватара. Изображение будет отмасштабировано до 64*64, может содержать прозрачность"
DEP_PNG_FILES = "PNG файлы"
DEP_ALL_FILES = "Все файлы"
DEP_WARN_TITLE = "Выбор аватара невозможен"
DEP_WARN_IS_ALREADY = "Этот аватар уже используется"
DEP_WARN_MUST_BE_PNG = "Аватар должен быть .png файлом"

#file transfer window
DFT_FILE_OPEN_TITLE = "Послать файл %s"
DFT_FILE_SAVE_TITLE = "Принять файл от %s"
DFT_SEND = "Отправка %s\n %s\n%04.1f%% (%i из %i байт(-а))"
DFT_RECEIVE = "Получение %s\n от %s\n%04.1f%% (%i из %i байт(-а))"
DFT_WAITING = "ожидание подключения"
DFT_STARTING = "запуск передачи"
DFT_ABORTED = "передача прервана"
DFT_COMPLETE = "передача завершена"
DFT_ERROR = "ошибка"

#settings dialaog
DSET_TITLE = "Конфигурация TorChat"
DSET_NET_TITLE = "Сеть"
DSET_NET_ACTIVE = "активно"
DSET_NET_INACTIVE = "неактивно"
DSET_NET_TOR_ADDRESS = "Tor прокси адрес"
DSET_NET_TOR_SOCKS = "Socks порт"
DSET_NET_TOR_CONTROL = "Порт контроллера"
DSET_NET_OWN_HOSTNAME = "Собственный TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Интерфейс"
DSET_NET_LISTEN_PORT = "Порт"
DSET_GUI_TITLE = "Внешний вид"
DSET_GUI_LANGUAGE = "Язык"
DSET_GUI_OPEN_MAIN_HIDDEN = "Запускать со свернутым главным окном"
DSET_GUI_OPEN_CHAT_HIDDEN = "Не открывать автоматически новые окна"
DSET_GUI_NOTIFICATION_POPUP = "Всплывающие подсказки"
DSET_GUI_NOTIFICATION_METHOD = "Вид подсказок"
DSET_GUI_FLASH_WINDOW = "Мигать заголовком окна при получении нового сообщения"
DSET_MISC_TITLE = "Разное"
DSET_MISC_TEMP_IN_DATA = "Хранить временные файлы внутри папки с программой"
DSET_MISC_TEMP_CUSTOM_DIR = "Папка для временных файлов (оставьте пустой для папки по-умолчанию)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "отложенные сообщения ждут отправки"
NOTICE_DELAYED_MSG_SENT = "отложенные сообщения отправлены"
NOTICE_DELAYED = "отложено"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: сообщения в очереди"
MSG_OFFLINE_EMPTY = "(больше) нет сообщений в очереди для %s"
MSG_OFFLINE_QUEUED = "сообщения в очереди для %s:\n\n%s"

#buddy list mouse hover popup
BPOP_BUDDY_IS_OFFLINE = "Контакт не в сети"
BPOP_CONNECTED_AWAITING_RETURN_CONN = "Соединено, ожидаем взаимного соединения..."
BPOP_CLIENT_SOFTWARE = "Клиент: %s V%s"

#logging of conversations to file
LOG_HEADER = "Этот лог файл не подписан и не является неоспоримым доказательством"
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
LOG_STARTED = "Запись начата"
LOG_STOPPED = "Запись закончена"
LOG_DELETED = "Лог-файлы удалены"
LOG_IS_ACTIVATED = "Запись лог-файла включена:\n%s"
LOG_IS_STOPPED_OLD_LOG_FOUND = "Логгирование выключено, но старый лог-файл все еще существует:\n%s"


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
ABOUT_TITLE = "О программе TorChat"
ABOUT_TEXT = """TorChat %(version)s (svn: r%(svn)s)\
  %(copyright)s\
\
Среды запуска:\
  Python: %(python)s\
  wx: %(wx)s\
\
TorChat - свободное ПО: вы можете распространять его и/или \
изменять в соответствии с условиями лицензии GNU General Public \
License в том виде, в котором она опубликована Free Software Foundation, \
3 версии или (на ваш выбор) любой другой последующей \
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
