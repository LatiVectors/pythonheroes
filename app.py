from flask import Flask, render_template, redirect

app = Flask(__name__)

link = "wa.me/2348162043451"

@app.route("/")
def lativectors():
    return render_template("index.html")

@app.route("/join")

def join():
    return redirect(link)

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = "5000", debug= True)
