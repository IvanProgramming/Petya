from bs4 import BeautifulSoup
import requests

class Joke:
    @staticmethod
    def get_random_joke():
        r = requests.get("https://www.anekdot.ru/random/anekdot/",
        headers={
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.101 Safari/537.36"
        })
        bs = BeautifulSoup(r.content, "lxml")
        for i in bs.select(".topicbox"):
            joke = i.select_one(".text")
            if joke:
                return "\n".join(filter(lambda x: str(x) != "<br/>", joke.contents))

