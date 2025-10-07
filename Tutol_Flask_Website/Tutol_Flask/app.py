from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaofcircle', methods=['GET', 'POST'])
def AreaOfCircle():
    area = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            area = round(3.14 * radius ** 2, 4)
        except ValueError:
            area = "Invalid input. Please enter a number."
    return render_template('areaofcircle.html', area=area)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def AreaOfTriangle():
    area = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            area = round(0.5 * base * height, 4) 
        except ValueError:
            area = "Invalid input. Please enter valid numbers."
    return render_template('areaoftriangle.html', area=area)


@app.route('/touppercase', methods=['GET', 'POST'])
def ToUppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
