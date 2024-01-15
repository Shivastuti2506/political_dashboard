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

#### latest update 1: till now, we were just able to explore 5 major hot topics, but now, we will be able to see the top 5 discussions( if any ) ongoing about that particular topic.
- I have used the reddit API keys and ID to scrap and display the top discussions around a city. The heading and url of the discussions for every topic can be seen after runing the project.
#### latest update 2: After successfully completing the discussion scrapping part, I have prepared the backend for GPTanalyser for analysing sentiments, summaries and demands . Although the code works fine with hardcoded data but while using the actual API keys and LLM models as per the latest openai documentation, they will cost me to increasing my rate limits for using th APIs. Still I have attached the GPT.py file separately for reference with API key and model name mentioned in it. 

#### latest update 3: The frontend has been updated which includes the dropdown for each source ( newsAPI and reddit)
<img width="603" alt="image" src="https://github.com/Shivastuti2506/political_dashboard/assets/153611876/c980cbbb-43f8-464d-aa1e-d28f7b6edc47">

### 3 ways for quality checking

#### latest update 4: A file named, faithfulness.py can be used to assess the faithfullness of the scrapped results. To use and verify the function , we need to have a premium openAI key therefore I have attached the function in a separate file. I have assumed that we have some reference ( grountruth ) for the verification purpose. 
Evaluating the faithfulness of generated text or results typically involves comparing them to a reference or ground truth to determine how accurately the information has been conveyed.

- If we don't have a ground truth or reference data to compare against, evaluating faithfulness becomes more challenging. However, we can still implement a simple **heuristic-based evaluation** that considers certain characteristics associated with faithful information. 

- If we don't have a ground truth and we want to evaluate faithfulness in a more nuanced way, we might consider leveraging external sources or fact-checking services. An example is , we could incorporate an external fact-checking API, such as the ClaimReview API provided by Google. 
