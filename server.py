from flask import Flask ,render_template as rt,request as req,url_for
from qr import genarate_qr

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
            genarate_qr(t,c,bc)
            return rt("sqr.html")
    except Exception as e:
         print(e)    
         return "<center><h1>Something wonts wrong.</h1></center>"

app.run(port=3000,host="0.0.0.0",debug=True)