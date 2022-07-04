from flask import Flask
import twint
import twint.output

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Nick"


@app.route("/about")
def about():
    return "<h1>This is about me.</h1>"


@app.route("/hashtag")
def hashtagScraper():
    # Configure
    c = twint.Config()
    c.Hide_output = True
    c.Store_object = True
    c.Username = "Bitboy_Crypto"
    c.Search = "world"

    # Run
    twint.run.Search(c)

    tweetDict = converToDict(twint.output.tweets_list)

    return tweetDict


def converToDict(list):
    print(type(list[0]))
    newDict = {list[i].id: {"tweet": list[i].tweet,
                            "date": list[i].datestamp} for i in range(0, len(list), 2)}
    return newDict


@app.route("/twt")
def twitScrape():
    twitUN = "justinbieber"
    returnable = {
        'profile': None,
        'tweets': []
    }
    c = twint.Config()
    c.Username = twitUN
    c.Hide_output = True
    c.Store_object = True
    twint.run.Lookup(c)
    t = twint.output.users_list
    # returnable['profile'] = (twint.output.users_list[0]).__dict__
    # c2 = twint.Config()
    # c2.Username = twitUN
    # c2.Store_object = True
    # c2.Hide_output = True
    # c2.Limit = 3200
    # twint.run.Search(c2)
    # for tweet in twint.output.tweets_list:
    #     returnable['tweets'].append(tweet.__dict__)
    print(t)
    return convert(t)


@app.route("/user")
def twitUser():
    c = twint.Config()
    c.Username = "justinbieber"
    c.Limit = 100
    c.Store_csv = True
    c.Output = "jb.csv"
    c.Lang = "en"
    c.Translate = True
    c.TranslateDest = "it"
    twint.run.Search(c)


@app.route("/s")
def twitSearch():
    c = twint.Config()


def convert(list):
    dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return dict


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
