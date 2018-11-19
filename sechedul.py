import time
import sechedul

import django

django.setup('daydayup.settings')

from historytoday.tasks import *

sechedul.every().day.at('11:37').do(save_story_db)

while True:
    sechedul.run_pending()
    time.sleep(1)
