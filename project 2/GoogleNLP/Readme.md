# Sentiment Analysis
Natural Language processing has a lot of branches. Sentiment analysis is one of them. Sentiment analysis can be defined as classifying text into different classes based on its texture. For gathering meaningful information from a text and use AI for classification use of IMDB dataset has been considered. IMDb reviews consist of 50,000 movie reviews in English (25,000 for training, 25,000 for testing) extracted from the famous Internet Movie Database, along with a simple binary target for each review indicating whether it is negative (0) or positive (1). This data set is very simple and has been decoded and preprocessed before. So, the input of training and testing for this data is number instead of alphabetic character. Labels of these reviews are stored as "0" and "1".  For dealing with this classification task 2-layer GRU with 2 layers of dropout among them have been used. The structure of the models and their parameters has shown in Figure1.
![image](https://user-images.githubusercontent.com/85686755/136421066-2df7386c-ee50-42ec-8b75-048a0d4fdfcb.png)

 
Figure 1. Specification and information of model.
Many of these reviews are very large and extracting negative or positive structure from them can be done only with the first 5 to 6 sentences. For example, this is one of the reviews for training: " This has to be one of the worst films of the 1990s when my friends I were watching this film being the target audience it was aimed at we just sat watched the first half an hour with our jaws touching the floor at how bad it was the rest of the time everyone else in the theatre just started talking to each other leaving or generally crying into their popcorn that they paid money they had earnt working to watch this feeble excuse for a film it must have looked like a great idea on paper but on film, it looks like no one in the film has a clue what is going on crap acting crap costumes I can't get across how embarrassing this is to watch save yourself an hour a bit of your life ". The negative meaning of these reviews can be seen from the first 3 sentences so there is no need to survey the rest. So, it had been decided to work with the first 300 words. 
The result of training model for 10 epochs has shown in Figure 2.
 
Figure 2. Result of accuracy and loss for 10 epochs.
![image](https://user-images.githubusercontent.com/85686755/136421118-31dfae66-0a41-4458-aefa-259dcdd9eaa1.png)

The result shows good accuracy on training but not a good accuracy on the validation set. For avoiding this procedure Drop out layer has been used. For increasing the result on validation, it is better to use full sentences as input data.
![image](https://user-images.githubusercontent.com/85686755/136421013-48e75363-2ac6-40e8-b82c-5d2fefbc4eca.png)

