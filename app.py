from flask import Flask, request, jsonify
from web_scrap import TVRankScraper
import os

app = Flask(__name__)
scrapper = TVRankScraper()


@app.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the TV Ranking API'
    )


@app.route('/ratings', methods=['GET'])
def ratings_route():
    """return ratings for date, category, area"""
    date = request.args.get('date')
    category = request.args.get('category')
    area = request.args.get('area')

    print(f"{date}, {category}, {area}")

    ratings = scrapper.get_ratings(date, category, area)

    return jsonify(
        ratings
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
