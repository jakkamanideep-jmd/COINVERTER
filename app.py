from flask import Flask, request, render_template,redirect,url_for
from currency_converter import CurrencyConverter

app = Flask(__name__)
c = CurrencyConverter()

@app.route("/", methods=["GET", "POST"])
def home():
    result=None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from"]
        to_currency = request.form["to"]
        result = c.convert(amount, from_currency, to_currency)
        return redirect(url_for('home',result=result))
    result=request.args.get("result")
    return render_template('index.html',result=result)
    

if __name__ == "__main__":
    app.run(debug=True)
