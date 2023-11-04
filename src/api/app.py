from flask import Flask

from src.process.SeleniumEdge import ShopeeSeleniumEdge
from src.trash.ShopeeNoLogin import Crawl

app = Flask(__name__)

shopee = Crawl()

seleniumEdge = ShopeeSeleniumEdge()


@app.route("/api/v1/data")
def home():
    return seleniumEdge.crawl_data_edge()


if __name__ == "__main__":
    app.run(debug=True)
