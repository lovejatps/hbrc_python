#coding=utf-8
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado.options import define,options


define("port", default=9090, type=int, help="rn on the given port")


'''
学习Tornado
'''
class MainHandler(tornado.web.RequestHandler):
    def get(self):  
        self.write("Hello, Tornado!!!")
        print "Respond to the request"

def make_app():
    return tornado.web.Application([
        (r"/hello\.html", MainHandler),
    ])

if __name__ == "__main__":
    print "start Tornado!"
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()