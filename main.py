import os
import helper
import flask

# application settings
name_application = "unutulmaz_notalar"
application = flask.Flask(name_application,
                          static_folder=os.path.abspath("unutulmaz-notalar/static/"),
                          static_url_path="/static/")


# api get composers list
@application.route("/api/getir/bestekarlar")
def api_get_composers():
    results = helper.Database.from_database("SELECT * FROM bestekarlar ORDER BY id ASC")
    results = {"bestekarlar": results}
    return flask.jsonify(results)


# api get forms list
@application.route("/api/getir/formlar")
def api_get_forms():
    results = helper.Database.from_database("SELECT * FROM formlar ORDER BY id ASC")
    results = {"formlar": results}
    return flask.jsonify(results)


# api get tunes list
@application.route("/api/getir/makamlar")
def api_get_tunes():
    results = helper.Database.from_database("SELECT * FROM makamlar ORDER BY id ASC")
    results = {"makamlar": results}
    return flask.jsonify(results)


# api get genres list
@application.route("/api/getir/turler")
def api_get_genres():
    results = helper.Database.from_database("SELECT * FROM turler ORDER BY id ASC")
    results = {"turler": results}
    return flask.jsonify(results)


# api get methods list
@application.route("/api/getir/usuller")
def api_get_methods():
    results = helper.Database.from_database("SELECT * FROM usuller ORDER BY id ASC")
    results = {"usuller": results}
    return flask.jsonify(results)


# api get authors list
@application.route("/api/getir/yazarlar")
def api_get_authors():
    results = helper.Database.from_database("SELECT * FROM yazarlar ORDER BY id ASC")
    results = {"yazarlar": results}
    return flask.jsonify(results)


# api get songs
@application.route("/api/getir/eserler/<int:song_id>")
def api_get_songs(song_id):
    results = helper.Database.from_database("SELECT * FROM eserler WHERE id={0}".format(song_id))
    results = {"eserler": results}
    return flask.jsonify(results)


# prevent data leakage
@application.errorhandler(404)
def page_not_found(error):
    return "yasak", 404


# api will run on port 80 with root privileges, else 8080 port
if __name__ == "__main__":

    # try to run the application
    try:

        # start the application on port 80, needs root privileges on linux
        application.run(debug=True, host="0.0.0.0", port=80, threaded=True)
        application.logger.info("Frontend Server Manager started using Werkzeug WSGI on port 80!")

    # permission error handling
    except PermissionError:

        # fall back to port 8080 if root privileges cannot be obtained
        application.logger.error("Cannot start Frontend Server Manager on port 80 because of the user privileges!")
        application.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
        application.logger.info("Frontend Server Manager started using Werkzeug WSGI on port 8080!")
