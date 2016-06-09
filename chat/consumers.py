from channels import Group
from channels.sessions import channel_session
from channels.generic.websockets import JsonWebsocketConsumer


class ChatServer(JsonWebsocketConsumer):
    strict_ordering = False
    slight_ordering = True

    def receive(self, content, **kwargs):
        print('receive', content)
        self.send(content)

    def send(self, content, **kwargs):
        print('send', content)
        super(JsonWebsocketConsumer, self).send(content)




# @channel_session
# def ws_connect(message):
#     print('ws_connect', message)
#     room = message.content['path'].strip("/")
#     message.channel_session['room'] = room
#     Group("chat-%s" % room).add(message.reply_channel)
#
# @channel_session
# def ws_message(message):
#     print('ws_message', message)
#     Group("chat-%s" % message.channel_session['room']).send({
#         "text": message['text'],
#     })
#
# @channel_session
# def ws_disconnect(message):
#     print('ws_disconnect', message)
#     Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
