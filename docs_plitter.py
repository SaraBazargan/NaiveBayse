news = '/Users/sara/Desktop/naive/train/news/data_train_news.txt'
opinions = '/Users/sara/Desktop/naive/train/opinions/data_train_opinions.txt'
classifieds = '/Users/sara/Desktop/naive/train/classifieds/data_train_classifieds.txt'
features = '/Users/sara/Desktop/naive/train/features/data_train_features.txt'
test = '/Users/sara/Desktop/naive/test/data_valid.txt'

import contextlib

def split(file):
    file_large = file
    l = 1  # lines per split file
    with contextlib.ExitStack() as stack:
        fd_in = stack.enter_context(open(file_large))
        for i, line in enumerate(fd_in):
            if not i % l:
                file_split = '{}.{}'.format(file_large, i//l)
                fd_out = stack.enter_context(open(file_split, 'w'))
            fd_out.write('{}\n'.format(line))

            
split(news)
split(opinions)
split(classifieds)
split(features)
split(test)
