from flask import render_template, Flask


app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)
