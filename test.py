from moodmatch import MoodMatch

#api is needed for synonym search http://words.bighugelabs.com/api.php
moodmatch = MoodMatch({'api_key': '17b4ea0267a290e34b3645db71e17f3f'})


def run_tests():
    """
    This test is against the film "The Shawshank Redemption"
    reviews.txt contains 3 reviews for that content

    opinions must match the content testing against.
    the more opinions you have, the greater the accuracy.
    """
    search_mood = 'touching'

    f = open('reviews.txt')
    opinions = f.read()

    match = moodmatch.match(search_mood, opinions)

    if match is True:
        print('This content is ' + search_mood)
    else:
        print('This content isn\'t ' + search_mood)

if __name__ == '__main__':
    run_tests()