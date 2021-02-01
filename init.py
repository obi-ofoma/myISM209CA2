from flask import Flask, render_template

app = Flask(__name__) # create a flask app named app

@app.route("/")
def home():
    return '''My name is Obiajulu Ofoma. This is my CA2 work.
    My GitHub URL is https://github.com/obi-ofoma/'''
    # In the return statement above, Use your own name and GitHub URL

@app.route("/products-and-services/")
def products_and_services():
    return render_template('index.html', title="Home MTN")


if __name__ == "__main__":
    app.run(port=5005)