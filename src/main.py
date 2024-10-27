from argparse import ArgumentParser
import predictions
from scrape import parse_article


def main(url):
    if url:
        print("Scraping Data")
        article = parse_article(url)
        print("Predicting Sentiment")
        return print("Model recommendation is to " + predictions.get_prediction(article)[1])


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='AnonymizedTrading',
        description='Anonymized Trading of Stocks using a NLP model to analyse Financial News Sentiment'
    )

    parser.add_argument('--url', default=None)
    args = parser.parse_args()

    main(args.url)


