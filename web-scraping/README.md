# Fandom Wikipedia Webscraping Assignment

## Purpose

The purpose of this Python script is to webscrape relevant information from the Undertale Fandom Wiki.
- **Undertale** is an indie game developed by Toby Fox and was released in 2014 on Steam. It was a major part of my middle school experience, and dozens (if not hundreds) of YouTubers created game playthroughs during this time, alongside other passionate fans who further contributed to the fandom with musical transcriptions of the game music/fanart/etc.

What makes these boss characters unique is that the player is not guarunteed a "boss" encounter with every villain: the encounters can vary drastically, depending on the player's previous interactions with minor "fightable" monsters. I believe this boss character information can prove to be very useful to researchers as they attempt to analyze each character as unique narrative markers across the 3 different routes within the game: the Pacifist route, the Neutral route, and the Genocide route.

## Checking the robots.txt file
- Link to robots.txt: https://undertale.fandom.com/robots.txt 
- **Allows**: user-agent * (all webscrapers), API access (api.php?), 
- **Noindex**: templates, user profiles, help pages
- **Disallow**: Special, User_talk, User profiles, Discussion pages, etc; does not allow SemrushBot, GPT, Google-Extended, and Perplexity

## Current .py Progress
- As of **11/16/2024**: The .py script scrapes all of the character names (and their corresponding links) found on the Boss page, and is saved in alphabetical order.
- **Works in Progress**: While this script is capable of saving all the characters into a CSV file, this is simply my minimum viable product. In my downtime, I hope to mess around a little more with the .py script and figure out how to (1) categorize the boss characters into their sub-categories, such as midbosses and minibosses, and (2) display the data in a more reader-friendly format, potentially using tables. 