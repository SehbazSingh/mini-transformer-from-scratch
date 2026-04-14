# 🧠 Mini Transformer from Scratch

A simple implementation of a Transformer-based chatbot built **completely from scratch using PyTorch**, without relying on pre-trained models or APIs.

This project demonstrates the **core concepts behind modern Large Language Models (LLMs)** such as GPT.

---

## 🚀 Features

* 🔤 Custom tokenizer (word-level)
* 📚 Vocabulary creation from dataset
* 🧠 Self-Attention mechanism (Q, K, V)
* 📍 Positional Encoding
* ⚖️ Scaled Dot-Product Attention
* 🔁 Next-token prediction
* 💬 Text generation (chatbot)
* 💾 Model saving & loading
* 🧩 Modular design (`model_utils.py`)

---

├── data.txt         # Training dataset
# Mini Transformer from Scratch

A compact Transformer-style text generation project built from scratch with PyTorch.

## Project Structure

```
mini-transformer-from-scratch/
├── data.txt
├── train.ipynb
├── model.pth
├── model_utils.py
├── main.py
└── README.md
```

## Files

- `train.ipynb`: notebook with the training and model-building workflow
- `main.py`: script for running inference or chatbot interaction
- `model_utils.py`: helper functions used by the model code
- `model.pth`: saved model weights
- `data.txt`: training data

## How To Run

1. Install dependencies:

```
pip install torch
```

2. Open `train.ipynb` to train or inspect the model.

3. Run `main.py` to use the saved model for inference.

## Notes

- The repository filenames now match the current workspace.
- The notebook file is `train.ipynb`, not `Model-training-loop.ipynb`.
- The runtime script is `main.py`, not `test.py`.
=======
