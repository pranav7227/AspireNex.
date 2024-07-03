import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from model.image_captioning_model import generate_caption

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            print("No selected file")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(f"Saving file to {filepath}")
            file.save(filepath)
            caption = generate_caption(filepath)
            return render_template('index.html', caption=caption, filename=filename)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

