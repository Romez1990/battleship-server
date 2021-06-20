from src.questions.question_service_impl import QuestionServiceImpl

questions = QuestionServiceImpl()
for question in questions._QuestionServiceImpl__questions:
    question = question.to_model()
    print(question.text)
    for answer in question.answers:
        print(f'- {answer}')
    print()
