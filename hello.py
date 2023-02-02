from flask import Flask, request
app = Flask(__name__)
app.index_string = '''<!DOCTYPE html>
<html>
<head>
<title>My app title</title>
<link rel="manifest" href="./assets/manifest.json" />
{%metas%}
{%favicon%}
{%css%}
</head>
<script type="module">
   import 'https://cdn.jsdelivr.net/npm/@pwabuilder/pwaupdate';
   const el = document.createElement('pwa-update');
   document.body.appendChild(el);
</script>
<body>
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', ()=> {
      navigator
      .serviceWorker
      .register('./assets/sw01.js')
      .then(()=>console.log("Ready."))
      .catch(()=>console.log("Err..."));
    });
  }
</script>
{%app_entry%}
<footer>
{%config%}
{%scripts%}
{%renderer%}
</footer>
</body>
</html>
'''

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

