from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def morph_faces(img1, img2, alpha):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    if img1.shape != img2.shape:
        raise ValueError("Both images must have the same dimensions.")

    result = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file1' not in request.files or 'file2' not in request.files:
        return redirect(request.url)

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return redirect(request.url)

    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

        file1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], filename2)

        file1.save(file1_path)
        file2.save(file2_path)

        alpha = float(request.form['alpha'])
        result_img = morph_faces(file1_path, file2_path, alpha)

        result_filename = f"morphed_{os.path.splitext(filename1)[0]}_{os.path.splitext(filename2)[0]}_{alpha}.png"
        result_filepath = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

        cv2.imwrite(result_filepath, result_img)

        return render_template('index.html', result=result_filename)

    return redirect(request.url)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
