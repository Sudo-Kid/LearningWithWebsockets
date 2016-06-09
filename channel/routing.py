from channels.routing import route, route_class
from chat import consumers

channel_routing = [
    route_class(consumers.ChatServer, path=r'^/chat/$'),
    # route("websocket.connect", consumers.ws_connect),
    # route("websocket.receive", consumers.ws_message),
    # route("websocket.disconnect", consumers.ws_disconnect),
]
