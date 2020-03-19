import os
import pandas as pd


if __name__ == '__main__':
    path = "./results/"
    pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)

    data = pd.DataFrame(columns=['label'])
    print(pd_all.shape)


    for index in pd_all.index:# todo change output results

        # ["不满", "低落", "愤怒", "开心", "喜悦", "厌恶"]-6 no[fear,none,surprise]

        buman = pd_all.loc[index].values[0]
        sadness = pd_all.loc[index].values[1]
        anger = pd_all.loc[index].values[2]
        happy = pd_all.loc[index].values[3]
        joy = pd_all.loc[index].values[4]
        disgust = pd_all.loc[index].values[5]

        if max(buman, sadness, anger, happy, joy, disgust) == buman:
            data.loc[index + 1] = ["不满"]
        elif max(buman, sadness, anger, happy, joy, disgust) == sadness:
            data.loc[index + 1] = ["低落"]
        elif max(buman, sadness, anger, happy, joy, disgust) == anger:
            data.loc[index + 1] = ["愤怒"]
        elif max(buman, sadness, anger, happy, joy, disgust) == happy:
            data.loc[index + 1] = ["开心"]
        elif max(buman, sadness, anger, happy, joy, disgust) == joy:
            data.loc[index + 1] = ["喜悦"]
        else:
            data.loc[index + 1] = ["厌恶"]


        # ["anger", "disgust", "fear", "happiness", "like", "none", "sadness", "surprise"]-8

        # anger_score = pd_all.loc[index].values[0]
        # disgust_score = pd_all.loc[index].values[1]
        # fear_score = pd_all.loc[index].values[2]
        # happiness_score = pd_all.loc[index].values[3]
        # like_score = pd_all.loc[index].values[4]
        # none_score = pd_all.loc[index].values[5]
        # sadness_score = pd_all.loc[index].values[6]
        # surprise_score = pd_all.loc[index].values[7]
        #
        # if max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score, surprise_score) == anger_score:
        #     # data.append(pd.DataFrame([index, "neutral"],columns=['id','polarity']),ignore_index=True)
        #     data.loc[index+1] = ["anger"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score, surprise_score) == disgust_score:
        #     #data.append(pd.DataFrame([index, "positive"],columns=['id','polarity']),ignore_index=True)
        #     data.loc[index+1] = [ "disgust"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score,
        #              surprise_score) == fear_score:
        #     data.loc[index + 1] = ["fear"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score,
        #              surprise_score) == happiness_score:
        #     data.loc[index + 1] = ["happiness"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score,
        #             surprise_score) == like_score:
        #     data.loc[index + 1] = ["like"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score,
        #             surprise_score) == none_score:
        #     data.loc[index + 1] = ["none"]
        # elif max(anger_score, disgust_score, fear_score, happiness_score, like_score, none_score, sadness_score,
        #          surprise_score) == sadness_score:
        #     data.loc[index + 1] = ["sadness"]
        # else:
        #     #data.append(pd.DataFrame([index, "negative"],columns=['id','polarity']),ignore_index=True)
        #     data.loc[index + 1] = ["surprise"]
        # #print(negative_score, positive_score, negative_score)

    data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')
    #print(data)