from web_scrap import TVRankScraper
import pytest


@pytest.fixture
def scraper():
    return TVRankScraper()


def test_get_ratings_with_valid_parameters(scraper):
    # Very first test for scraper is working
    ratings = scraper.get_ratings("20221001", 1, 1)
    assert len(ratings) == 20
