# DataIncubator

Are Mainstream media indirectly contributing to the increase of skepticism towards scientific facts?

* Context:

In the current context of strong political and ideological division, the partiality of the media and the style in which the news are presented is (too) frequently questioned. The way people read and apprehend the news is now strongly influenced by their main source of information. While in the past, the general public trusted faithfully and with more or less interest the facts that were delivered to them through their television set by the so-called "mainstream" media, an alarming fraction of them are now eagerly following alternative news outlets.

Although it would be presumptuous to judge certain media (or media anchors) based on their political or personal convictions, there is at least one area when indulgence should be limited: SCIENCE. Our scientific knowledge was built on facts that should be subject to relatively limited or at least constructive questioning. While the proliferation of misinformation is in part due to the rise of fake news and pseudoscience frauds, we have to wonder how mainstream media may have also contributed to the increase of skepticism towards scientists and scientific facts.

Some factors are already quite straight forward to pin down e.g. the search for a certain journalism fairness in reporting both sides of an argument even when only one side is motivated by actual scientific evidence, or the abusive use of sensationalism in misleading scientific headlines that may not reflect the content and seriousness of the results presented in the article. Mainstream media are also often presenting themselves as the voice of scientific reason with a subtle disdain towards people that may have unorthodox opinions, a fact that may just add fuel to the current tensions. 

* Project:

-General goal
The project aims at investigating the influence of mainstream media in the debate between science lovers and skeptics. The aim of this data-driven investigation is to isolate factors (headlines, keywords, tone etc.) that have infuriated the public or provoked some mistrust of mainstream media reports on scientific topics. This project is not only envisaged to be an interesting case of society study. The ultimate goal is to report on these findings to interested stakeholders such as mainstream media outlets that would surely valued such research. 

- Timeliness: 
In the current time of fake news, it is important to understand what could be down to slow down or reverse the process of misinformation of the general public. In anticipation of the fellowship, I will collect tweets and articles as well as comments underneath articles in web based mainstream resources. The data generated over the next few weeks are particularly interesting for this project since the mid-term elections are approaching and discussions about fake news are stronger than ever.

- Impact of the project: 
As mentioned earlier, the outcome of this project will be engaging to the media at large and to people that may be interested in learning what could be done to stop the propagation of nonsense in reports on scientific facts. Knowing how to communicate science well to the general public may be as important as the science itself. As a side note, an exciting product could potentially be offered freely to some media outlets in exchange for advertisement of the DataIncubator fellowship and its sponsors.

- Personal interests: 
As a scientist myself, I value that the general public embraces the advancement of scientific discoveries (and new technologies) rather than fears or disregards them. I am also concerned by the importance of reliable media sources in the communication of science; they are our main mean of public outreach. I am also interested in conducting a project matched to the current context of affairs in the US.

- Technical means to realize such project:

To conduct such project, we will search news articles on scientific topics towards which the reaction of the general public has been strongly positive or negative on the Twittersphere. We expect to isolate the usual science suspects e.g. climate change, efficiency of vaccines etc. We will then confront the content of the public tweets with the original piece of information i.e. a twitter post or the referenced url of a web based news article. In particular cases when the tweet has been particularly popular but refers to a TV reports, we may consider retrieving the corresponding transcripts from the given outlet transcripts archives.

The project will also be conducted in a comparative way with the analysis confronting: 
1- different media outlets and their rhetoric (e.g. CNN versus MSNBC versus FoxNews)
2- English-speaking American versus European news style (e.g. CNN versus BBCNews). Australian media may be included in the analysis if relevant or time allows.

The main challenge of the project is the construction of the dataset. All data are already available online via a variety of archival database but need to be collected. Part of the data will be retrieved prior to the fellowship:
- Tweets can be retrieved through query via a Twitter API in the context of the Twitter developer platform:
https://developer.twitter.com/content/developer-twitter/en.html 
- Web based articles can be retrieved directly via their referenced url on the mainstream media website.
e.g. https://www.nytimes.com/search/
- Most TV transcripts of media outlet are available on the archive system of their website. 
e.g. http://transcripts.cnn.com/TRANSCRIPTS/

