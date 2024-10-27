import pandas as pd


MODEL_NAME = "BertTinySentimentMARKET-REWORK-2"
results_map = {
    0: 'sell',
    1: 'hold',
    2: 'buy'
}


def get_prediction(news_input: str) -> [int, str]:
    import aivm_client as aic
    tokenized_input = aic.tokenize(news_input)
    encrypted_input = aic.BertTinyCryptensor(tokenized_input[0], tokenized_input[1])
    results = aic.get_prediction(encrypted_input, MODEL_NAME)
    bin_value = results.numpy().argmax()
    return bin_value, results_map[bin_value]


def _get_predictions_model(news_input):
    """"
    dummy function
    """
    return 1, 'buy'


def back_test(df: pd.DataFrame, initial_cash_value=1000, predictions_engine='nillion'):
    stock_val = df['Price'][0]
    cash_value = initial_cash_value - stock_val
    cheapest = float("inf")
    return_vals = [1]

    if predictions_engine == 'nillion':
        get_preds = get_prediction
    else:
        get_preds = _get_predictions_model

    for i, article in enumerate(df['Article']):
        signal = get_preds(article)[1]
        if i == 0:
            continue

        price = df['Price'].iloc[i]
        prev_price = df['Price'].iloc[i - 1]
        stock_val *= 1 + ((price - prev_price) / prev_price)

        if signal == 'buy':
            stock_val += price  # buy 1 share
            cash_value -= price  # decrease cash value by 1 share
        else:
            cheapest = min(cheapest, price)
            net = (price - cheapest)/price  # calculate the profit/loss percentage change
            cash_value += cheapest*net
            stock_val -= cheapest

        return_vals.append((cash_value + stock_val)/initial_cash_value)

    return return_vals
