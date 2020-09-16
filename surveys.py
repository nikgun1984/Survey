class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, link, title, instructions, questions):
        """Create questionnaire."""
        self.link = link
        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "satisfaction",
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "personality",
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

face_masks  = Survey(
    "face_masks",
    "Survey Results on Mask-Wearing Behaviors and Beliefs",
    "Answer all questions in this quiz!",
    [
        Question("Did you wear a mask or other face covering the last time you went out in public to an indoor space, such as shopping in a grocery store?"),
        Question("If masks were provided for free when entering a store, would you wear one?"),
        Question("Where you live, is it required for most adults to wear a mask or face covering in public spaces, such as grocery stores?",
        ["Yes", "No", "Not Sure"]),
        Question("When at a store, do you feel more comfortable, less comfortable, or indifferent if employees are wearing masks?",
        ["More comfortable","Less comfortable","Indifferent"]),
        Question("When at a store, do you feel more comfortable, less comfortable, or indifferent if other shoppers are wearing masks?",
        ["More comfortable","Less comfortable","Indifferent"]),
        Question("Does wearing a mask help to reduce the spread of the coronavirus?",
        ["Yes, a lot", "Yes, some", "Not sure", "No, it does nothing", "No, it increases the spread"]),
        Question("Does wearing a mask make you less likely to follow social-distancing guidelines?",
        ["Yes", "No", "Not Sure"])
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "face_masks": face_masks
}