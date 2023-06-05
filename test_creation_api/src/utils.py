import openai


def generate_with_chat_gpt(
    prompt: str, max_tokens: int = 64, temperature: float = 1.0
) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content
