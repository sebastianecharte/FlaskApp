from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://c.tenor.com/6tlB3xGf1AoAAAAM/cat-white.gif",
    "https://c.tenor.com/2v1aDCelTJgAAAAM/cat-cats.gif",
    "https://c.tenor.com/lolcvIC490YAAAAM/happy-smile.gif",
    "https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif",
    "https://c.tenor.com/e_cOg0wWyQUAAAAM/cat-finger.gif",
    "https://c.tenor.com/Bid8b-ni4EMAAAAM/cat-cat-standing.gif",
    "https://c.tenor.com/_vG3rPAG2v4AAAAM/cat-cat-attack.gif",
    "https://c.tenor.com/ZGld2C6W3O8AAAAM/cat-fight.gif",
    "https://c.tenor.com/TPDruIOzoEkAAAAM/kitten-smol.gif",
    "https://c.tenor.com/1B2lKBCpZnIAAAAM/billu-billu-fight.gif",
    "https://c.tenor.com/ZyKrjlLW-t8AAAAM/cat-cats.gif",
    "https://c.tenor.com/OlM-1hGiioMAAAAM/skate-skateboard.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")