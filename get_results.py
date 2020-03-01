import os
import pandas as pd


if __name__ == '__main__':
    path = "./results/"
    pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)

    data = pd.DataFrame(columns=['polarity'])
    print(pd_all.shape)

    for index in pd_all.index:
        dissatisfied_score = pd_all.loc[index].values[0]
        low_score = pd_all.loc[index].values[1]
        angry_score = pd_all.loc[index].values[2]
        happy_score = pd_all.loc[index].values[3]
        joy_score = pd_all.loc[index].values[4]
        disgust_score = pd_all.loc[index].values[5]

        if max(dissatisfied_score, low_score, angry_score,happy_score,joy_score,disgust_score) == dissatisfied_score:
            # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = ["dissatisfied"]
        elif max(dissatisfied_score, low_score, angry_score,happy_score,joy_score,disgust_score) == low_score:
            #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
            data.loc[index+1] = [ "low_score"]
        elif max(dissatisfied_score, low_score, angry_score,happy_score,joy_score,disgust_score) == angry_score:
            data.loc[index + 1] = ["angry_score"]
        elif max(dissatisfied_score, low_score, angry_score,happy_score,joy_score,disgust_score) == happy_score:
            data.loc[index + 1] = ["happy_score"]
        elif max(dissatisfied_score, low_score, angry_score,happy_score,joy_score,disgust_score) == joy_score:
            data.loc[index + 1] = ["joy_score"]
        else:
            #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
            data.loc[index + 1] = ["disgust_score"]
        #print(negative_score, positive_score, negative_score)

    data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')
    #print(data)