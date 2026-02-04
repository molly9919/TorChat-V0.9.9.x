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

LANGUAGE_CODE = "pt"
LANGUAGE_NAME = "Português"
LANGUAGE_NAME_ENGLISH = "Portuguese"
TRANSLATOR_NAMES = ["Marc Young mycbx@lavabit.com"]

#buttons
BTN_CANCEL = "Cancelar"
BTN_OK = "Ok"
BTN_SAVE_AS = "Salvar como..."
BTN_CLOSE = "Fechar"

#status
ST_AVAILABLE = "Disponível"
ST_AWAY = "Longe"
ST_EXTENDED_AWAY = "Longe por mais tempo"
ST_OFFLINE = "Desligado"

#TaskbarMenu
MTB_SHOW_HIDE_TORCHAT = "Mostrar/Esconder o TorChat"
MTB_QUIT = "Sair"

#popup menu
MPOP_CHAT = "Bate-papo..."
MPOP_SEND_FILE = "Enviar arquivo..."
MPOP_EDIT_CONTACT = "Editar contato..."
MPOP_DELETE_CONTACT = "Deletar contato..."
MPOP_SHOW_OFFLINE_MESSAGES = "Mostrar mensagens offline enfileiradas"
MPOP_CLEAR_OFFLINE_MESSAGES = "Limpar mensagens offline enfileiradas"
# MPOP_ACTIVATE_LOG = u"Activate logging to file"
# MPOP_STOP_LOG = u"Stop logging"
# MPOP_DELETE_EXISTING_LOG = u"Delete existing log file"
# MPOP_DELETE_AND_STOP_LOG = u"Delete log and stop logging"
MPOP_ADD_CONTACT = "Adicionar contato..."
MPOP_ABOUT = "Sobre o TorChat"
MPOP_TIPJAR = "TorChat Bitcoin Tip-Jar"
MPOP_ASK_AUTHOR = "Perguntar ao %s..."
MPOP_SETTINGS = "Configurações..."
# MPOP_EDIT_MY_PROFILE = u"Edit my profile..."

#chat window popup menu
CPOP_COPY = "Copiar"

#confirm delete message box
D_CONFIRM_DELETE_TITLE = "Confirmar exclusão"
D_CONFIRM_DELETE_MESSAGE = "Realmente deletar este contato?\n(%s %s)"

#warning about log
D_LOG_WARNING_TITLE = "TorChat: O Arquivo de registros(Log) está ativo"
D_LOG_WARNING_MESSAGE = "Arquivo de registros(Log) ativado!\n\nArquivo de registros: %s\n\nLembrar de deletar o arquivo de registros se você terminou de eliminar os erros(debugging) porque o arquivo de registros pode conter informações sensíveis."

#warning about used port
D_WARN_USED_PORT_TITLE = "TorChat: Porta em uso "
D_WARN_USED_PORT_MESSAGE = "Algo, provavelmente outra intância do TorChat já está escutando pela porta %s:%s. Você deve criar outro perfil usando diferentes portas para ser possível iniciar o TorChat uma segunda vez."

# #warning about unread messages
D_WARN_UNREAD_TITLE = "TorChat: Mensagens não lidas"
D_WARN_UNREAD_MESSAGE = "Essas mensagens não foram lidas.\nElas serão perdidas para sempre!\n\nVocê realmente quer sair do TorChat agora?"

#warning about offline buddy
D_WARN_BUDDY_OFFLINE_TITLE = "TorChat: Esse amigo está desligado"
D_WARN_BUDDY_OFFLINE_MESSAGE = "Essa operação não é possível com amigos desligados"

#warning about multiple files
D_WARN_FILE_ONLY_ONE_TITLE = "TorChat: Múltiplos arquivos"
D_WARN_FILE_ONLY_ONE_MESSAGE = "Você não pode iniciar a tranferência de arquivos múltiplos usando uma única operação. Inicie transferências uma de cada vez ou ao invés disso envie um arquivo zip."

#warning about file save error
D_WARN_FILE_SAVE_ERROR_TITLE = "TorChat: Erro ao salvar arquivo"
D_WARN_FILE_SAVE_ERROR_MESSAGE = "O arquivo '%s' não pôde ser criado.\n\n%s"

#warning about file already exists
D_WARN_FILE_ALREADY_EXISTS_TITLE = "TorChat: O arquivo existe"
D_WARN_FILE_ALREADY_EXISTS_MESSAGE = "O arquivo '%s' já existe.\nSobrescrevê-lo?"

