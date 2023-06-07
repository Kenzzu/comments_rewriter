import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"
result = []


def process_line(line: str):
    """
    Process a line of text and rewriteit using OpenAI's
    text-davinci-003 model.

    Args:
        line (str): The input text to be rewritten.

    Returns:
        str: The rewritten text.

    Raises:
        Exception: If an error occurs during the OpenAI completion generation.
    """
    try:
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=(
                f'rewrite this text in other words on Russan language: '
                f'{line}'
                ),
            max_tokens=2054,
            temperature=0.2,  # степень случайности
            top_p=1,
            frequency_penalty=0.5,  # штраф за повторение
            presence_penalty=0.5  # штраф за включение фраз
        )
        return completion.choices[0].text.replace("\r", "").replace("\n", "")
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def main():
    """
    Main function to process the input file and generatethe rewritten
    output file.
    """

    with open('data/input.txt', 'r') as input_file:
        for counter, line in enumerate(input_file, start=1):
            processed_line = process_line(line)
            if processed_line:
                result.append(processed_line + "\r")
            print(counter)

    with open('data/result.txt', "w") as output_file:
        for line in result:
            output_file.write(line)


if __name__ == '__main__':
    main()
