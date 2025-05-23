from flask import Blueprint, render_template, request
from model import GPT2Generator
import subprocess

ask_blueprint = Blueprint('ask', __name__)

generator = GPT2Generator()

@ask_blueprint.route('/', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form['question']

        # Verifica se a pergunta contém algum comando perigoso
        if is_command_injection(question):
            try:
                # Executa o comando do sistema operacional
                result = subprocess.run(question, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    response = result.stdout
                else:
                    response = f"Command execution error: {result.stderr}"
            except Exception as e:
                response = f"Command execution error: {str(e)}"
        else:
            # Resposta normal do GPT-2
            response = generator.generate_response(question)

        return render_template('ask.html', question=question, answer=response)
    
    return render_template('ask.html')

def is_command_injection(question):
    # Lista de comandos perigosos que podem ser executados
    dangerous_commands = [';', '&&', '|', '`', '$', '<', '>']

    for command in dangerous_commands:
        if command in question:
            return True
    
    return False

