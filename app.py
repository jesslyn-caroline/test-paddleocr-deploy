import os
from api import create_app

app = create_app()

if __name__ == "__main__":
    # app.run(port=8000, debug=True)
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)