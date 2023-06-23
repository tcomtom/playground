from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/play')
def play():
  return render_template("index.html", times=3)

@app.route('/play/<times>/')
def playCount(times):
  return render_template("index.html", times = int(times))

@app.route('/play/<times>/<color>')
def playCountColor(times, color):
  return render_template("index.html", times = int(times), color = color)

if __name__ == "__main__":
  app.run(debug=True, port=5001)
