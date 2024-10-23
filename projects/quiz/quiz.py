from string import ascii_lowercase
import random 


number_questions_per_quiz=5

QUESTIONS={
    "who is father of computer":[
        "charles babage",
        "denis ritchie",
        "james gosling",
        "dale carnage"
       ],
    "what is python extension":[
        ".py",
        ".p",
        ".python",
        ".pip"
        ],
}

num_questions=min(number_questions_per_quiz,len(QUESTIONS))
questions=random.sample(list(QUESTIONS.items()),k=num_questions)

correct_answer_number=0
for number, (question,options) in enumerate(questions, start=1):
    correct_answer=options[0]
    print(f"Q.{number} {question}")

    # sorted_options=sorted(options)
    # print(sorted_options)
    # labeled_options=dict(zip(ascii_lowercase,sorted(options)))
    labeled_options=dict(zip(ascii_lowercase,random.sample(options,k=len(options))))

    for index,option in labeled_options.items():
        print(f"{index}){option}")

    # user_answer_index=input("enter your answer: ")
    while(user_answer_index:=input("enter your answer: ")) not in labeled_options:
        print(f"Please answer one of {','.join(labeled_options)}")
    user_answer=labeled_options.get(user_answer_index)
    if user_answer==correct_answer:
        correct_answer_number +=1
        print("⭐correct⭐")

    else:
        print(f"correct answer is {correct_answer}")

print(f"you answered {correct_answer_number} correctly out of {number} questions")



def run_quiz():
    #preprocess
    questions=prepare_questions()

    #process
    correct_answer_number=0
    for question in questions:
        correct_answer_number +=ask_questions(question)

    #post process
    print(f"you answered {correct_answer_number} correctly out of questions")

