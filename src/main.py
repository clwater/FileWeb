import tornado.web
import FileUtils

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        dirList , fileList , parentPath= FileUtils.listFile()
        self.render("template/main.html", title="ImageFile", dirList=dirList , fileList=fileList
                    ,parentPath = '')

class MainHandlerDir(tornado.web.RequestHandler):
    def get(self , child_path):
        dirList , fileList , parentPath= FileUtils.listFile(child_path)
        self.render("template/main.html", title=child_path, dirList=dirList , fileList=fileList
                    ,parentPath = parentPath)



application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/child/(.*)", MainHandlerDir),

])

if __name__ == "__main__":
    port = 9001
    application.listen(port)
    print("run in" , port)
    tornado.ioloop.IOLoop.instance().start()

