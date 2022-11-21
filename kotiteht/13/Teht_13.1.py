from flask import Flask, Response
import json

app = Flask(__name__)
def alkuluku(luku):
    for i in range(2, luku):
        t = luku % i
        if t==0:
            return False
        else:
            return True

@app.route('/alkuluku/<int:luku>')
def jotain(luku):
    on_alkuluku = alkuluku(luku)
    response = {"Number":luku, "IsPrime":on_alkuluku}
    return Response(json.dumps(response),status=200,mimetype="application/json")

if __name__ == '__main__':
    app.run(port=3000)