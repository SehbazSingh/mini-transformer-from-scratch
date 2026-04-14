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

## 🏗️ Architecture

The model follows a simplified Transformer pipeline:

```
Input Text
   ↓
Tokenization
   ↓
Embedding Layer
   ↓
Positional Encoding
   ↓
Self-Attention (Q, K, V)
   ↓
Linear Layer (Prediction)
   ↓
Next Token Output
```

---

## 🧠 Key Concepts Implemented

* Self-Attention
* Scaled Dot-Product Attention
* Positional Encoding
* Sequence Modeling
* Probabilistic Sampling (temperature)

---

## 📂 Project Structure

```
mini-transformer-from-scratch/
│
├── model_utils.py   # Load model + generate responses
├── train.py         # Training script
├── main.py          # Chatbot interface
├── data.txt         # Training dataset
├── model.pth        # Saved model weights
└── README.md
```

---

## ⚙️ Installation

```
git clone https://github.com/your-username/mini-transformer-from-scratch.git
cd mini-transformer-from-scratch
pip install torch
```

---

## ▶️ How to Run

### 1. Train the model

```
python train.py
```

### 2. Run chatbot

```
python main.py
```

---

## 💬 Example Outputs

```
You: what is ai
Bot: ai is artificial intelligence

You: who are you
Bot: i am a chatbot

You: what is python
Bot: python is a programming language
```

---

## 💾 Model Saving & Loading

The trained model is saved using:

```
torch.save(...)
```

And reused with:

```
load_model("model.pth")
```

---

## 🎯 Limitations

* Small dataset → limited knowledge
* Word-level tokenizer (no subword handling)
* Single-head attention (not full transformer)
* No pretraining on large corpora

---

## 🚀 Future Improvements

* Multi-head attention
* Larger dataset
* Better tokenizer (BPE / WordPiece)
* GUI / Web interface (Streamlit)
* Model deployment

---

## 📌 Learning Outcomes

This project helps understand:

* How Transformers work internally
* How LLMs generate text
* Importance of data quality
* Model training vs inference
* End-to-end ML pipeline

---

## 👨‍💻 Author

**Sehbaz Singh**

---

## ⭐ Acknowledgment

Inspired by modern NLP architectures like Transformer and GPT.
