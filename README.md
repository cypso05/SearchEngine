# SearchEngine
This is a Search Engine developed from rapidAPI database. it incorporates python, javascript and HTML5 to provide real time results. 
To use this application, navigate to  "real-time-web-search.p.rapidapi.com", signup and suscribe to get your unique API key. replace the portion of the script in the app.py file with your API key and you are ready to test the application. 
# app.py
This Python code implements a simple web search application using the Flask framework.

The main purpose of app.py is to provide a web interface that allows users to submit search queries, make requests to a third-party search API, and return the search results to display on the webpage.

The code first imports the necessary modules like Flask, render_template, request, and jsonify. Flask provides the web framework, render_template is used to generate HTML pages, request gives access to web requests, and jsonify converts Python objects to JSON format.

Next, an instance of the Flask application called 'app' is created. This will allow creating the routes and views for the web app.

API keys for making requests to the real-time web search API are defined - RAPID_API_KEY and RAPID_API_HOST. These keys are needed to authenticate the requests to the API.

The route '/' is defined which renders the homepage template 'index.html' when a user visits the root URL.

The '/search' route handles the search request posted from the homepage form. It first checks if the request method is POST, then extracts the search query and limit parameters from the form data.

Headers are defined for making the API request - containing the API key and host. The search URL and parameters are built with the user's query and limit.

A request is made to the API and the JSON response is returned. If any error occurs, an error message is returned instead.

Finally, the app is run with debug mode enabled.

# index.html
The index.html code implements a basic search engine UI with HTML, CSS, and JavaScript.

It starts by setting up the HTML document structure with the doctype, html, head, and body tags. In the head, it includes meta tags for character encoding and viewport, styles the page with CSS, and loads a JavaScript script.

The CSS styles the overall page layout, fonts, colors, etc. It has styles for headings, the search form, results container, and individual result styling.

The HTML body contains a main .container div which centers the content. It has a heading, a search form with input and button, and a div to display results.

The JavaScript handles the search form submission. It adds a submit event listener to the form which prevents the default submit, gets the search query value, and sends a POST request to the backend with the query.

The POST request is handled asynchronously. When the JSON response comes back, it clears any previous results, loops through the hits, and inserts new HTML search results into the page by concatenating strings.

Each result div shows the title linked to the URL, snippet text, and domain.

So in summary, the HTML, CSS, and JS work together to:

Display a search form
Allow the user to input a search query
Send the query to the backend on form submit
Receive the results
Dynamically display the results on the page
It transforms the user's search query input into useful search results output by using form submission and asynchronous requests to retrieve and display relevant data from the backend search API.
