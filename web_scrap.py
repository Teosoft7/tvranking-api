from bs4 import BeautifulSoup
import requests


class TVRankScraper:
    def __init__(self):
        print("TVRankScraper initialized")
        self.status = ""

    def get_ratings(self, date, category, area, test=False):
        """ Get ratings from nielsen Korea """
        """ Returns top rank programs for date, category, area """
        """ date : string (YYYYMMDD) """
        """ category : integer, Channel category(1: terrestrial, 3: cable, 2: general) """
        """ area : integer, Area Code (0: national wide, 1: Great Seoul Area) """

        url_string = f"http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1"
        url_string += f"&sub_menu={category}_1"
        url_string += f"&area={area}&begin_date={date}"

        try:
            response = requests.get(url_string)
            parsed_html = BeautifulSoup(response.content.decode(
                'utf-8', 'replace'), 'html.parser')
            ranking_tb = parsed_html.body.find_all(
                'table', attrs={'class': 'ranking_tb'})

            rows = ranking_tb[0].find_all('tr', attrs={'class': None})
        except:
            print("Eror happend while accessing data on Nielsen.")
            return []

        result = []
        i = 0
        for row in rows:
            i += 1
            if (i <= 2):
                # skip headers
                continue

            # extract row
            items = row.find_all('td')
            rank = items[0].text.strip()
            channel = items[1].text.strip()
            programme = items[2].text.strip()
            rating = items[3].text.strip()

            # convert data to dictionary
            item = {
                'rank': int(rank),
                'channel': channel,
                'rating': float(rating),
                'programme': programme,
                'date': date[:4] + '-' + date[4:6] + '-' + date[6:8]
            }

            if test:
                print(
                    f"TEST MODE : {date} {rank} {channel} {programme} {rating}")

            result.append(item)

        return result
