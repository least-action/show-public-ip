from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web


class IpReturnHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write(self.request.remote_ip)


def make_app():
    return tornado.web.Application([
        (r"/", IpReturnHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
