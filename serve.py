import web

urls = (
  '/', 'index',
)


class index:
    def GET(self):
        return "Hello, world in rackspace-demo-2 application!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
