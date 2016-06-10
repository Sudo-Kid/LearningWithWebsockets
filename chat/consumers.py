import json

from channels import Group
from channels.auth import http_session_user
from channels.auth import channel_session_user
from channels.auth import channel_session_user_from_http


def select_room(message):
    if message.user.is_authenticated() and message.user.is_active:
        return ['auth-chat']
    else:
        return ['no-auth-chat']

def add_user_to_message(message):
    user = message.user.get_username()
    content = json.loads(message['text'])
    content['user'] = user
    return json.dumps(content)

def new_user_in_channel(message):
    user = message.user.get_username()
    content = {
        'user': 'Bot',
        'msgText': user + ' has joined the channel'
    }
    return json.dumps(content)

@channel_session_user_from_http
def ws_connect(message):
    room = select_room(message)
    content = new_user_in_channel(message)
    Group("chat-%s" % room).add(message.reply_channel)
    Group("chat-%s" % room).send({
        "text": content,
    })

@channel_session_user
def ws_message(message):
    room = select_room(message)
    content = add_user_to_message(message)
    Group("chat-%s" % room).send({
        "text": content,
    })

@channel_session_user
def ws_disconnect(message):
    room = select_room(message)
    Group("chat-%s" % room).discard(
            message.reply_channel)
