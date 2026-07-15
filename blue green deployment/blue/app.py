from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Blue Version</title>
        <style>
            body {
                font-family: Arial;
                background-color: #dbeafe;
                text-align: center;
                padding-top: 100px;
            }
            .box {
                background: white;
                width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 0px 10px gray;
            }
            h1 {
                color: blue;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🔵 BLUE VERSION</h1>
            <h2>Student Portal</h2>
            <p>Welcome to the Student Portal Application.</p>
            <button>View Profile</button>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)