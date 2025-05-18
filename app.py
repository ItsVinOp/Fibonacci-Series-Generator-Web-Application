from flask import Flask, render_template, request

app = Flask(__name__)

def generate_fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == 'POST':
        try:
            terms = int(request.form['terms'])
            result = generate_fibonacci(terms)
        except ValueError:
            result = ["Invalid input! Please enter a number."]
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
