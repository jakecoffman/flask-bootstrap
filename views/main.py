import flask
import flask.views

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')