from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from flask import render_template

import io

app = Flask(__name__)

@app.route("/meme", methods=["POST"])
def meme():
    top = request.form.get("top", "")
    bottom = request.form.get("bottom", "")
    image = Image.open(request.files["image"])
    draw = ImageDraw.Draw(image)
    
        
    # Get image dimensions
    width, height = image.size

    # Calculate text size
    print("top:", top, "bottom:", bottom)
    print("Image size:", width, height)
    text_size = width * 0.1
    font = ImageFont.load_default(text_size)

    # Center text horizontally, place top near the top (10% of height), bottom near the bottom (85%)
    top_position = ((width - text_size * len(top) / 2) / 2, height * 0.1)
    bottom_position = ((width - text_size * len(bottom) / 2) / 2, height * 0.85 - text_size)

    draw.text(top_position, top, font=font, fill="white", font_size=text_size)
    draw.text(bottom_position, bottom, font=font, fill="white", font_size=text_size)

    output = io.BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return send_file(output, mimetype="image/png")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)