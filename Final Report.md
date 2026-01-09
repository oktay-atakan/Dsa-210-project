# The Impact of Game Soundtracks on Player Reception

Final Report            
----------------------------- 


## Motivation

As a musician, I've always been interested in game soundtracks. I like listening them, playing them myself with my instrument and try to compose soundtracks which can be used in games. Because I am interested in game soundtracks, I have developed scientific curoisty about their effects too. Since I like to compose game soundtracks I am curious about how they or do they make difference on a game. I wondered are the games with better soundtracks make difference. Details which makes a game better and qualified but cost lot of effort to put on for just a detail such as soundtrack playing while gamer try to complete a mission, the story moving forward while gamers just focused on their gameplay, the vievs in background which may be overlooked are might be very interesting when we think about the effort and money put on them. The question is, is it really worth to put so much effort on things that might just be overlooked or are they the real differences of a great game between average game? Therefore, I was motivated to research how big is the difference these details make focusing mainly on soundtrack.

## Data Sources

Data has driven from multiple sources such as RAWG Video Games Database (RAWG API), Steam Store API, Steam Search API (Steam Community), Steam Spy API. As it can be observed in the 01_data_collection notebook, data collection and dataset construction were carried out in four main steps:

Step 1 – Core Game Metadata (RAWG API)
First, core game-level metadata was collected from the RAWG API.
Extracted columns from RAWG:

  - Game name
  - Release date
  - User rating
  - Rating count
  - Genre information
  -Metacritic score (when available)

Step 2 – Critic and Commercial Data (Steam Store API)
Next, critic-based and commercial information was retrieved from the Steam Store API.
Extracted columns from Steam Store:

  - Steam AppID
  - Game price and free-to-play status
  - Metacritic score
  - Steam category and tag information
  - “Great Soundtrack” tag (when available)

Step 3 – Dataset Matching and Merging
To merge RAWG and Steam datasets, each game was searched by name using the Steam search endpoint in order to retrieve its Steam AppID.

  - Games that could not be matched to a Steam AppID were excluded.
  - The two datasets were then merged using the Steam AppID as a key.

This step ensured consistency between RAWG and Steam data sources.

Step 4 – Tag Enrichment (SteamSpy API)

Finally, the dataset was enriched using the SteamSpy API, which provides community-driven tag information.
Extracted user-perceived tags:

  - Great Soundtrack
  - Story Rich
  - Atmospheric

These tags were converted into binary indicators and used as both:

  - Predictive features
  - Target variables in the supervised learning task

## Data Anlaysis

As can be observed in EDA analysis and hypothesis testing notebooks, after data collection and merging was finished, data analysis was concudted on dataset. By graphing, scattering plots, using tables, comparing variables it was aimed to understand data beter, observe distributions of information in dataset, test hyphothesis and mark prediction and target variables for ML tasks.

### Dataset Overviev:
The final dataset consists of game-level observations obtained by merging multiple data sources as can be seen in 'final_merged_dataset_extended.csv'. The dataset includes the following columns:

  - rawg_id
  - name
  - released
  - rating
  - ratings_count
  - metacritic
  - genres
  - steam_id
  - appid
  - steam_name
  - is_free
  - price
  - price_numeric
  - metacritic_score
  - has_great_soundtrack
  - has_story_rich
  - has_atmospheric

Each row represents a single video game, and these variables are used throughout the exploratory analysis and supervised learning stages.

### Distributions of Key Variables

User ratings are mostly concentrated within a narrow range, indicating that most games receive moderately high ratings. Metacritic scores are more limited in number and show greater variability. Game prices are right-skewed, with many games priced low or offered for free, which motivated converting price information into a numeric format for analysis.

### Analysis of th Target Variable

The imbalance in the 'has_great_soundtrack' variable suggests that accuracy alone would not be an appropriate evaluation metric. This observation motivated the use of precision, recall, and F1-score in the supervised learning stage, as well as class-balancing techniques.

### Comparison Between Games With and Without Great Soundtracks

Games tagged as having a great soundtrack tend to receive higher average user ratings and higher Metacritic scores compared to games without this tag. In contrast, no clear or consistent difference is observed in game prices between the two groups. This suggests that soundtrack quality is more closely related to player and critic reception than to pricing. Which leads and points the hypothesis that were built at the start. Supporting to reject the null hyptohesis.

### Feature Relationships

