from os import environ
from flask import Flask
import subprocess


app = Flask(__name__)
app.run(environ.get('PORT'))
subprocess.run("python JoguinhosGratis.py")