from flask import Flask, jsonify

# Initialiser l'application Flask
app = Flask(__name__)

# Route d'exemple : Page d'accueil
@app.route('/')
def home():
	return "Bienvenue sur le serveur Flask !"

# Route d'exemple : API JSON
@app.route('/api/example', methods=['GET'])
def example():
	data = {"message": "Ceci est une réponse JSON", "status": "success"}
	return jsonify(data)

# Lancer le serveur Flask
if __name__ == '__main__':
	app.run(debug=True)
