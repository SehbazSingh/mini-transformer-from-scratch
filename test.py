from model_utils import load_model, generate
try :
    load_model("model.pth")
except Exception as e:
    print("Error loading model:", e)

while True:
    user = input("You: ")
    if user == "exit":
        break
    print("Bot:", generate(user.split()))