data = 'data_train.txt'
labels = 'labels_train.txt'
import codecs

def split_file(file, lable):
    with codecs.open(file,'r', 'utf8') as fp,  codecs.open(lable,'r', 'utf8') as fp2:
        fp_news = codecs.open(file.replace('.txt','_news.txt'),'w' , 'utf8')
        fp_opinions = codecs.open(file.replace('.txt','_opinions.txt'),'w', 'utf8')
        fp_classifieds = codecs.open(file.replace('.txt','_classifieds.txt'),'w' , 'utf8')
        fp_features = codecs.open(file.replace('.txt','_features.txt'),'w' , 'utf8')
        categories = fp.readlines()
        #print(categories[1])
        txt = fp2.read()
        classes = txt.split()
        #print(classes)
        j = 0
        for c in classes:
            if c == '0':
                fp_news.write(categories[j] +' ')
            elif c == '1':
                fp_opinions.write(categories[j] +' ')
            elif c == '2':
                fp_classifieds.write(categories[j] +' ')
            elif c == '3':
                fp_features.write(categories[j] +' ')
            j += 1        
        fp_news.close()
        fp_opinions.close()
        fp_classifieds.close()
        fp_features.close()
                

split_file(data,labels)


