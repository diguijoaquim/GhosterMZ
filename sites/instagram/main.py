from flask import Flask,render_template
import logging

app=Flask(__name__)
app.log_exception=False
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)
@app.route('/')

def home():
    app.logger.info(f"""
    Name: Ghost04
""")
    return render_template("mobile.html")

if __name__=="__main__":
    app.logger.info("Iniciando o aplicativo Flask.")
    app.run(debug=True)