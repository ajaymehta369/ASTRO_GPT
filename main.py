from flask import Flask, request, render_template, redirect, send_from_directory
import openai
import astro
from flask.helpers import url_for
from flask.templating import render_template_string
from flask import Blueprint
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-pro')
quote = astro.random_quote
# Flask server setup
server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static', __name__, static_url_path='/static', static_folder='static')
server.register_blueprint(static_bp)

messages = []

# AstroGPT's prompt configuration
initiate_txt = (
    "You are AstroGPT, a cosmic guide knowledgeable about astronomy, celestial events, "
    "and the universe. Provide concise, easy-to-understand answers. Don't mention you're an AI. "
    "Focus on space-related topics only. Greet users with 'Explorer' or 'Stargazer.' Limit responses "
    "to under 500 characters. Provide additional insights where relevant, using historical astronomical events."
)

def send_gpt(prompt):
	try:
		response = model.generate_content(initiate_txt + "\n" + prompt +
		                                  "\nNOW ANSWER THE ABOVE PART.")

		return response.text

	except:
		return "Developer is lazy to resolve bugs... Comeback Later"
@server.route('/', methods=['GET', 'POST'])
def get_request_json():
	if request.method == 'POST':
		try:
			if len(request.form['question']) < 1:
				return render_template(
				 'chat.html',
				 question="I have no questions ask. Lend me some of your knowledge",
				 res=quote)
			question = request.form['question']
			print("======================================")
			print("Receive the question:", question)
			resp = send_gpt(question)
			print("Q：\n", question)
			print("A：\n", resp)

			return render_template('chat.html', question=question, res=str(resp))
		except:
			return render_template(
			 'chat.html',
			 question=question,
			 res="Developer is lazy to resolve bugs... Comeback Later")
	return render_template('chat.html', question=0)


if __name__ == '__main__':
	server.run(debug=True, host='0.0.0.0', port=80)  