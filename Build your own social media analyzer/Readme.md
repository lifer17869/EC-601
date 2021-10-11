# Define MVP and User stories
Minimal Viable Product (MVP) for social media analyzer is going to be a result of an AI model for classifying opinion of people based on the gathered data from each user. First and most important aspect is gathering information from social media. Many of famous social media companies like twitter and Facebook have API for accessing information of their users. For gathering such information individual needs to get signed for developer accounts. After gathering developer account, we can get information for specific kay word for last determined number of last shared message. So, MVP will be a framework for entering authorization keys for individuals. After getting valid information user can search for specific keywords and specified number of publish post. A simple frame work of MVP has shown in figure 1.

 
Figure 1. MVP of proposed social media analyzer.

As it has shown in Figure 1 after importing specific information the results of classification will be shown based on positive, negative or neutral class for each comment.

Translate user stories to modular design
For analyzing sentiments first model must be developed with python. Each data will go throw the process of lemmatization, tokenization, parsing and characterizes elimination. Ai model need to work with proper encoded data then the cleaned texts will go throe the word embedding layer. In this layer based on the coding structure each word will converted to specific integer. An example of such a work has been shown below:
Mentioned comments or reviews:
‘This has to be one of the worst films’
Encoded Result:
[1, 14, 47, 8, 30, 31, 7, 4, 249, 108]
As it is clear each word has been converted to a relevant integer. Most of the comments in real world containing specific chanceries like: #, @,’,” and etc. This preprocessing structure will help to eliminate these none useful characterizes too. Also, lower case and upper-case words in most cases doesn’t change the meaning of words in preprocessing all word will be converted to lower case structure. A sample of this work has shown in figure2.
 
Figure 2. Raw data and results of cleaned comments.
After preprocessing and embedding, model will be applied on the encoded data. Such a model can be an already defined libraries for this work or a designed one from scratch most. Model out put will be the result of the classification. A sample of deep learning model with GRU structure has shown in Figure 3.
 
Figure 3. a deep learning model based on Gru layer for classification of the comments.

After result of analysis user can grasp a good idea about society opinion for specific key word if they can survey a lot of user’s comments. Also related key words which are related to specific key word can be seen at the end. The result of such work has shown in figure4.

 
Figure 4. Related key word to the London lockdown search.
 
A frame work of such a program has shown in figure 5.
 
Figure 5. Frame work of the model and modular design.





# Who is your user?
Users of such a service could be big companies which want to survey the social opinion of society about specific product or advertisement companies. In smaller lever this system can be converted as a service for each user to develop their own analyzer and change the model of the work.

# What are basic user stories?
Basic user stories will be based on specific information of each user. This story can get specified by the reviews on movies or comments about social event. These events will help media analyzer to propose better idea with more sells in the market. 
So, basic user stories can be seen in form of comments or trails of their discussion in social media.



![image](https://user-images.githubusercontent.com/85686755/136859498-d0bd14a9-396c-42d5-b0e8-ee9792de9b72.png)

