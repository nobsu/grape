# -*- coding: utf-8 -*-


from grape.web import create_app

app = create_app()
if __name__ == '__main__':
#     app.run()
    app.run(port=8080)