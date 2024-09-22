"""
File:    twitter_ats.py
Author:  Abby Joseph
Date:    3/15/2022
Section: 31
E-mail:  abbyj1@umbc.edu
Description: This program takes user inputted tweets to display the usernames at-ed and the
             hashtags used.
"""
EXIT_STRING = 'quit'
USER_LIST = 0
HASHTAG_LIST = 1


def twitter_ats(the_tweet):
    """
         A function to create a 2D list of the usernames and hashtags in a tweet
         :param the_tweet: the tweet to check for usernames and hashtags
         :return: a 2D list of the usernames and hashtags used
    """
    tweet_list = the_tweet.split()
    username_list = []
    hashtag_list = []
    combined_user_hashtag_list = []
    for word in tweet_list:
        if '@' in word and '#' in word:
            tweet_list.remove(word)
        elif '@' in word and word not in username_list:
            username_list.append(word)
        elif '#' in word:
            hashtag_list.append(word)
    temp_usernames = ''.join(username_list)
    username_list = temp_usernames.split('@')
    temp_hashtags = ''.join(hashtag_list)
    hashtag_list = temp_hashtags.split('#')

    for name in username_list:
        if name in ['']:
            username_list.remove(name)
    for tag in hashtag_list:
        if tag in ['']:
            hashtag_list.remove(tag)

    combined_user_hashtag_list.append(username_list)
    combined_user_hashtag_list.append(hashtag_list)

    return combined_user_hashtag_list


if __name__ == '__main__':

    tweet = input('What do you want to tweet? ')
    while tweet.lower() != EXIT_STRING:
        user_string = ', '.join(twitter_ats(tweet)[USER_LIST][:])
        hashtag_string = ', '.join(twitter_ats(tweet)[HASHTAG_LIST][:])
        print(f'The users are: {user_string}')
        print(f'The hashtags are: {hashtag_string}')
        tweet = input('What do you want to tweet? ')
