# NanoChatbot

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d1467b3f64184b72b42df0274e848448)](https://app.codacy.com/gh/teixeirazeus/NanoChatbot?utm_source=github.com&utm_medium=referral&utm_content=teixeirazeus/NanoChatbot&utm_campaign=Badge_Grade_Settings)

Nanochatbot is a simple chatbot with few lines of code, designed to be CPU efficient.

## Installation

```
pip install -r requirements.txt
```

For portuguese support
```
python -m spacy download pt_core_news_lg
```

For english support
```
python -m spacy download en_core_web_lg
```

## Quick Start
```
from nanochatbot import NanoChatbot, Rule

train_data = [
    Rule(questions=["Qual é seu nome?", "Quem é você?"], answers=["Meu nome é nanochatbot.", "Nanochatbot."]),
    Rule(questions=["Qual é sua comida favorita?", "Você tem alguma comida favorita?"], answers=["Eu gosto de pizza.", "Adoro pizza."]),
    Rule(questions=["Você é um robô?", "Quem é um humano?"], answers=["Sou uma inteligência artificial", "Sou um chabot."]),
    Rule(questions=["Oi", "Tudo bem?", "Olá"], answers=["Oi", "Tudo bem?", "Olá"]),
    Rule(questions=["Python ou java?", "Python ou C?"], answers=["Python :snake:"]),
]

bot = NanoChatbot(language='pt')
bot.train(train_data)

while 1:
    i = input(":")
    if i == "q": break
    print(bot.respond(i))
```