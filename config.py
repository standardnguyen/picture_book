from openai import OpenAI
import os

name_of_book = "whitenights"
full_book_txt = "whitenights_full.txt"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
model_to_use = "gpt-3.5-turbo-0125"
backup_model = "gpt-4-turbo"
image_model = "dall-e-3"

synopsis = '''
"White Nights" by Fyodor Dostoevsky is a short story that revolves around the emotional journey of its unnamed narrator, often referred to as the Dreamer. Set in St. Petersburg, Russia, during the season of the white nights—those bright summer evenings when the sun barely sets—the story unfolds over four nights and one day.

The Dreamer, a lonely, introverted young man prone to fantasy, encounters a young woman named Nastenka, who is crying on a bridge. He learns that she is waiting for the return of a man she loves, who promised to marry her after a year's absence. Over the course of four nights, Nastenka and the Dreamer become close; she shares her anxieties and hopes, while he listens and provides comfort, finding joy in the companionship that has eluded him in his solitary life.

As the Dreamer falls in love with Nastenka, he imagines a future with her, but on the final night, the man Nastenka loves returns. Realizing his romantic hopes are unattainable, the Dreamer decides to remain content with the friendship they have formed. The story ends with the Dreamer resuming his solitary life, touched by this brief connection but resigned to his loneliness.
'''
