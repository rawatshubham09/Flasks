from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weight = 0
    height = 0
    bmi = 0
    if request.method == 'POST' and 'weightvalue' in request.form:
        weight = int(request.form.get("weightvalue"))
        height = int(request.form.get("heightvalue"))

        bmi = weight/((height/100)**2)
        bmi = (bmi//0.01)/100

    return render_template('main.html', bmi = bmi)

if __name__=="__main__":
    app.run(debug=True)