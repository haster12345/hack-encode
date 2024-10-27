from argparse import ArgumentParser

import pandas as pd

from predictions import back_test, get_prediction
from scrape import parse_article


def main(url):
    if url:
        article = parse_article(url)
        return print(get_prediction(article))

    else:
        df = pd.read_csv('../stonks.csv')
        return_val = back_test(df, predictions_engine='')
        return return_val


if __name__ == '__main__':
    parser = ArgumentParser(
        prog='AnonymizedTrading',
        description='Anonymized Trading of Stocks using a NLP model to analyse Financial News Sentiment'
    )

    parser.add_argument('--url', default=None)
    args = parser.parse_args()

    main(args.url)


