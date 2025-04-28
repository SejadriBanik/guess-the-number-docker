from flask import Flask, request, session, redirect, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0  # Initialize attempts when game starts
    
    message = ""
    if request.method == 'POST':
        guess = int(request.form['guess'])
        number = session['number']
        session['attempts'] += 1  # Increase attempt count

        if guess < number:
            message = "Too low! Try again."
        elif guess > number:
            message = "Too high! Try again."
        else:
            message = f"Correct! You guessed it in {session['attempts']} attempts."
            session.pop('number')    # Clear number
            session.pop('attempts')  # Clear attempts (reset for new game)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
