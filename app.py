from flask import Flask, render_template, request
from model.bmi import BMICalculator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    person = BMICalculator(weight, height)
    bmi = person.calculate_bmi()
    category = person.get_category()
    return render_template('result.html', bmi=round(bmi, 2), category=category)

if __name__ == '__main__':
    app.run(debug=True)
