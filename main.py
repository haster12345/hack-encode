import aivm_client as aic

MODEL_NAME = "BertTinySentimentMARKET"
results_map = {
    0: 'sell',
    1: 'hold',
    2: 'buy'
}


def get_prediction(news_input:str) -> [int, str]:
    tokenized_input = aic.tokenize(news_input)
    encrypted_input = aic.BertTinyCryptensor(tokenized_input[0], tokenized_input[1])
    results = aic.get_prediction(encrypted_input, MODEL_NAME)
    bin_value = results.numpy().argmax()
    return bin_value, results_map[bin_value]


def back_test():
