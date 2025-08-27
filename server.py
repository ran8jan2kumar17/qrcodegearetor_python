from flask import Flask ,render_template as rt,request as req,url_for
from qr import genarate_qr
from pdf import gpdf1



app=Flask(__name__)

@app.get("/qr")
def qr():
    try:
        return rt("index.html")
    except Exception as e:
        print(e)
        return "<center><h1>Something wonts wrong.</h1></center>"

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
         return "<center><h1>Something wonts wrong.</h1></center>"
    
@app.get("/pdf")
def pdf():
     return rt("pdf.html")

@app.post("/gpdf")
def gpdf():
     try:
        files=req.files.getlist("images[]")
        cpdf=gpdf1([img.stream for img in files])
        return rt("spdf.html",pdfs=cpdf)
     except Exception as e:
           print(e)    
           return "<center><h1>Something wonts wrong.</h1></center>"

app.run(process.env.PORT)
#app.run(3000)