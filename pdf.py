import base64
import io
import img2pdf
from PIL import Image

def gpdf1(images=None):
    """
    Convert a list of images (any format) to a PDF and return base64 string.
    images: list of file-like objects (e.g., Flask FileStorage)
    """
    if not images:
        return None

    png_streams = []

    for img_file in images:
        img_file.seek(0)  # Reset pointer
        img = Image.open(img_file)

        # If image is already PNG or JPEG, pass it directly
        if img.format in "PNG":
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")  # Convert JPEG also to PNG for consistency
            buffer.seek(0)
            png_streams.append(buffer)
        else:
            # Convert any other format to PNG in memory
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            png_streams.append(buffer)

    # img2pdf expects file-like objects that support read()
    pdf_bytes = img2pdf.convert(png_streams)

    # Convert PDF bytes to base64
    pdf_base64 = base64.b64encode(pdf_bytes).decode()
    return pdf_base64
