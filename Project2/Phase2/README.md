# Phase 2

### MVP:
Design a product which is able to extract a specific user information from Twitter by using existing Twitter API and perform a sentimental analysis by using Google NLP API. By using this product, the Twitter developer and marketing management team are able to find a specific user’s tweets by entering user’s username and notice all his/her tweets’ sentiments and thus the developer is able to improve the algorithm to provide tweets that user is interested in and members in the marketing management team is able to identify when and how to engage with the user directly, such as finding more related advertisements for users and this way increasing the company’s profit.

### Users:
APP's developer and marketing management team

### User stories:
As a developer, I want to know the sentiment of users' tweets, so that I can improve the algorithms to provide more related tweets.
As a developer, I want to find a specific user's tweets, so that I can provide tweets to that user.
As a member of marketing management team, I want to know the users' attitude towards posts, so that I can find more related advertisements to increase the profit.

### Design:
The client can enter a twitter user’s username and then Apply the Twitter API to extract information from a specific user and save this user’s tweets content into a CSV file. Read the content in the CSV file and use Google NLP API to analyze the sentiments of each tweet.

### Test:
The output of CSV file
 A snapshot of the csv file
The output of python script, which shows the sentiments of texts
 A snapshot of sentimental analysis
 
 
### Reference:
https://www.youtube.com/watch?v=Lu1nskBkPJU 
https://www.youtube.com/watch?v=iqRgOdJZtiY