Depending on the time available and technical challenges encountered during the project, we will explore a number of area of investigation. Here is a non-exhaustive non-ordered list of topics:
- What are the most controversial scientific topics right now?
- Which media outlet is the subject of the most twitter fire for their science reports? And can we find the reason?
- Is there a difference in tweets and RT behaviors towards scientific articles in US and Europe?
- How long is the impact of an scientific article in time on the Twittersphere etc.

** Example of feasibility:
In order to show the feasibility of the project, I started to retrieve tweets using the tweepy python library for accessing the Twitter API. The tweets were collected based on a search of a pairs of keywords of interest for our analysis i.e. the name of one of six mainstream media outlets: CNN, BBC, FoxNews, CNBC, MSNBC & HBO's "Last Week Tonight" (the last being reknown for their extended piece of investigating journalism that could trigger large amount of comments) and one of the following science-related keywords: 'climate change','vaccines' and 'science'. 

We will extend the database to tweets mentioning the writing press i.e. "The New York Times" and additional keywords. The standard Twitter API only limits the search in the database to the last 7 days so the first exploratory exercises here are conducted on a limited number of tweets. I opened a number of streaming requests to collect tweets as they come in the coming couple of months. The statistics will greatly improved as the tweets come.

For this exercise, we retrieve for each tweet its unique ID, the data of its creation and the text of the tweets itself. The tables are made available at the following link: https://github.com/agalametz/DataIncubator

Exercise 1: What is the frequency of "retweet" RT depending on the media communicating the information? 
- Test: The tweets about 'science', 'climate change' and 'vaccines' were counted for the six distinct media outlets at hand. We determine the percentage of 'RT' tweets among there. The result can be found in "ImpactMediaScienceSkepticism_twitter_interpret_Figure1.png".  
- Conclusion: The RT tend to be more common for media such as 'FoxNews' that are known to use a more alarming rhetoric. We could have also looked at the number of '?' and '!' and upper case for such analysis. We see as well that a show like the 'Last week tonight' also seems to provoke more reaction and follow-up than classic TV media.

Exercise 2: What is the topic (and keywords) that have made people react in tweets concerning 'FoxNews' and 'science'?
- Test: We looked at the tweets in the 'FoxNews_science.json' table and made a clean ranking of the words used in these tweets. The two first words "discovery" and "woman"+"World"+'Transgender' refer to two new articles: 
--"Gruesome Pompeii discovery: Ancient city reveals grisly secret" (https://www.foxnews.com/science/gruesome-pompeii-discovery-ancient-city-reveals-grisly-secret)
--"‘Not fair’: World cycling bronze medalist cries foul after transgender woman wins gold" (https://www.foxnews.com/sports/not-fair-world-cycling-bronze-medalist-cries-foul-after-transgender-woman-wins-gold)
Both articles have strong headlines. An analysis of the text content of both articles through the "IBM BlueMix Tone Analyzer" (https://tone-analyzer-demo.ng.bluemix.net/) show that both articles appeal to the "sadness" and "fear" emotions. This type of tone analysis exercises using online provider can be made automatic via an API. We could also use the "Sentiment140" database of 1.6 million classified tweets (https://www.kaggle.com/kazanova/sentiment140) to train a machine-learning algorithm to provide the general sentiment of a news article.

Conclusions: 
This project will be exploring the impact of mainstream media in the rise of skepticism	of the public towards science. Through the analysis of tweets and their corresponding online source of inspiration, we will attempt to unravel the potential 'mistakes' that are made by the media in that direction e.g. their use of strong headlines or of a given tone or keywords. The results could be communicated via an online article or directly provided to interested media.

