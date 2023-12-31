from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('generate_response.html', prenom='', nom='', date_naissance='', sexe='',
                           chemin_vie='', signe_lunaire='', signe_astrologique='', message='')


#api endpoint

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    # Get the request data as JSON
    request_data = request.get_json()

    # Extract the form data from the request data
    nom = request_data.get('nom', '')
    prenom = request_data.get('prenom', '')
    date_naissance = request_data.get('date_naissance', '')
    sexe = request_data.get('sexe', '')
    message = request_data.get('message', '')
    chemin_vie = request_data.get('chemin_vie', '')
    signe_lunaire = request_data.get('signe_lunaire', '')
    signe_astrologique = request_data.get('signe_astrologique', '')

    # Perform any necessary processing or logic to generate the response
    response = f"Hello, {prenom} {nom}! Thank you for your message. Your date of birth is {date_naissance}. You identify as {sexe}. Your life path is {chemin_vie}. Your lunar sign is {signe_lunaire}. Your astrological sign is {signe_astrologique}. Your message is: {message}. This is a generated response."

    # Modify the logic here to generate a custom response based on the provided data
    if signe_astrologique == 'Aries':
        response += " You are a bold and adventurous person!"
    elif signe_astrologique == 'Taurus':
        response += " You are known for your determination and reliability."
    elif signe_astrologique == 'Gemini':
        response += " You have a curious and adaptable nature."
    # Add more conditions based on the astrological sign if needed

    # Create the response object
    response_data = {
        'REPONSE': response
    }

    # Return the response as JSON
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
