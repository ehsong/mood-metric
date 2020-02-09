# mood-metric

Building a mood metric using DepecheMood lexicon.

This metric is built using [DepecheMood Lexicon](https://github.com/marcoguerini/DepecheMood) which can retrieve scores for 8 ranges of mood - afraid, amused, angry, annoyed, don't care, happy, inspired, and sad for approximately 37K terms. For more information on the construction of the lexicon please see the paper:

Staiano, J., & Guerini, M. (2014). "DepecheMood: a Lexicon for Emotion Analysis from Crowd-Annotated News". Proceedings of ACL-2014. Paper available at http://www.anthology.aclweb.org/P/P14/P14-2070.pdf

Other than the code partly provided by the authors in their [github](https://github.com/marcoguerini/DepecheMood), this code includes simple text preprocessing of removing punctuations, special characters, and tokenizing.

For more detailed background about the project, please see my [medium post](https://medium.com/@esther.e.song/mood-metric-detecting-mood-at-workplace-using-lexicon-based-approach-8a2b2bbba74).

