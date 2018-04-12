# Chinese-Word2Vec-Model

利用搜狗实验室的全网新闻语料训练的word2vec中文模型。

可以直接使用模型做一些近义词的推荐，或者特征选择以及特征降维等工作。

具体的训练过程可以参考这篇文章(https://www.jianshu.com/p/6d542ff65b1e)
使用的是Python语言的gensim库实现的word2vec 官网地址(https://radimrehurek.com/gensim/models/word2vec.html)

因为使用了1G多的语料进行训练，得到了一个1G多的模型(包含有70多万的词汇)，github上不好传，就上传到了百度网盘
可以移步()到网盘上下载。使用起来很方便简单。

可以参考Test.py里来测试一下模型，更多的用法请参照gensim官网的API文档
