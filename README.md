In our project, we deploy a pre-trained BertTiny model to AIVM, with the intention to predict whether to buy, sell, or hold stocks based on financial news articles. The purpose of using AIVM (AI Virtual Machine) in this project is to efficiently deploy the BERTTiny model, enabling real-time predictions for stock trading decisions (based on financial news). In this project, Nillion is used to ensure secure, decentralised data processing and sharing. By leveraging Nillion's technology, the sensitive financial data and model computations remain private and protected, which is critical in the financial domain where security and data integrity are paramount.

In this project, backtesting simulates the performance of our BERT-based model’s stock trading decisions (buy, sell, hold) over time using historical financial news data. The backtesting function starts with an initial cash value and iterates through each news article in the dataset, simulating trades based on model predictions. By calculating changes in stock value relative to the initial stock price, it provides a record of returns to evaluate the model’s decision-making effectiveness. Integrating Nillion enhances this process with an added layer of security and decentralization. Nillion's technology ensures that sensitive financial data and computations are processed securely, reducing risks of data breaches. This decentralized structure supports private, secure prediction processing, even in large-scale simulations, maintaining data integrity and privacy standards. By anonymizing data and trading decisions, Nillion safeguards confidentiality in financial applications.

<img src="https://media.discordapp.net/attachments/419923179985960970/1300047468880330813/image.png?ex=671f6b0e&amp;is=671e198e&amp;hm=28c540ef46d1b7acd995e917daf6e2fc7520583ca20ba9b411fb90410e423ac5&amp;=&amp;format=webp&amp;quality=lossless&amp;width=1025&amp;height=89" alt="Image"/>

Additionally, we provide a Command Line Interface (CLI) tool that allows users to input a URL of a financial news article. Our tool, given an article, scrapes the web to generate real-time predictions (buy, sell, or hold) based on the content of the article.


<img src="https://media.discordapp.net/attachments/419923179985960970/1300043120645374034/image.png?ex=671f6701&amp;is=671e1581&amp;hm=9c3d44ea99621ae434cbf59fd2f361eb890baaed9cdecaebad9a835c14df646d&amp;=&amp;format=webp&amp;quality=lossless&amp;width=706&amp;height=411" alt="Image"/>![image](https://github.com/user-attachments/assets/071a785f-e250-4b63-b638-ca5b602e4c1b)

This graph shows the backtested results of our algorithm, showing how our model predicts the return of stock values over time. These results can be improved over time, by training the model further, using more data, and evolving our backtesting algorithm to more accurately reflect trends.













