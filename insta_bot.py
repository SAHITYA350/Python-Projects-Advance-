from instabot import Bot
bot = Bot()
bot.login(username="sahitya_215", password="Babu1#_oppo")
bot.follow('ezsnippet')
bot.upload_photo("C:/Users/Sahitya/OneDrive/Pictures/Ghibli(Me).jpg", caption="I love code")
bot.unfollow("ezsnippet")
bot.follow("_somen_das_")
bot.send_message("I love python", ["_somen_das_","debanjan657"])

followers = bot.get_user_followers("sahitya_215")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("sahitya_215")
for followings in following:
        print(bot.get_user_info(followings))