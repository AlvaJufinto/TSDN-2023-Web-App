from lib.DetectPhising import DetectPhising
from lib.Wording import GOOD_SITE, BAD_SITE, PENCEGAHAN, PENANGANAN, PHOTOS_URL
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    link = ''
    if(request.method == 'POST'):
        link = request.form['link'] 

        load = str(DetectPhising(request.form['link']).predict())
        if(load == 'good'):
            return render_template("resultFound.html", result = GOOD_SITE)
        elif (load == 'bad'):
            return render_template("resultFound.html", result = BAD_SITE)
        return render_template("index.html", pencegahan = PENCEGAHAN, penanganan=PENANGANAN, photos=PHOTOS_URL, link=link, error=load)

    return render_template("index.html", pencegahan = PENCEGAHAN, penanganan=PENANGANAN, photos=PHOTOS_URL, link=link)