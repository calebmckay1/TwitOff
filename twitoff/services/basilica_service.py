from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BASILICA_API_KEY')


if __name__ == "__main__":


connection = Connection(API_KEY)
print('CONNECTION', type(connection))

embeddings = list(connection.embed_sentences(tweets)

print(embeddings)

breakpoint