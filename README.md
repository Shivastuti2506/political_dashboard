# political_dashboard
The aim is to build a small dashboard which will give us a sense for the kinds of sentiments and discussions happening in a city around a specific topic.
## Hardcoded_output folder
### I have attached a Hardcoded_file, in which i have provided a raw structure for the project without using the actual API's for now, one can run the app and see the layout for the same. In order to run the given project , you may need to pip install below requirements.
- python
- flask
- praw
- openai
- requests
#### once having all the dependencies installed , you can run the app using command on the terminal 
```
python app.py
```
## main folder
### for the main project, I have uploaded th main folder, which consists of the ongoing project. 
- for now , I have gathered an API which provides the top 5 news for the entered country.
- There is a class GPTAnalyser, which i shall be using for analysis purpose in upcoming commits.
- For running this folder, we will be using the above dependencies only.

### latest update: till now, we were just able to explore 5 major hot topics, but now, we will be able to see the top 5 discussions( if any ) ongoing about that particular topic.
