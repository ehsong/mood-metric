
def read_depechemood():
    '''
    reads depechemood lexicon that has scores for 8 ranges of mood for 37 terms
    ----
    returns

    a panda dataframe with terms as index, emotion categories as columns, scores as rows
    '''
    import pandas as pd
    dm_url = "https://raw.githubusercontent.com/marcoguerini/DepecheMood/master/DepecheMood%2B%2B/DepecheMood_english_token_full.tsv"
    depechemood = pd.read_csv(dm_url, sep='\t', index_col=0)
    depechemood = depechemood[depechemood['freq']> 10]
    depechemood.drop('freq', inplace=True, axis=1)
    return depechemood


dm = read_depechemood()

def extract_emofeats(lex, lex_vocab, text):
    '''
    returns a matrix for a given text

    '''
    import pandas as pd
    import numpy as np
    from tqdm import tqdm

    # clean the text
    import re
    clean_text1 = re.sub('[^A-Za-z0-9]+', ' ', text)
    clean_text2 = re.sub(r'[0-9]+', '', clean_text1)
    clean_text3 = clean_text2.strip() # remove periphery
    tokenized = clean_text3.split()

    # start here
    lex_dict = lex.to_dict('split')
    lex_d = {word: lex_dict['data'][i] for i, word in enumerate(lex_dict['index'])}
    assert len(lex_d.keys()) == len(lex_vocab)
    Ss = np.zeros((len(text), lex.shape[1]))
    for i, doc in tqdm(enumerate(tokenized)):
        intersection = set(lex_vocab) & set([doc])
        s = []
        for inter in intersection:
            s.append(lex_d[inter])
        s = np.array(s)
        divisor = len(s) if len(s) > 0 else 1
        Ss[i, :] = np.sum(s, axis=0) / divisor
    return Ss

def mood_metric_scores(dm,text):
    '''
    obtains the emotion class based on the maximum score obtained

    returns
    -------
    emotion class and the emotion score vector
    '''
    Ss = extract_emofeats(dm, set(dm.index.values), text)
    # average the emoscore for each emotion category
    import numpy as np
    import pandas as pd
    k = np.array([sum(Ss[:,i]) for i in range(Ss.shape[1])])/Ss.shape[1]
    # normalize the row vector
    # this is the score range
    q = k/k.sum(axis=0,keepdims=1) # message-level emo-score;
    # get the classified emotion
    p = list(q)
    emo_name = []
    for col in dm.columns:
        emo_name.append(col)
    # get the pos
    m = max(p)
    pos = p.index(m)
    return emo_name[pos], p
