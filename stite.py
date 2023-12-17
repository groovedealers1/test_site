from flask import render_template, Flask, request


app = Flask(__name__, template_folder='template')


@app.route('/test_site/', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('jump.html')
    else:
        return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)

