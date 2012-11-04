import flask

app = flask.Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

import views.main

main = views.main.Main.as_view('main')
app.add_url_rule('/', view_func=main)

app.secret_key = 'top_secret'

if __name__ == "__main__":
    app.run(debug=True)