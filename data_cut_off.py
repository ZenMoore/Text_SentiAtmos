import os
import pandas as pd
from sklearn.utils import shuffle

# 内容格式(train/val): ID1\tID2\tlabel\ttext\n
# 内容格式(test): NA\tline_num\tunknwn\text\n
# 文件格式: train.tsv, test.tsv, dev.tsv

if __name__ == '__main__':
    path = "./dataset/original/"
    # 这里应该是给定一个 for train 的 .tsv
    # 用于分隔产生 train_set 和 dev_set 的 .tsv
    # 但是我们已经有了分隔好的 train.txt 和 val.txt
    pd_all = pd.read_csv(os.path.join(path, "data.tsv"), sep='\t' , encoding="utf-8")
    pd_all = shuffle(pd_all)


    dev_set = pd_all.iloc[0:int(pd_all.shape[0]/10)]
    train_set = pd_all.iloc[int(pd_all.shape[0]/10): int(pd_all.shape[0])]
    dev_set.to_csv("dataset/original/dev.tsv", index=False, sep='\t', encoding="utf-8")
    train_set.to_csv("dataset/original/train.tsv", index=False, sep='\t', encoding="utf-8")