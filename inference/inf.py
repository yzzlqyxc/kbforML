from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from flask import Flask, request, jsonify

checkpoint = "/shared/checkpoint-1377"  
tokenizer = AutoTokenizer.from_pretrained(checkpoint, local_files_only=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModelForSequenceClassification.from_pretrained(checkpoint, local_files_only=True)
model = model.to(device)


app = Flask(__name__)
@app.route("/getinf", methods=["POST"])
def getinf():
    data = request.get_json()

    sentence1 = data.get('first')
    sentence2 = data.get('second')
    inputs = tokenizer(sentence1, sentence2, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
    print(sentence1, sentence2)

    return jsonify({"probs": probs.cpu().numpy().tolist(), "pred":pred})

app.run(host="0.0.0.0", port=5001)