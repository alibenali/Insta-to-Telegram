import instaloader, time
from datetime import datetime, timedelta
import instaloader

#  SETTUP
principal_account = "aliben24_"
session = "session-aliben24_"
scraping_account = "aliprod29"



# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.load_session_from_file(username=principal_account,filename=session) # (load session created w/
                               #  `instaloader -l USERNAME`)


# Define the profile name of the account to download from
profile_name = input('Profile username: ') or scraping_account
# Log in to Instagram (optional)
min_date = datetime.now() - timedelta(days=1)

while True:
    try:
        L.download_profile(profile_name, 
                    profile_pic=True, profile_pic_only=False, post_filter=lambda post: post.date_utc >= min_date, download_stories= True, fast_update=True)
        time.sleep(200)
    except:
        pass