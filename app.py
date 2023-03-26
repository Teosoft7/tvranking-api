from flask import Flask, request, jsonify
from web_scrap import TVRankScraper
import os
from flask_cors import CORS

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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
