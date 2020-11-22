# Tweepy
A Personality Development App

## Devpost Link

## Inspiration for our App

Mental illness is a global problem. More than 300 million people, 4.4% of the world’s population, suffer from depression.
According to the National Alliance of Mental Illness (NAMI), approximately one out of five people experiences some type of mental illness each year. We have realised the strong potential Twitter’s resources have in solving one of the biggest problems of today’s  world.

## What is Tweety?

Tweety is a personality development application aimed at bringing users sentiment based recommendations, challenges for personal growth, a place to vent and to notify loved ones when users experience prolonged negative emotions. We use the data from Twitter to monitor our users' feelings.

## User Interface

![Alt text](media\ChatScreen.png? "Title")
![Alt text](media\chat11.png?raw=true "Title")
![Alt text](media\tw.png?raw=true "Title")
![Alt text](media\chat1.png?raw=true "Title")
![Alt text](media\chat.png?raw=true "Title")
![Alt text](media\chat3.png?raw=true "Title")

## Workflow

### Fetch User Tweets

Recent tweets of the user are fetched using the Twitter API through tweepy Python library.

### Sentiment Analysis

The text from tweet is cleaned and analysed is classified as positive, neutral or negative using TextBlob python library. The total percentage of positive, negative and neutral tweets are calculated. 

### Journaling

We provide the users a place to self-reflect and express their emotions.

### Recommendations

Based on the highest percentage of sentiment, movies are recommended to the user. This is implemented through web scraping.

### Challenges

Users are provided challenges for personal development. Completion of a challenge leaves the user with a sense of accomplishment and a tweet is automatically sent out from their account celebrating this.

### Prolonged Negative Emotions

If a user is experiencing prolonged negative emotions:
- Direct Messages are sent out to their chosen contacts asking them to check up on them.
- Mental Health resources are provided to the user.

## Future Scope

- We can use Google's Natural Language API to generate more accurate results. We can train the model with extra datasets to increase accuracy even further.
- We aim to use Google's Recommendation AI over Web Scraping to provide more personalised recommendations.
- We would also like to integrate a chatbot to this application so that users can have a non-judgemental outlet to communicate  with.
- We would like to list out mental health experts and their contact details so that the user can obtain professional help, if required.
