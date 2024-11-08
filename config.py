from openai import OpenAI
import os

name_of_book = "thegambler2"
full_book_txt = "thegambler_fullv2.txt"
client = OpenAI(api_key="")
model_to_use = backup_model = "gpt-4o-mini"
image_model = "dall-e-3"

image_genre = "Expressionist"
image_genre_expansion = "This genre often uses vivid colors, exaggerated forms, and dramatic, sometimes distorted imagery to express the inner feelings of the characters or themes."
race_tune = "Russian, but make sure it's not a caricature"

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

# synopsis = '''
# "Notes from Underground" by Fyodor Dostoevsky is a short novel and one of the first existentialist works, divided into two parts. It is often regarded as a profound psychological exploration of the individual.

# Part One is titled "Underground" and serves as an extended monologue by the narrator, known as the Underground Man, who is a retired civil servant living in St. Petersburg. This section is more philosophical and is structured as a series of ruminations and arguments. The Underground Man discusses his views on free will, suffering, rationality, and human nature. He presents himself as an outsider to society, who despises the world around him yet feels painfully self-aware and unable to withdraw completely. His insights are bitter and cynical, critiquing the idea that human society can be improved through science and rationalism, which he sees as overly simplistic and blind to the chaotic, irrational depths of human nature.

# Part Two, "Apropos of the Wet Snow," shifts into a more narrative style, recounting events from the Underground Man’s life when he was about 24 years old. It provides concrete examples of his earlier philosophical musings. This part tells of his interactions with old schoolmates and a young woman named Liza, whom he meets during a visit to a brothel. His relationships are marked by manipulation, cruelty, and pride, yet they also reveal his profound loneliness and desire for connection, which he ultimately sabotages himself. Through his encounters with Liza, particularly, the Underground Man exemplifies his own theories about the self-destructive impulses and desire for suffering he previously theorized about.

# The novel ends with the Underground Man bitterly critiquing his own narrative, unsure of whether he has accomplished anything through his confessions. This narrative style and the themes Dostoevsky explores deeply influenced modern existentialist and post-modern thought, focusing on the complex, often contradictory nature of human consciousness and the limitations of purely rational systems in understanding humanity.

# '''