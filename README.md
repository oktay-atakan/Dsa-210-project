# The Impact of Game Soundtracks on Player Reception

Project Overview
-----------------------------------------------------
This project explores whether there is a impact of a game soundtrack on player reception. Using the data of game reviews and comparing them with "Great Soundtrack" tags, popularity of the soundtrack and nominations or awards of that game in soundtrack related categories; difference between reviews of the games with great and popular soundtrack and the games without them will be analyzed.

While working on a video game, companies always use large amount of resource their game soundtracks. For instance, Valve had a 'Valve Studio Orchestra' for their soundtracks, programmer of a game named 'Doki Doki: Literature Club' was originally composer and wrote a story where he can use the elements of soundtrack efficiently. Therefore, understanding whether there is a effect of game soundtrack on the market of the game is essential in high paying game industry.

The primary goal is understanding if there is a relationship between great and popular soundtracks and the percentage of positive game reviews. Since video game industry is a wide range and high price industry, it is important to understand that is it worth to money and effort that is put on the soundtrack of a game.

-----------------------------------------------------
Motivation
-----------------------------------------------------
As a musician, I've always been interested in game soundtracks. I like listening them, playing them myself with my instrument and try to compose soundtracks which can be used in games. Therefore, this is a topic which I am interested in personally. Because I am interested in game soundtracks, I have developed scientific curoisty about their effects too. Since I like to compose game soundtracks I am curious about how they or do they make difference on a game.

-----------------------------------------------------
Research question
-----------------------------------------------------
Does the visibility or quality of a video game soundtrack have an influence on player reception?

Sub-questions:

Do games with the “Great Soundtrack” tag on Steam receive higher review scores than others?

Is there a relationship between original soundtrack visibility measured by YouTube view counts and game ratings?

Do award-winning or nominated soundtracks correlate with higher critical reception?

-----------------------------------------------------
Hypothesis
-----------------------------------------------------
The soundtrack of a video game affects player reception and has an impact on the game reviews and game ratings.

-----------------------------------------------------

Data Collection & Sources
-----------------------------------------------------
The project will rely on publicly accessible APIs and web data.

Game Metadata (Rawg.io API)

- Game Title
- Release Year
- Metacritic ratings
- Rating
- Genre

User Reviews and Tags (Steam API)

- Review score
- Review count
- 'has_great_soundtrack' tag

Soundtrack Visibility (YouTube Data API)

- View count of Main Theme/Original Soundtrack videos

Award and Soundtrack Info (Wikipedia/VGMdb)

- Existence of any award/nomination
- Existence of Original Soundtrack

Methodology
------------------------------------------------------
The collected data will be cleaned, merged and analyzed to explore the relationship between soundtrack related factors and player reception. First, data will be gathered from the mentioned API's and web sources. Each dataset will be constituted by data such as ratings, 'great soundtrack' tag, game title, release year etc.

After data collection, missing and duplicated data will be handled and datasets will be merged using common collumns like release year, game title.

When data is ready, exploratory data anlysis (EDA) will be performed to visualize, distributions and patterns between review scores and soundtrack related data.

Statistical tests will be performed to show obvious differences between games with 'great soundtrack' tag and games without it, the games whose soundtrack is popular and whose aren't, award winning or nominated soundtracks and others.

Finally, regression analysis will be implied to compare all data together and answer the main research question.
