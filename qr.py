import qrcode
from PIL import Image
import os

def genarate_qr(t,c,bc):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    
    if os.path.exists("static/newqr.py"):
        os.remove("static/newqr.py")

    qr.add_data(t)
    qr.make(fit=True)

    qr_img=qr.make_image(fill_color=c,back_color=bc)

    qr_img.save("static/newqr.png")



