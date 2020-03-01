import pandas as pd

# 转换train.csv为train.tsv
train_set =pd.read_csv("./dataset/original/train.csv",sep=',', header=0)
print(train_set.keys)
train_df_bert = pd.DataFrame({
    # 'id':range(len(train_set)),
    'id1' : train_set['id1'],
    'id2' : train_set['id2'],
    'label':train_set['label'],
    'text': train_set['text'].replace(r'\n', ' ', regex=True)
})
train_df_bert.to_csv('./dataset/original/train.tsv', sep='\t', index=False, header=True)

# 转换val.csv为val.tsv
val_set =pd.read_csv("./dataset/original/val.csv",sep=',', header=0)
val_df_bert = pd.DataFrame({
    'id1':val_set['id1'],
    'id2':val_set['id2'],
    'label':val_set['label'],
    'text': val_set['text']
})
val_df_bert.to_csv('./dataset/original/dev.tsv', sep='\t', index=False, header=True)

#转换test.csv为test.tsv
test_set =pd.read_csv("./dataset/original/test.csv",sep=',', header=0)
test_df_bert = pd.DataFrame({
    'validity':test_set['validity'],
    'id':test_set['id'],
    'label':test_set['label'],
    'text': test_set['text']
})
test_df_bert.to_csv('./dataset/original/test.tsv', sep='\t', index=False, header=True)