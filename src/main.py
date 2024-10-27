from argparse import ArgumentParser
import predictions
from scrape import parse_article


def main(url):
    if url:
        article = parse_article(url)
        return print(predictions.get_prediction(article))


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='AnonymizedTrading',
        description='Anonymized Trading of Stocks using a NLP model to analyse Financial News Sentiment'
    )

    parser.add_argument('--url', default=None)
    args = parser.parse_args()

    main(args.url)


