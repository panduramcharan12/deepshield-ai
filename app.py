from flask import Flask, render_template, request
from model.detector import detect_deepfake
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():

    result = None
    confidence = None
    filename = None

    if request.method == 'POST':

        file = request.files['image']

        if file:

            filepath = os.path.join(
                app.config['UPLOAD_FOLDER'],
                file.filename
            )

            file.save(filepath)

            result, confidence = detect_deepfake(filepath)

            filename = file.filename

    return render_template(
        'index.html',
        result=result,
        confidence=confidence,
        filename=filename
    )


if __name__ == '__main__':
    app.run(debug=True)
