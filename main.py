from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')

def home():
    # Simple HTML content
    html_content = """
    <!doctype html>
    <html>
    <head><title>Flask App</title></head>
    <body>
        <h1>Welcome to the Flask App!</h1>
        <p>This is a simple HTML page served by Flask.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
