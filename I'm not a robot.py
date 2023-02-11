from flask import Flask, request

app = Flask(__name__)

@app.route('/robot', methods=["post"])
def robot():
  form = request.form
  if form["metal"]=='Yes':
    return "You're a robot"

@app.route('/')
def index():
    page = """
    <form method="post" action="/robot">
        <p>Are you made of metal? <input type="radio" name="metal" value = "Yes" > Yes </p>
        <input type="radio" name="metal" value = "No" > No </p>
        <p>What is infinity +1?
            <input type = "text" name = "infinity" required>
        </p>
        <p>What is your favorite food?
            <select name = "food">
                <option value = "human food">Human food</option>
                <option value = "Oil">Oil</option>
            </select>
        </p>
        <button type = "submit">I'm not a robot</button>
    </form>"""
    return page



app.run(host='0.0.0.0', port=81)
