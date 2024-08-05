from flask import Flask, render_template, redirect, url_for
import serial

app = Flask(__name__)

# ser = serial.Serial('/dev/ttyTHS1', 9600)

ser = 0;

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/automatic')
def automatic():
    return render_template('automatic.html')

@app.route('/send/<int:value>')
def send(value):
    ser.write(str(value).encode())
    return redirect(url_for('manual'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
