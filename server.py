from flask import Flask ,render_template as rt,request as req,url_for
from qr import genarate_qr
from pdf import gpdf1
import os
from werkzeug.exceptions import RequestEntityTooLarge



app=Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.get("/qr")
def qr():
    try:
        return rt("index.html")
    except Exception as e:
        print(e)
        return "<center><h1>Something wants wrong. Please Try Again.</h1></center>"

@app.post("/gqr")
def gqr():
    try:
            t=req.form.get("qrtext")
            c=req.form.get("qrc")
            bc=req.form.get("qrbg")
            qr=genarate_qr(t,c,bc)
            return rt("sqr.html",f=qr)
    except Exception as e:
         print(e)    
         return "<center><h1>Something wants wrong. Please Try Again.</h1></center>"
    
@app.get("/pdf")
def pdf():
     return rt("pdf.html")

@app.post("/gpdf")
def gpdf():
     try:
        files=req.files.getlist("images[]")
        cpdf=gpdf1([img.stream for img in files])
        if cpdf == None:
             return "<h1>It Only Accept .PNG images. Please Try Again.</h1>"
        else:
             return rt("spdf.html",pdfs=cpdf)
     except Exception as e:
           print(e)    
           return "<center><h1>Something wnts wrong. Please Try Again.OR File too large! Max upload size is 2MB.</h1></center>"
     

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    return "<h1>File too large! Max upload size is 2MB.</h1>", 413



port = int(os.environ.get("PORT", 3000))
app.run(host="0.0.0.0", port=port)
