pip install torch transformers nltk


import nltk
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


nltk.download('punkt')


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def chat_with_bot(user_input, chat_history_ids=None):
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

print("AI Chatbot: Hello! Type 'exit' to end the chat.")
chat_history_ids = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Chatbot: Goodbye!")
        break
    
    response, chat_history_ids = chat_with_bot(user_input, chat_history_ids)
    print(f"AI Chatbot: {response}")
