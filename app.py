import torch
from flask import Flask, request, jsonify
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

app = Flask(__name__)

# Load tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Load model architecture
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Load model weights and map to CPU
model.load_state_dict(torch.load('D:/Study/Khai Thác Dữ Liệu/bert_model.pth', map_location=torch.device('cpu')))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    
    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    
    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    
    # Get predicted label
    predicted_label = torch.argmax(logits, dim=1).item()
    
    # Map label to class name
    label_map = {0: 'No Spam', 1: 'Spam'}
    predicted_class = label_map[predicted_label]
    
    return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
