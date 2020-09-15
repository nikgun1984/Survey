from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import face_masks

app = Flask(__name__)

app.config['SECRET_KEY'] = "whateverpassword1"
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

responses = []
# debug  = DebugToolbarExtension(app)
@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/questions/<int:num>')
def get_question(num):
    if num < len(responses) or num > len(responses):
        flash("You accessed an invalid question...","error")
        return redirect(f'/questions/{len(responses)}')
    else:
        if num < len(face_masks.questions):
            quest = face_masks.questions[num]
            return render_template('question.html',num=num, quest = quest)
        else:
            return redirect('/thankyou')


@app.route('/answer/<int:num>', methods=["POST"])
def post_question(num):
    choice = request.form[str(num)]
    if face_masks.questions[num].allow_text:
        answer = request.form[f"question{num}"]
    responses.append(choice)
    return redirect(f'/questions/{num+1}')

@app.route('/thankyou')
def thank_you():
    return render_template('thanks.html')
