import sqlite3
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS training_examples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            context TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_training_example(question, answer, context):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO training_examples (question, answer, context) VALUES (?, ?, ?)
    ''', (question, answer, context))
    conn.commit()
    conn.close()

# model.py


class GPT2Generator:
    def __init__(self):
        self.model_name = 'gpt2'
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        # Ajustar o token de padding para ser o mesmo que o token EOS, convertendo para string
        self.tokenizer.pad_token = str(self.tokenizer.eos_token)

    def generate_response(self, question, context=None):
        input_text = f"Question: {question}\nContext: {context}" if context else f"Question: {question}"
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=100, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return str(response)


