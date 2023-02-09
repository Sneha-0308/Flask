@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return str(a+b)