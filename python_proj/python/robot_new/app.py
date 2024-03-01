# app.py
from flask import Flask, render_template, request
from Bio import SeqIO
from alphafold.predict import AlphaFold

app = Flask(__name__)

# Load the pre-trained AlphaFold model
alphafold = AlphaFold()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the protein sequence from the form
        protein_sequence = request.form['protein_sequence']

        # Predict protein structure using AlphaFold
        prediction = alphafold.predict(protein_sequence)

        # Pass the prediction result to the template
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
