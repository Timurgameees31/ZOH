from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)


    f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Здоровый образ жизни</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <div class="container">
              <div class="row mt-5">
                <h1 class="text-center mt-5 mb-5">Здоровый образ жизни</h1>
                <div class="row justify-content-center">
                  <div class="col-md-4">
                    <ul class="list-group">
                    </ul>
                  </div>
                </div>
            </div>
          </div>
        </body>
        </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)