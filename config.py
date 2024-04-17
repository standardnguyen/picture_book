from openai import OpenAI
import os

name_of_book = "whitenights"
full_book_txt = "whitenights_full.txt"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model_to_use = "gpt-3.5-turbo-0125"
backup_model = "gpt-4-turbo"
image_model = "dall-e-3"

image_genre = "Expressionism"

# synopsis = '''
# "White Nights" by Fyodor Dostoevsky is a short story that revolves around the emotional journey of its unnamed narrator, often referred to as the Dreamer. Set in St. Petersburg, Russia, during the season of the white nights—those bright summer evenings when the sun barely sets—the story unfolds over four nights and one day.

# The Dreamer, a lonely, introverted young man prone to fantasy, encounters a young woman named Nastenka, who is crying on a bridge. He learns that she is waiting for the return of a man she loves, who promised to marry her after a year's absence. Over the course of four nights, Nastenka and the Dreamer become close; she shares her anxieties and hopes, while he listens and provides comfort, finding joy in the companionship that has eluded him in his solitary life.

# As the Dreamer falls in love with Nastenka, he imagines a future with her, but on the final night, the man Nastenka loves returns. Realizing his romantic hopes are unattainable, the Dreamer decides to remain content with the friendship they have formed. The story ends with the Dreamer resuming his solitary life, touched by this brief connection but resigned to his loneliness.
# '''

synopsis = '''
Fyodor Dostoyevsky's novel "The Gambler" tells the story of Alexei Ivanovich, a tutor in the employ of a Russian general. Set in the fictional town of Roulettenburg, a European spa destination with a bustling casino, the story delves into Alexei's compulsive gambling and his tumultuous relationships.

Alexei is infatuated with the General's ward, Polina Alexandrovna, who manipulates his emotions and prompts him to gamble on her behalf. The General himself is waiting for a rich aunt, Madame de Cominges, to die so he can inherit her wealth and pay off his debts. He is also engaged in a relationship with a Frenchwoman named Blanche, who is primarily interested in his anticipated inheritance.

As the plot unfolds, Alexei experiences both significant wins and losses at roulette, reflecting his erratic fortunes in love and life. His gambling addiction is portrayed as an emotional rollercoaster that mirrors his desperate attempts to satisfy Polina’s demands and his own quest for self-worth.

Ultimately, "The Gambler" explores themes of addiction, love, desperation, and the influence of money on personal and social relations. The novel draws heavily on Dostoyevsky's own experiences with gambling, making it a deeply personal reflection on compulsion and control.
'''
