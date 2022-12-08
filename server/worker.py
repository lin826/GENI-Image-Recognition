#!/usr/bin/env python
# encoding: utf-8
import os
import clip
import json
import torch
from PIL import Image
from flask import Flask, request, jsonify
from torchvision.datasets import CIFAR100

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

# Download the dataset
cifar100 = CIFAR100(root=os.path.expanduser("~/.cache"), download=True, train=False)
text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in cifar100.classes]).to(device)

app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({})

@app.route('/recognize', methods=['POST'])
def recognize_image():
    file = request.files['image']
    img = Image.open(file.stream)

    # Prepare the inputs
    image_input = preprocess(img).unsqueeze(0).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top one most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(1)

    for value, index in zip(values, indices):
        return jsonify({'text': cifar100.classes[index],'accuracy': value.item()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
