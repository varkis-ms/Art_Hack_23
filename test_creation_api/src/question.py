from typing import List

from src.constants import TEST_GENERATOR_PROMPT
from src.models import QuesitonAnswerModel
from src.utils import generate_with_chat_gpt


def create_test_from_prompt(
    article_text: str,
    num_questions: int,
    max_tokens: int = 64,
    temperature: float = 1.0,
) -> List[QuesitonAnswerModel]:
    prompt = TEST_GENERATOR_PROMPT.format(
        article_text=article_text, num_questions=num_questions
    )

    raw_response = generate_with_chat_gpt(
        prompt=prompt, max_tokens=max_tokens, temperature=temperature
    )

    test = []
    for line in raw_response.split("\n"):
        try:
            question_answer = QuesitonAnswerModel.from_response(line)
            test.append(question_answer)
        except Exception as e:
            print(e)

    return test
