from lib.DetectPhising import DetectPhising
from lib.Wording import BAD_WORDING, GOOD_WORDING, PENCEGAHAN, PENANGANAN
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    link = ''
    if(request.method == 'POST'):
        link = request.form['link'] 

        load = str(DetectPhising(request.form['link']).predict())
        if(load == 'good'):
            return render_template("resultFound.html", result = GOOD_WORDING)
        elif (load == 'Bad'):
            return render_template("resultFound.html", result = BAD_WORDING)
        return render_template("index.html", pencegahan = PENCEGAHAN, penanganan=PENANGANAN, link=link, error=load)

    return render_template("index.html", pencegahan = PENCEGAHAN, penanganan=PENANGANAN, link=link)