from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Green Version</title>
        <style>
            body {
                font-family: Arial;
                background-color: #dcfce7;
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
                color: green;
            }
            .feature {
                margin-top: 20px;
                background: #f0fdf4;
                padding: 15px;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🟢 GREEN VERSION</h1>
            <h2>Student Portal</h2>
            <p>Welcome to the Student Portal Application.</p>
            <button>View Profile</button>

            <div class="feature">
                <h3>✨ NEW FEATURE ADDED</h3>
                <p>Students can now check attendance online.</p>
                <button>Check Attendance</button>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)