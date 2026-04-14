import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# =========================
# GLOBAL VARIABLES
# =========================
embed = None
Wq = None
Wk = None
Wv = None
fc = None

word_to_index = None
index_to_word = None

embed_dim = 16
seq_length = 3

# =========================
# LOAD MODEL
# =========================
def load_model(path="model.pth"):
    global embed, Wq, Wk, Wv, fc
    global word_to_index, index_to_word

    checkpoint = torch.load(path)

    word_to_index = checkpoint['word_to_index']
    index_to_word = checkpoint['index_to_word']

    vocab_size = len(word_to_index)

    embed = nn.Embedding(vocab_size, embed_dim)
    Wq = nn.Linear(embed_dim, embed_dim)
    Wk = nn.Linear(embed_dim, embed_dim)
    Wv = nn.Linear(embed_dim, embed_dim)
    fc = nn.Linear(embed_dim, vocab_size)

    embed.load_state_dict(checkpoint['embed'])
    Wq.load_state_dict(checkpoint['Wq'])
    Wk.load_state_dict(checkpoint['Wk'])
    Wv.load_state_dict(checkpoint['Wv'])
    fc.load_state_dict(checkpoint['fc'])

    embed.eval()
    Wq.eval()
    Wk.eval()
    Wv.eval()
    fc.eval()

# =========================
# TOKENIZER
# =========================
def encode(text):
    return [word_to_index.get(word, word_to_index["<UNK>"]) for word in text.split()]

# =========================
# POSITIONAL ENCODING
# =========================
def positional_encoding(seq_len, embed_dim):
    pe = torch.zeros(seq_len, embed_dim)
    for pos in range(seq_len):
        for i in range(embed_dim):
            pe[pos, i] = pos / (10000 ** (2 * (i//2) / embed_dim))
    return pe

# =========================
# GENERATE FUNCTION
# =========================
def generate(start_words, max_len=5):
    words = start_words.copy()

    for _ in range(max_len):

        input_words = words[-seq_length:]
        if len(input_words) < seq_length:
            input_words = ["<UNK>"] * (seq_length - len(input_words)) + input_words

        input_seq = encode(" ".join(input_words))
        input_tensor = torch.tensor([input_seq])

        emb = embed(input_tensor)
        pe = positional_encoding(emb.shape[1], emb.shape[2])
        emb = emb + pe

        Q = Wq(emb)
        K = Wk(emb)
        V = Wv(emb)

        scores = (Q @ K.transpose(-2, -1)) / math.sqrt(embed_dim)
        attention = F.softmax(scores, dim=-1)

        out = attention @ V
        output = fc(out)

        last_output = output[0, -1]

        probs = F.softmax(last_output / 0.8, dim=-1)
        predicted_index = torch.multinomial(probs, 1).item()

        next_word = index_to_word[predicted_index]

        if next_word == "<END>" or next_word == "<UNK>":
            break

        words.append(next_word)

    return " ".join(words[len(start_words):])