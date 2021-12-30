### this was a giveaway for women who commented on my tweet
### twitter api does not support comment lookup at this time
### 12/30/21
import getpass
import random

women_commenters = getpass.getpass(prompt = "Provide commenters: ").split()

winners = random.choices(women_commenters, k=2)

for winner in winners:
    print(winner)