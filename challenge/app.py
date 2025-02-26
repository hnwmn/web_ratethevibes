from flask import Flask, request, redirect, url_for, render_template, jsonify, abort

app = Flask(__name__)

feedback = [
    {"email": "john.doe@warwick.ac.uk", "comment": "Only feedback is that this society is amazing!"},
    {"email": "jane.smith@warwick.ac.uk", "comment": "Needs improvement."},
    {"email": "admin@intakectf.warwick.ac.uk", "comment": "Your flag is: Intake24{U1RBVFVTXzIwMF9PSw}"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # We do no actual processing or storage of data
    return redirect(url_for('thankyou'))

@app.route('/submissions', methods=['GET', 'POST'])
def submissions():
    x_forwarded_for = request.headers.get('X-Forwarded-For')

    if request.method == 'POST':
        return jsonify({"message": "POST request received, but nothing special here. Are you sure you're coming from the right place?"})
    
    if x_forwarded_for == '127.0.0.1':
        # Return feedback data if the X-Forwarded-For header is set to '127.0.0.1'
        return jsonify(feedback)
    
    # For GET requests abort with a 403 Forbidden error
    abort(403)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submissions/archive')
def archive():
    return jsonify({
        "status": "error",
        "message": "Archive has been disabled. No data here."
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)