from gensim import models

if __name__ == '__main__':
    #model=models.Word2Vec.load('word2vec_779845.model')
    model=models.KeyedVectors.load_word2vec_format('word2vec_779845.bin',binary=True)
    list=['深圳','中国','篮球','哥哥']
    for w in list:
        value=model.most_similar(positive=[w],topn=15)
        print("关键词: {}".format(w))
        for v in value:
            print(v[0],v[1])