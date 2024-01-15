
# Political Dashboard 📊

## Overview
The Political Dashboard is designed to provide insights into sentiments and discussions surrounding a specific topic within a city. The project is built using Python and Flask, leveraging various APIs to gather information. The `Hardcoded_output` folder contains a raw structure of the project with a hardcoded file for initial visualization. The `main` folder is an ongoing project that fetches top news and discussions about a chosen topic.

## Getting Started
To run the project, ensure you have the following dependencies installed:
- Python
- Flask
- PRAW
- OpenAI
- Requests

Use the following command to run the app:
```bash
python app.py
```

## hardcoded file
- Explore the provided Hardcoded_file to get a glimpse of the project's layout without using actual APIs.

## main folder : the ongoing project
- I have gathered an API which provides the top 5 news for the entered area.
- There is a class GPTAnalyser, which we shall be using for analysis purpose in upcoming commits.
- For running this folder, We will be using the above dependencies only.

#### UPDATE 1:  Gathering Topics and related discussions done
- Till now, we were just able to explore 5 major hot topics, but now, we will be able to see the top 5 discussions( if any ) ongoing about that particular topic.
- I have used the reddit API keys and ID to scrap and display the top discussions around a city. The heading and url of the discussions for every topic can be seen after runing the project.
#### UPDATE 2: Analyser backend prepared
- After successfully completing the discussion scrapping part, I have prepared the backend for GPTanalyser for analysing sentiments, summaries and demands .
- Although the code works fine with hardcoded data but while using the actual API keys and LLM models (as per the latest openai documentation), they will cost us to increasing our rate limits for using the APIs.
- I have attached a GPT.py file separately for reference. 

#### UPDATE 3: Frontend updated 
<img width="603" alt="image" src="https://github.com/Shivastuti2506/political_dashboard/assets/153611876/c980cbbb-43f8-464d-aa1e-d28f7b6edc47">

### UPDATE 4:  3 ways for quality checking

####  A file named, faithfulness.py can be used to assess the faithfullness of the scrapped results. To use and verify the function , we need to have a premium openAI key therefore I have attached the function in a separate file. I have assumed that we have some reference ( grountruth ) for the verification purpose. 
- Evaluating the faithfulness of generated text or results typically involves comparing them to a reference or ground truth to determine how accurately the information has been conveyed.

- If we don't have a ground truth or reference data to compare against, evaluating faithfulness becomes more challenging. However, we can still implement a simple **heuristic-based evaluation** that considers certain characteristics associated with faithful information. 

- If we don't have a ground truth and we want to evaluate faithfulness in a more nuanced way, we might consider leveraging external sources or fact-checking services. An example is , we could incorporate an external fact-checking API, such as the ClaimReview API provided by Google. 
