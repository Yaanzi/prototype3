from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    script_path = 'os.py'
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    output = result.stdout
    return render_template('result.html', output=output)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/support')
def support():
    return render_template('support.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)