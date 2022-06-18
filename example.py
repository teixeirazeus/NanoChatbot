from nanochatbot import NanoChatbot, Rule

train_data = [
    Rule(questions=["Qual é seu nome?", "Quem é você?"], answers=["Meu nome é nanochatbot.", "Nanochatbot."]),
    Rule(questions=["Qual é sua comida favorita?", "Você tem alguma comida favorita?"], answers=["Eu gosto de pizza.", "Adoro pizza."]),
    Rule(questions=["Você é um robô?", "Quem é um humano?"], answers=["Sou uma inteligência artificial", "Sou um chabot."]),
    Rule(questions=["Oi", "Tudo bem?", "Olá"], answers=["Oi", "Tudo bem?", "Olá"]),
    Rule(questions=["Python ou java?", "Python ou C?"], answers=["Python :snake:"]),
]

bot = NanoChatbot()
bot.train(train_data)

while 1:
    i = input(":")
    if i == "q": break
    print(bot.respond(i))
