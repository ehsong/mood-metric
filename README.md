# mood-metric

This metric was built using [DepecheMood Lexicon](https://github.com/marcoguerini/DepecheMood) which can retrieve scores for 8 ranges of mood - afraid, amused, angry, annoyed, don't care, happy, inspired, and sad for approximately 37K terms. For more information on the construction of the lexicon please see the paper:

Staiano, J., & Guerini, M. (2014). "DepecheMood: a Lexicon for Emotion Analysis from Crowd-Annotated News". Proceedings of ACL-2014. Paper available at http://www.anthology.aclweb.org/P/P14/P14-2070.pdf

Other than the code partly provided by the authors in their [github](https://github.com/marcoguerini/DepecheMood), this code includes simple text preprocessing of removing punctuations, stop words, special characters, and tokenizing.

For more detailed background about the project, please see my medium post ["Mood Metric: Detecting Mood at the Workplace Using Lexicon-Based Approach"](https://medium.com/@esther.e.song/mood-metric-detecting-mood-at-workplace-using-lexicon-based-approach-8a2b2bbba74).

### Example

Excerpt from Jane Austen's *Pride and Prejudice*

"When she remembered the style of his address, she was still full of indignation; but when she considered how unjustly she had condemned and upbraided him, her anger was turned against herself; and his disappointed feelings became the object of compassion."

![mood metric](/pride_and_prejudice.png)

### Notes

To run the .py file please run the following command in terminal:  
```pip3 install seaborn```  
```pip3 install spacy```  
```python3.8 -m spacy download en_core_web_lg```  


### Comparing Performance Against NRC

For this project, I compared the performance of DepecheMood with [NRC Lexicon](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm) which includes 14K unigrams for 8 ranges of emotions. The performance of the two lexicons were tested on [ISEAR data set](https://www.unige.ch/cisa/research/materials-and-online-research/research-material/) which includes 7K self-written sentences for 7 emotion categories. The notebook is [here](https://github.com/ehsong/mood-metric/blob/master/nrc_dm_comparison.ipynb). For this work I used [ISEAR Loader](https://github.com/sinmaniphel/py_isear_dataset) which is a tool that helps loading ISEAR data in python.
