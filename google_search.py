import webbrowser
import re

# Controls
def launch_google(query):

    address = "https://www.google.com/#q="
    query_words = query.split()

    # REMOVE NONALPHANUMERIC CHARS
    query = re.sub(r'\W+', ' ', query)
    
    # ENSURE LOWER CASE
    query = query.lower()

    # REMOVE LEADING AND TRAILING WHITE SPACES
    query = query.strip()

    # REPLACE WHITE SPACES WITH '+'
    query = query.replace(" ", "+")

    # APPEND QUERY TO ADDRESS
    url = address + query
    
    webbrowser.open_new(url)
