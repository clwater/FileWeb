import tornado.web
import FileUtils
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        dirList , fileList , parentPath= FileUtils.listFile()
        self.render("template/main.html", title="ImageFile", dirList=dirList , fileList=fileList
                    ,parentPath = '')

class MainHandlerDir(tornado.web.RequestHandler):
    def get(self , child_path):
        dirList , fileList , parentPath= FileUtils.listFile(child_path)
        # self.redirect(imageurl)
        self.render("template/main.html", title=child_path, dirList=dirList , fileList=fileList
                    ,parentPath = parentPath)

class MainHandlerImage(tornado.web.RequestHandler):
    def get(self , child_path):
        print child_path
        self.redirect('http://23.83.255.85/' + child_path)


class MainHandlerSaveInfo(tornado.web.RequestHandler):
    def get(self):
        fileUrl = self.get_argument('fileUrl', '')


        parentPath = self.get_argument('parentPath', '')
        path = "/service/images"  + parentPath

        print fileUrl
        # tmp = os.popen('wget ' + fileUrl).readlines()
        # os.system('cd ' + path)
        text = path +  ' ' +fileUrl
        os.system('wget -P ' + text)
        # self.write('wget -P ' + text)
        # _path = str(path)
        # _path = _path.replace('/service/images/' ,'')
        self.write('wget -P ' + text)



application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/dir/(.*)", MainHandlerDir),
    (r"/image/(.*)", MainHandlerImage),
    (r"/save" , MainHandlerSaveInfo)

])

if __name__ == "__main__":
    port = 9001
    application.listen(port)
    print("run in" , port)
    tornado.ioloop.IOLoop.instance().start()

