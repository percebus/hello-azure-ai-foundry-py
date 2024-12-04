# Evaluation results

```
'-----Summarized Metrics-----'
{'groundedness.gpt_groundedness': 1.5454545454545454,
 'groundedness.groundedness': 1.5454545454545454}
'-----Tabular Result-----'
                                     outputs.response                                    outputs.context  ...           outputs.groundedness.groundedness_reason line_number
0   Could you please specify which tent you are as...  [[{'id': '8', 'content': 'Welcome to the joy o...  ...  The RESPONSE does not reference any specific t...           0
1   Could you please specify which camping table y...  [[{'id': '5', 'content': 'CampBuddy's BaseCamp...  ...  The RESPONSE does not relate to the specific d...           1
2   Sorry, I only can answer queries related to ou...  [[{'id': '11', 'content': 'Meet the TrekReady ...  ...  The RESPONSE does not relate to the CONTEXT at...           2
3   Could you please clarify if you're asking abou...  [[{'id': '11', 'content': 'Meet the TrekReady ...  ...  The RESPONSE does not relate to the informatio...           3
4                                            (Failed)                                           (Failed)  ...  The RESPONSE is grounded in the CONTEXT as it ...           4
5   The TrailMaster X4 Tent comes with an included...  [[{'id': '1', 'content': 'Unveiling the TrailM...  ...  The RESPONSE accurately reflects part of the i...           5
6                                            (Failed)                                           (Failed)  ...  The RESPONSE is entirely unrelated to the CONT...           6
7   The TrailBlaze Hiking Pants are crafted from h...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not relate to the CONTEXT at...           7
8   Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not reference any of the pro...           8
9   Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not relate to the CONTEXT at...           9
10  Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not connect to the CONTEXT a...          10
11  Sorry, I only can answer queries related to ou...  [[{'id': '13', 'content': 'Unleash your inner ...  ...                                                NaN          11
12  Sorry, I only can answer queries related to ou...  [[{'id': '8', 'content': 'Welcome to the joy o...  ...                                                NaN          12

[13 rows x 8 columns]
```

[View evaluation results in AI Studio:](https://ai.azure.com/build/evaluation/4531fb18-e4e7-4e75-9164-8f9fad614b2e?wsid=/subscriptions/2445fdd8-5e2c-4da4-8e51-8da0deba3b81/resourceGroups/rg_openai/providers/Microsoft.MachineLearningServices/workspaces/hello-ai-foundry)
