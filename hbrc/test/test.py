#coding=utf-8
#import __init__
import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import define,options

define("port", default=9090, type=int, help="rn on the given port")
# settings ={
#     "static_path" : os.path.join(os.path.dirname(__file__), "static"),
#     "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
#     "gzip" : True,
#     "debug" : True,
# }

'''
学习Tornado
'''
class MainHandler(tornado.web.RequestHandler):
    def get(self):  
        #self.write("Hello, Tornado!!!")
        name = self.get_argument("name", "default", strip=True)
        sex = self.get_argument("sex", "男", strip=True)
        print sex
        items = ["Item 1", "Item 2", name,sex]
        self.render("test.html",title="My python html templates",items=items)
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
    
    
    
    