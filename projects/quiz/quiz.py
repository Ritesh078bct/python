from string import ascii_lowercase
import random 
import pathlib
import tomllib

QUESTIONS_PATH=pathlib.Path(__file__).parent/"questions.toml"

number_questions_per_quiz=5

QUESTIONS=tomllib.loads(QUESTIONS_PATH.read_text())
# print(QUESTIONS_PATH)

# QUESTIONS={
#     "who is father of computer":[
#         "charles babage",
#         "denis ritchie",
#         "james gosling",
#         "dale carnage"
#        ],
#     "what is python extension":[
#         ".py",
#         ".p",
#         ".python",
#         ".pip"
#         ],
# }

# num_questions=min(number_questions_per_quiz,len(QUESTIONS))
# questions=random.sample(list(QUESTIONS.items()),k=num_questions)

# correct_answer_number=0
# for number, (question,options) in enumerate(questions, start=1):
#     correct_answer=options[0]
#     print(f"Q.{number} {question}")

#     # sorted_options=sorted(options)
#     # print(sorted_options)
#     # labeled_options=dict(zip(ascii_lowercase,sorted(options)))
#     labeled_options=dict(zip(ascii_lowercase,random.sample(options,k=len(options))))

#     for index,option in labeled_options.items():
#         print(f"{index}){option}")

#     # user_answer_index=input("enter your answer: ")
#     while(user_answer_index:=input("enter your answer: ")) not in labeled_options:
#         print(f"Please answer one of {','.join(labeled_options)}")
#     user_answer=labeled_options.get(user_answer_index)
#     if user_answer==correct_answer:
#         correct_answer_number +=1
#         print("⭐correct⭐")

#     else:
#         print(f"correct answer is {correct_answer}")

# print(f"you answered {correct_answer_number} correctly out of {number} questions")



def run_quiz():
    #preprocess
    questions=prepare_questions(QUESTIONS, number_questions_per_quiz)

    #process
    correct_answer_number=0
    for number, (question,options) in enumerate(questions,start=1):
        print(f"\nQustion {number}",end=".")
        correct_answer_number +=ask_questions(question,options)

    #post process
    print(f"you answered {correct_answer_number} correctly out of questions")

def prepare_questions(questions,num_questions_per_quiz):
    num_questions=min(number_questions_per_quiz,len(questions))
    questions=random.sample(list(questions.items()),k=num_questions)
    return questions



def get_answer(question,options):
    print(f" {question}")
    labeled_options=dict(zip(ascii_lowercase,options))

    for index,option in labeled_options.items():
        print(f"{index}){option}")

    # user_answer_index=input("enter your answer: ")
    while(user_answer_index:=input("enter your answer: ")) not in labeled_options:
        print(f"Please answer one of {','.join(labeled_options)}")

    return labeled_options[user_answer_index]


def ask_questions(question,options):
    correct_answer=options[0]
    ordered_options=random.sample(options,k=len(options))

    answer=get_answer(question,ordered_options)
    if answer==correct_answer:
        print("⭐correct ⭐")
        return 1
    else:
        print(f" the correct answer is {correct_answer}")
        return 0
    


if __name__=="__main__":
    run_quiz();
