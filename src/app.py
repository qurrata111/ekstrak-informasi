from flask import Flask, render_template, flash, request, url_for
from extract_information import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("app.html")

@app.route('/pranala')
def profile():
    return render_template("pranala.html")

@app.route('/send', methods=['POST'])
def send(sum=sum):
    
    if request.method == 'POST':
        folder = request.form['folderPath']
        keyword = request.form['keyword']
        algoritma = request.form['algoritma']
        infos = []
        if algoritma == 'kmp':
            try:
                infos = extract_information(folder, keyword, "kmp")
            except:
                infos = []
            sum = str(len(infos)) + " kalimat ditemukan"
            return render_template('app.html', sum=sum, items=infos)

        elif algoritma == 'bm':
            try:
                infos = extract_information(folder, keyword, "bm")
            except:
                infos = []
            sum = str(len(infos)) + " kalimat ditemukan"
            return render_template('app.html', sum=sum, items=infos)

        elif algoritma == 'regex':
            try:
                infos = extract_information(folder, keyword, "regex")
            except:
                infos = []
            sum = str(len(infos)) + " kalimat ditemukan"
            return render_template('app.html', sum=sum, items=infos)

if __name__ == "__main__":
    app.run(debug=true)