from flask import Flask, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)


@app.route('/get_time', )
def get_time():
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'time': time_now}

@app.route('/<filename>')
def file(filename):
    return app.send_static_file( filename)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8080)