import re
from typing import List
import os

from pydantic import BaseModel, BaseSettings, Field


class Settings(BaseSettings):
    open_ai_key: str = os.getenv("OPEN_AI_KEY")

class QuesitonAnswerModel(BaseModel):
    question_text: str = Field(
        ..., description="Текст вопроса", example="Что такое линейная регрессия?"
    )
    answer_text: str = Field(..., description="Ответ на вопрос", example="AX=B")
    popularity: float = Field(
        ...,
        description="Оценка популярности вопроса по шкале от одного до десяти",
        example=7,
        gte=1,
        leq=10,
    )
    difficulty: float = Field(
        ...,
        description="Оценка сложности вопроса по шкале от одного до десяти",
        example=4,
        gte=1,
        leq=10,
    )

    @classmethod
    def from_response(cls, response: str) -> "QuesitonAnswerModel":
        contain_russian = re.search("[а-яА-Я]", response)
        if not contain_russian:
            raise ValueError(
                f"Questions and answers should contain russian language words"
            )

        occurences = re.findall("<Q>|</Q>|<P>|</P>|<D>|</D>|<A>|</A>", response)
        if occurences != ["<Q>", "</Q>", "<P>", "</P>", "<D>", "</D>", "<A>", "</A>"]:
            raise ValueError(f"Response «{response}» does not match pattern")

        questions = re.findall("<Q>(.*)</Q>", response)
        if len(questions) != 1:
            raise ValueError(
                f"Questions array «{questions}» does not contain single element"
            )

        answers = re.findall("<A>(.*)</A>", response)
        if len(answers) != 1:
            raise ValueError(
                f"Answers array «{answers}» does not contain single element"
            )

        question = questions[0]
        answer = answers[0]

        popularities = re.findall("<P>(.*)</P>", response)
        if len(popularities) != 1:
            raise ValueError(
                f"Popularities array «{popularities}» does not contain single element"
            )

        difficulties = re.findall("<D>(.*)</D>", response)
        if len(difficulties) != 1:
            raise ValueError(
                f"Difficulties array «{difficulties}» does not contain single element"
            )

        popularity = popularities[0]
        if not popularity.isdigit():
            raise ValueError(f"Popularity «{popularity}» is not a digit")

        difficulty = difficulties[0]
        if not difficulty.isdigit():
            raise ValueError(f"Difficulty «{difficulty}» is not a digit")

        return cls(
            question_text=question,
            answer_text=answer,
            popularity=popularity,
            difficulty=difficulty,
        )
