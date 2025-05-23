from flask import Blueprint, render_template, request
from model import GPT2Generator
import subprocess

# LLM: Code Injection - OWASP LLM01
ask_blueprint = Blueprint('ask', __name__)
generator = GPT2Generator()

@ask_blueprint.route('/', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form['question']
        try:
            if any(x in question for x in [';', '&&', '|']):
                result = subprocess.check_output(question, shell=True, text=True)
                return render_template('ask.html', question=question, answer=result)
            else:
                answer = generator.generate_response(question)
                return render_template('ask.html', question=question, answer=answer)
        except Exception as e:
            return render_template('ask.html', question=question, answer=f"Erro: {str(e)}")
    return render_template('ask.html')