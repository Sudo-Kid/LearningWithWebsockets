from channels import Group
from channels.auth import http_session_user
from channels.auth import channel_session_user
from channels.auth import channel_session_user_from_http


@channel_session_user_from_http
def ws_connect(message):
    Group("chat-%s" % message.user.username[0]).add(message.reply_channel)

@channel_session_user
def ws_message(message):
    Group("chat-%s" % message.user.username[0]).send({
        "text": message['text'],
    })

@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.user.username[0]).discard(
            message.reply_channel)
