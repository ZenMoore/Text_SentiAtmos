# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:56:22 2020

@author: zxh
"""
import csv
import pandas as pd
import os
import get_results
import player

def get_sentences(indir, outdir_txt, outdir_csv):
    cutLineFlag = ["？", "！", "。", " ",
                   ".","?","!"," ",
                   "\n", "\t", "\r"]
    sentenceList = []
    with open(indir, "r", encoding="UTF-8") as file:
        for line in file:
            # words = re.sub("\?", "", line.strip())
            # words = re.sub("\[*\]", "", words)
            words = line.strip()
            oneSentence = ""
            for word in words:
                print(word)
                if word not in cutLineFlag:
                    oneSentence = oneSentence + word
                else:
                    oneSentence = oneSentence + word
                    if oneSentence.__len__() > 4:
                        sentenceList.append(oneSentence.strip() + "\r")
                    oneSentence = ""
    with open(outdir_txt, "w", encoding="UTF-8") as resultFile:
        print(sentenceList.__len__())
        sentenceList.insert(0, 'placeholder\n')
        resultFile.writelines(sentenceList)  # 得到分句txt文档

    # PARTIE 2
    csvFile = open('./text/temp.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    csvRow = []  # 最终得到的csv文档命名

    f = open(outdir_txt, 'r', encoding='utf-8')
    for line in f:
        csvRow = line.split()
        writer.writerow(csvRow)

    f.close()
    csvFile.close()

    # PARTIE3
    header = ['validity', 'id', 'label', 'text', 'label']
    with open(outdir_csv, 'w', newline='')as f:  # newline=" "是为了避免写入之后有空行
        ff = csv.writer(f)
        ff.writerow(header)

    validity = []  # label unknown 设置好
    label = []
    df_grade = pd.DataFrame(validity)
    df_grade = pd.concat([df_grade, pd.DataFrame(label)], axis=1)
    df_grade['label'] = 'unknown'


    data_initial = pd.read_csv('./text/temp.csv')
    # data_final = pd.read_csv(outdir_csv)

    data_initial.to_csv(outdir_csv)

    # 生成有validity等的final.csv
    df = pd.read_csv(outdir_csv, low_memory=False)  # 读取csv,设置low_memory=False防止内存不够时报警告
    df['validity'] = 'NA'  # 增加新的列company
    df['label'] = 'unknown'
    df['id'] = df.index
    df['text'] = data_initial
    # 以下保存指定的列到新的csv文件，index=0表示不为每一行自动编号，header=1表示行首有字段名称 header=0无表头
    df.to_csv(outdir_csv, columns=['validity', 'id', 'label', 'text'], index=0, header=0)

def transformer(dir):
    pd_all = pd.read_csv(dir+'/test.csv', sep=',', header=None, encoding="utf-8")
    # test_df_bert = pd.DataFrame()
    pd_all.to_csv(dir+'/test.tsv', sep='\t', index=False, header=None, encoding="utf-8")

if __name__ == '__main__':

    dir = './text'
    pos = 0

    while True:
        if os.path.exists("./text/o.temp"):

            input_article = dir+'/article.txt'
            seg_article = dir+'/seg_article.txt'
            test_file = dir+'/test.csv'

            # 长文本分句
            get_sentences(input_article, seg_article, test_file)

            # 文件格式转换
            transformer(dir)
            #
            # 预测结果
            os.system('python run_classifier.py '
                      '--task_name=emlo '
                      '--do_predict=true '
                      '--data_dir='+dir+' '
                      '--vocab_file=./albert_model/vocab.txt '
                      '--bert_config_file=./albert_model/albert_config_tiny.json '
                      '--init_checkpoint=./best_model/model.ckpt-28000 '
                      '--max_seq_length=128 '
                      '--output_dir=./results')

            # 解析结果
            sentiment = get_results.run('./results')

            # 播放音频
            print(sentiment)
            file = open("D:/Java/J Workplace/sentiatmos/senti.txt", 'w')
            sentinum = 0
            if sentiment == '不满':
                sentinum = 0
            elif sentiment == '低落':
                sentinum = 1
            elif sentiment == '愤怒':
                sentinum = 2
            elif sentiment == '开心':
                sentinum = 3
            elif sentiment == '喜悦':
                sentinum = 4
            else:
                sentinum = 5
            file.write(str(sentinum))
            file.flush()
            file.close()
            player.run(sentiment)


            # if pos == 0:
            #     player.run("喜悦")
            #     pos += 1
            # else:
            #     player.run("低落")



        else: pass
