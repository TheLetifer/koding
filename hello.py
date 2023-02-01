from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    html = """
    <html>
        <head>
            <style>
                .center {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <div class="center">
                <p>Tumhari Mummy ki Gand!</p>
            </div>
        </body>
    </html>
    """
    return html



if __name__ == "__main__":
    app.run()

