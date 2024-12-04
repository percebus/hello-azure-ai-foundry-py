# Evaluation results

```
'-----Summarized Metrics-----'
{'groundedness.gpt_groundedness': 1.25, 'groundedness.groundedness': 1.25}
'-----Tabular Result-----'
                                     outputs.response                                    outputs.context  ...           outputs.groundedness.groundedness_reason line_number
0   Sorry, I only can answer queries related to ou...  [[{'id': '8', 'content': 'Welcome to the joy o...  ...  The RESPONSE is completely unrelated to the CO...           0
1   Could you clarify which specific camping table...  [[{'id': '5', 'content': 'CampBuddy's BaseCamp...  ...  The RESPONSE does not reference any of the inf...           1
2   Sorry, I only can answer queries related to ou...  [[{'id': '11', 'content': 'Meet the TrekReady ...  ...  The RESPONSE does not relate to the CONTEXT at...           2
3   Could you please specify what kind of care ins...  [[{'id': '11', 'content': 'Meet the TrekReady ...  ...  The RESPONSE does not relate to the informatio...           3
4   Sorry, I only can answer queries related to ou...  [[{'id': '1', 'content': 'Unveiling the TrailM...  ...  The RESPONSE does not relate to the CONTEXT at...           4
5                                            (Failed)                                           (Failed)  ...  The RESPONSE does not reference any of the inf...           5
6   Sorry, I only can answer queries related to ou...  [[{'id': '15', 'content': 'Introducing the Out...  ...  The RESPONSE accurately reflects part of the i...           6
7   The TrailBlaze Hiking Pants are crafted from h...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not relate to the CONTEXT at...           7
8   Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not reference any of the pro...           8
9   Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not reference or relate to a...           9
10  Sorry, I only can answer queries related to ou...  [[{'id': '10', 'content': 'Meet the TrailBlaze...  ...  The RESPONSE does not relate to the CONTEXT at...          10
11  Sorry, I only can answer queries related to ou...  [[{'id': '13', 'content': 'Unleash your inner ...  ...  The RESPONSE does not relate to the specific d...          11
12  Sorry, I only can answer queries related to ou...  [[{'id': '8', 'content': 'Welcome to the joy o...  ...                                                NaN          12

[13 rows x 8 columns]
```

[View evaluation results in AI Studio:](https://ai.azure.com/build/evaluation/236b2396-0ae4-429c-a035-4e71f0409c39?wsid=/subscriptions/2445fdd8-5e2c-4da4-8e51-8da0deba3b81/resourceGroups/rg_openai/providers/Microsoft.MachineLearningServices/workspaces/hello-ai-foundry)
