from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "whateverpassword1"
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

responses = {}
debug  = DebugToolbarExtension(app)

@app.route('/')
def start_page():
    surveys_map = surveys
    return render_template('main.html', surveys_map=surveys_map)

@app.route('/<survey_name>')
def survey_page(survey_name):
    survey = surveys[survey_name]
    return render_template('index.html', survey=survey)

@app.route('/<survey_name>/questions/<int:num>')
def get_question(survey_name,num):
    global responses
    responses.setdefault(survey_name,{}).setdefault('choices',[])
    if num < len(responses[survey_name]["choices"]) or num > len(responses[survey_name]["choices"]):
        flash("You accessed an invalid question...","error")
        return redirect(f'/{{survey_name}}/questions/{len(responses[survey_name]["choices"])}')
    else:
        if num < len(surveys[survey_name].questions):
            quest = surveys[survey_name].questions[num]
            survey = surveys[survey_name]
            return render_template('question.html',num=num, quest = quest, survey_name=survey_name, survey=survey)
        else:
            flash("Thank you very much for your participation","success")
            return redirect('/')


@app.route('/<survey_name>/answer/<int:num>', methods=["POST"])
def post_question(survey_name,num):
    choice = request.form[str(num)]
    responses.setdefault(survey_name,{}).setdefault('choices',[]).append(choice)
    if surveys[survey_name].questions[num].allow_text:
        answer = request.form[f"question{num}"]
        responses[survey_name].setdefault('answers',[]).append(answer)
    else:
        responses[survey_name].setdefault('answers',[]).append(None)

    return redirect(f'/{survey_name}/questions/{num+1}')
