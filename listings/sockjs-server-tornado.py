from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

port = 9999

class EchoConnection(SockJSConnection):
    def on_message(self, msg):
        self.send(msg)

if __name__ == '__main__':
    router = SockJSRouter(EchoConnection, '/echo')

    app = web.Application(router.urls)
    app.listen(port)
    
    instance = ioloop.IOLoop.instance()
    instance.start()
    
    