def init_index_route(app):
    @app.route("/")
    def index():
        return "API is running..."