A positive relationship is observed between user ratings and Metacritic scores, indicating general agreement between players and critics. The relationship between price and ratings appears weak. Additionally, the story rich and atmospheric tags frequently co-occur with the “Great Soundtrack” tag, suggesting a connection between narrative elements, atmosphere, and perceived soundtrack quality.

### Summary of EDA Findings

Overall, the exploratory analysis indicates that games with great soundtracks are generally associated with higher user and critic evaluations. The observed patterns support the use of supervised classification to further examine whether these features can jointly predict the presence of a great soundtrack.

## Findings

### Hyphothesis Testing Results

To evaluate the hypothesis, as can be observed in hypothesis testing notebook, games tagged as having a Great Soundtrack were compared with games without this tag in terms of user ratings and Metacritic scores. The analysis shows that games with the Great Soundtrack tag tend to have higher average user ratings and higher Metacritic scores. This pattern is consistently observed across both player-based and critic-based evaluation metrics.

These differences suggest that the presence of a great soundtrack is associated with better reception, supporting the hypothesis that soundtrack quality contributes to how qualified a game is perceived.

### Machine Learning

The supervised classification model further supports this finding. Using user ratings, rating counts, Metacritic scores, and thematic tags as input features, the model was able to predict the presence of the Great Soundtrack tag with a Macro F1-score of approximately 0.73. This indicates that the soundtrack-related label is not random, but instead systematically related to observable indicators of game quality and reception as can be observed in notebook named 'ML_task_supervised.ipynb'.

Additionally, the model’s ROC-AUC score of approximately 0.68 demonstrates that games with great soundtracks can be distinguished from other games better than random guessing based on these features alone.

### Conclusion

Taken together, both the comparative analysis and the supervised learning results supports the alternative hypothesis. Games with great soundtracks are more likely to receive higher user and critic evaluations, suggesting that soundtrack quality plays a meaningful role in overall player reception. While the relationship is not deterministic, the observed patterns indicate that soundtrack quality is an important component of perceived game quality.

## Limitations and Future Work

One of the key limitations in the project was evaluating a sound track which is a challenge since it is subjictive. This could be fixed by trying to collect a dataset with more games (aka same dataset with more rows) or adding more information about games soundtracks such as awasrd nominations, crtics and rating scores about them, popularity information of a spesific soundtrack by investigating view count at Youtube (aka more columns in dataset specificly about soundtrack informations). By completing these, analayzing the effect of the soundtrack would be more accurete, and more precise.

As a development and future work, 'has_story_rich' and 'has_atmospheric' tags could be also evaluated as we done for 'has_a_great_soundtrack' tag. By completing these evaluations, we can conclude that wether narrative components of a game makes a game more likeable, more playeble, even more marketable. It could answer the question of 'Does it really matter to put so much effort on a story that nobody will care, music that nobody will listen and creating an atmosphere that nobody will feel its existence?'. These analysis may guide a game developer and remind them what is important and which features make a game special for a gamer.

## References

In this project, Chat GPT is used in order to finalize the code structures, organize the outputs of outputs, to visualize and making data readable. Prompts, answers and chats with Caht GPT is documented and archived.

All data sources used in this project are publicly accessible and were collected for academic purposes only.

### Data Sources

  - RAWG Video Games Database API,
https://rawg.io/apidocs,
Used to collect core video game metadata including release dates, genres, ratings, and Metacritic scores.
  - Steam Store API,
https://store.steampowered.com/api/appdetails,
Used to retrieve Steam-specific game information such as pricing, availability, and critic scores.
  - Steam Community Search API,
https://steamcommunity.com/actions/SearchApps,
Used to match video game titles with their corresponding Steam App IDs.
  - SteamSpy API,
https://steamspy.com/api.php,
Used to collect user-generated tag information such as Great Soundtrack, Story Rich, and Atmospheric.

### Tools and Libraries
  - scikit-learn,
Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research.
Used for supervised learning, model evaluation, and performance metrics.
  - pandas,
McKinney, W. (2010). Data Structures for Statistical Computing in Python.
Used for data cleaning, merging, and analysis.
  - NumPy,
Used for numerical operations and data processing.
  - Matplotlib & Seaborn,
Used for data visualization during exploratory data analysis.

### Course Materials

  - DSA 210 – Data Science and Analytics,
Lecture slides and course materials provided by Sabancı University.


