import openai
from typing import List
from fastapi import FastAPI
from src.question import create_test_from_prompt
from src.models import Settings, QuesitonAnswerModel


settings = Settings()
app = FastAPI()

openai.api_key = settings.open_ai_key


@app.get("/get_test")
def get_test(input_article: str, num_questions: int) -> List[QuesitonAnswerModel]:
    # could return less than num_questions :(
    questions = create_test_from_prompt(
        article_text=input_article,
        num_questions=num_questions,
        max_tokens=1024,
    )
    return questions
