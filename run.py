from flask import Flask, render_template, send_from_directory
#from cachebuster import CacheBuster

app = Flask(__name__)
#config = {'extensions': ['.js', '.css', '.png', '.jpg'], 'hash_size': 5}

#cache_buster = CacheBuster(config=config)

#cache_buster.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<path:filename>', methods=['GET'])
def getpdf(filename):
    return send_from_directory(app.static_folder, f'{filename}.pdf')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
