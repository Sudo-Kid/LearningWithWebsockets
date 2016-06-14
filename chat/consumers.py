import json

from channels import Group
from channels.auth import http_session_user
from channels.auth import channel_session_user
from channels.auth import channel_session_user_from_http

from . import models


def select_group(request):
    group = request.content['path'].strip('/')
    if request.user.is_authenticated() and request.user.is_active:
        user_groups = models.UserChatGroup.objects.filter(
            user__user=request.user, group__name=group)
        if not user_groups:
            return ['auth-chat']
        return [user_groups[0].group.name]
    else:
        return ['no-auth-chat']

def add_user_to_message(message):
    user = message.user.get_username()
    content = json.loads(message['text'])
    content['user'] = user
    return json.dumps(content)

def new_user_in_channel(message, group):
    user = message.user.get_username()
    content = {
        'user': 'Bot' + '@' + group[0],
        'msgText': user + ' has joined the group ' + group[0]
    }
    return json.dumps(content)

@channel_session_user_from_http
def ws_connect(message):
    group = select_group(message)
    content = new_user_in_channel(message, group)
    Group("chat-%s" % group).add(message.reply_channel)
    Group("chat-%s" % group).send({
        "text": content,
    })

@channel_session_user
def ws_message(message):
    group = select_group(message)
    content = add_user_to_message(message)
    Group("chat-%s" % group).send({
        "text": content,
    })

@channel_session_user
def ws_disconnect(message):
    group = select_group(message)
    Group("chat-%s" % group).discard(
            message.reply_channel)
