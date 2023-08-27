
FROM python:3.11

# Встановимо робочу директорію всередині контейнера
WORKDIR /My_course_project

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install pipenv
RUN pipenv install
RUN pip install dist/bot_assistant-0.1.0-py3-none-any.whl

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5000

# Запустимо наш застосунок всередині контейнера. Це точка входу.
ENTRYPOINT ["python", "bot_assistant/main.py"]