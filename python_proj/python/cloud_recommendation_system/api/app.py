from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Get the absolute path to the model file
model_file = os.path.join(os.path.dirname(__file__), '..', 'models', 'decision_tree_model.pkl')
model = joblib.load(model_file)

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    features = [data['cpu_usage'], data['ram_usage'], data['storage_usage'], data['transaction_count']]
    recommendation = model.predict([features])[0]
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
