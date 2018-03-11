from instapy import InstaPy
from pyvirtualdisplay import Display
from time import time, strftime
import emoji

# Logs you in with the specified username and password of your IG account
insta_username = 'type your username'
insta_password = 'type your password'

# Logging in using your credentials...
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

session.login()

# MODE 1 --> Like feed & follow users
# MODE 2 --> Like feed & interact with users
# MODE 3 --> Unfollow users (don't use a lot of time MODE 3!!)

# Select your MODE to execute the code (** no more than 1000 likes per day **)
mode = 1

# Settings for the insta-bot
time_now = strftime("%H:%M")
start_worktime = '10:00'
finish_worktime = '16:30'
session.set_dont_like(['sex', 'girl'])
session.set_ignore_users(['username', 'username', 'username', 'username'])

while True:
    if start_worktime < time_now < finish_worktime:
        if mode == 1:
            # Number of likes per each hashtag!!
            session.like_by_tags(['hashtag'], amount=50, media='photo')
            # Default enabled=False, follows ~ every 10th user from the images
            session.set_do_follow(enabled=True, percentage=20)
            time.sleep(1000)

        elif mode == 2:
            # Visits the author's profile page of a certain post and likes a given number of his pictures
            session.like_by_feed(['hashtag'], amount=50, randomize=True, unfollow=True, interact=True)
            time.sleep(1000)

        elif mode == 3:
            session.unfollow_users(amount=8)
            # Instagram will only unfollow 10 before you'll be 'blocked for 10 minutes'
            # ** if you enter a higher number than 10 it will unfollow 10, then wait 10 minutes and will continue then **
            time.sleep(1200)

    else:
        print ('Out of worktime... Waiting till tomorrow')
        # end the bot session
        session.end()
