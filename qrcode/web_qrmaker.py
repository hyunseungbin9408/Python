from flask import Flask, render_template, request, jsonify
import pyqrcode
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make_qrcode", methods=["POST"])
def make_qrcode():
    text = request.form.get("text")
    c = pyqrcode.create(text)
    base64 = c.png_as_base64_str(scale=5, module_color=[0, 0, 0, 255], background=[255, 255, 255])
    return jsonify(error="ok", data=base64)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8999, debug=True)
    