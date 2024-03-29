# Import Flask, render_template, request, and jsonify 
# Flask - web framework, render_template - to render HTML templates
# request - to access web requests, jsonify - to convert to JSON
from flask import Flask, render_template, request, jsonify
import requests # To make HTTP requests

# Create Flask app instance
app = Flask(__name__) 

# API keys for making requests to search API
RAPID_API_KEY = "9d01b0e0fcmsh697f6ab0ed8b363p1b02c2jsn2de91ea25e7e" 
RAPID_API_HOST = "real-time-web-search.p.rapidapi.com"

# Route for the home page
@app.route('/')
def index():
    # Render home page template
    return render_template('index.html')

# Route for search requests
@app.route('/search', methods=['POST'])
def search():
    # Check if request method is POST
    if request.method == 'POST':
        # Get search query and limit from form
        query = request.form.get('query')  
        limit = request.form.get('limit', '10')
        
        # Set headers for API request
        headers = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": RAPID_API_HOST
        }
        
        # Build request URL and parameters
        url = "https://real-time-web-search.p.rapidapi.com/search"
        params = {"q": query, "limit": limit}
        
        # Make API request
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            # Return JSON response
            return jsonify(data)
            
        except Exception as e:
            # Return error message
            return jsonify({'error': str(e)})
            
    # Return error if not POST request
    return jsonify({'error': 'Method not allowed'})

# Run app
if __name__ == '__main__':
    app.run(debug=True)