#dialog: add/edit contact
DEC_TITLE_ADD = "Adicionar novo contato"
DEC_TITLE_EDIT = "Editar contato"
DEC_TORCHAT_ID = "TorChat ID"
DEC_DISPLAY_NAME = "Nome aparente(display name)"
DEC_INTRODUCTION = "Introdução"
DEC_MSG_16_CHARACTERS = "O endereço deve ter 16 or 56 caracteres, não %i."
DEC_MSG_ONLY_ALPANUM = "O endereço deve conter apenas números e letras minúsculas"
DEC_MSG_ALREADY_ON_LIST = "%s já está na sua lista"

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
DFT_FILE_OPEN_TITLE = "Enviar arquivo para %s"
DFT_FILE_SAVE_TITLE = "Salvar arquivo de %s"
DFT_SEND = "Enviando %s\npara %s\n%04.1f%% (%i de %i bytes)"
DFT_RECEIVE = "Recebendo %s\nde %s\n%04.1f%% (%i de %i bytes)"
# DFT_WAITING = u"waiting for connection"
# DFT_STARTING = u"starting transfer"
# DFT_ABORTED = u"transfer aborted"
# DFT_COMPLETE = u"transfer complete"
# DFT_ERROR = u"error"

#settings dialaog
DSET_TITLE = "Configuração do TorChat"
DSET_NET_TITLE = "Rede"
DSET_NET_ACTIVE = "ativo"
DSET_NET_INACTIVE = "inativo"
DSET_NET_TOR_ADDRESS = "Endereço de proxy do Tor"
DSET_NET_TOR_SOCKS = "Porta Socks"
DSET_NET_TOR_CONTROL = "Porta de Controle"
DSET_NET_OWN_HOSTNAME = "Meu próprio TorChat-ID"
DSET_NET_LISTEN_INTERFACE = "Interface de escuta"
DSET_NET_LISTEN_PORT = "Porta de Escuta"
DSET_GUI_TITLE = "Interface do usuário"
DSET_GUI_LANGUAGE = "Língua"
DSET_GUI_OPEN_MAIN_HIDDEN = "Iniciar com a janela principal minimizada"
DSET_GUI_OPEN_CHAT_HIDDEN = "Não abrir novas janelas automáticamente"
DSET_GUI_NOTIFICATION_POPUP = "Pop-up de notificação"
# DSET_GUI_NOTIFICATION_METHOD = u"Notification method"
DSET_GUI_FLASH_WINDOW = "Janela rápida quando chegar uma nova mensagem"
DSET_MISC_TITLE = "Variado"
DSET_MISC_TEMP_IN_DATA = "Armazenar arquivos temporários no diretório de dados"
DSET_MISC_TEMP_CUSTOM_DIR = "Diretório temporário (deixar vazio para OS-padrão)"

#notices in the chat window (those in square brackets)
NOTICE_DELAYED_MSG_WAITING = "mensagens atrazadas estão esperando para serem enviadas"
NOTICE_DELAYED_MSG_SENT = "as mensagens atrazadas foram enviadas"
NOTICE_DELAYED = "atrazada"

#messagebox for offline messages
MSG_OFFLINE_TITLE = "TorChat: mensagens não lidas"
MSG_OFFLINE_EMPTY = "essas não são (mais) mensagens enfileiradas para %s"
MSG_OFFLINE_QUEUED = "mensagens enfileiradas offline para %s:\n\n%s"

# #buddy list mouse hover popup
# BPOP_BUDDY_IS_OFFLINE = u"Buddy is offline"
# BPOP_CONNECTED_AWAITING_RETURN_CONN = u"Connected, awaiting return connection..."
# BPOP_CLIENT_SOFTWARE = u"Client: %s V%s"

# #logging of conversations to file
# LOG_HEADER = u"This log file is not digitally signed and has no cogency of proof of anything."
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
ABOUT_TITLE = "Sobre o TorChat"
ABOUT_TEXT = """TorChat %(version)s (svn: r%(svn)s)\
  %(copyright)s\
\
Ambiente Runtime:\
  Python: %(python)s\
  wx: %(wx)s\
\
O TorChat é um software livre: você pode redistribuí-lo e/ou \
modificá-lo sob os termos da GNU General Public \
License publicada pela Free Software Foundation, \
usando qualquer versão 3 dessa licença, ou (conforme sua opção) \
qualquer versão anterior.\
\
O TorChat é distribuído na esperança de que ele seja útil, \
mas SEM QUALQUER GARANTIA; sem que isso implique \
em garantia de MERCANTIBILIDADE ou APTIDÃO PARA PROPÓSITOS PARTICULARES. \
Veja a GNU General Public License para mais detalhes.\
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
