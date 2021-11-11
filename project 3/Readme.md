Test and Unit Test
Testing is one of the most important part pf the coding it is very important to keep in mind that every part of the code is going to work under different condition and situation. The python programming language will provide a library with unit test in order to test each aspect of the work. In This repository in order to evaluate performance of sentiment analysis first we try to get a gibberish tweet into the program and evaluate the result. We tested different gibberish tweet like " kab\5ashbshbhabshz", "5555555", "#", "#hsdgxbhg" and etc. The result of all of this combination with sentiment analysis program was neutral. So, the program doesn’t confuse for specifying categories of these tweets. Also, for checking the positive and negative value of the tweet we tested the "I really Hated this movie\food" and "This meal was palatable for me" the result for these tweets was correctly categorize as positive and negative. It is important to mention that long sentences tweet have been tested during the gibberish testing.
But testing performance of a function like sentiment analysis function is the last part of the testing structure. To have a complete set of manual tests, all we need to do is make a list of all the features that our code has, the different types of input it can accept, and the expected results. Now, every time we make a change to your code, you need to go through every single item on that list and check it.
But considering all of these option for testing the code is going to be hard and confusing because testing different structure if the code may cause different problem and tracking down these problems will be very hard. So, one the modern way to test our model is unit test.
A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps us to isolate what is broken in your application and fix it faster. In order to test our model with unit test we first create a python file with name of the installation_test.py. The result of testing all variable and syntax of the code has shown below.




![image](https://user-images.githubusercontent.com/85686755/141327215-c8e1be65-c773-4ba9-977c-312460203e53.png)

 
Figure1. Testing the code with unit test


![image](https://user-images.githubusercontent.com/85686755/141327293-9f3c8afe-f372-4370-89e3-ecd38a49e6a0.png)


Result of this code was correct as before and no error has been raised.


