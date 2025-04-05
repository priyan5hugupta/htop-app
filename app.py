from flask import Flask
import os
import datetime
import pytz
import subprocess
import getpass

app = Flask(__name__)

@app.route("/")
def htop():
    # Your full name
    full_name = "Priyanshu Gupta"

    # System username
    username = "priyan5hugupta"

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist)

    # Output of top command (first few lines)
    top_output = subprocess.getoutput("top -b -n 1 | head -n 30")

    html = f"""
    <h2>Name: {full_name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {current_time}</h2>
    <h2>TOP output:</h2>
    <pre style="white-space: pre-wrap; font-size: 14px;">{top_output}</pre>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
