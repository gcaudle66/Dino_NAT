from webui import app
import os
flask_debug = os.environ['FLASK_DEBUG'] = '1'
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
