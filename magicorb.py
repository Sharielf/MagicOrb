import random
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
answ = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
        "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
name = input('Как тебя зовут?')
print('Привет', name)

while True:
    ques = input('Задайте свой вопрос!')
    print(random.choice(answ))
    cont = input('Еще есть вопросы? Ответь да/нет')
    if cont.lower() == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
