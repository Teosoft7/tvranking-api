import os
from flask import Flask, jsonify
from flask_cors import CORS
from web_scrap import TVRankScraper


app = Flask(__name__)
CORS(app)
scrapper = TVRankScraper()


@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the TV Ranking API'
    )


@app.route('/ratings/<date>/<category>/<area>', methods=['GET'])
def ratings_date_route(date, category, area):
    print(f'ratings with date : {date}, {category}, {area}')

    ratings = scrapper.get_ratings(date, category, area)

    return jsonify(
        ratings
    )


@app.route('/last8ratings/<channel>/<programme>', methods=['GET'])
def ratings_last8(channel, programme):
    print(f'last 8 ratings of program : {channel}, {programme}')
    return jsonify(
        status=True,
        message="Last 8 ratings for program"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
