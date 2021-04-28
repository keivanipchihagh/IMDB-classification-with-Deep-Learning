# Imports
import pandas as pd

def create_df(root_dir, review_count):

    pos_dir = root_dir + '/pos'
    neg_dir = root_dir + '/neg'

    def get_reviews(dir, review_count, type):
        ''' Read reviews '''

        partial_reviews = []

        for i in range(1, review_count + 1):
            review_path = dir + '/review ({0}).txt'.format(i)
            with open(review_path, mode = 'r', encoding = "utf8") as review:
                partial_reviews.append(review.read())

            if i % 500 == 0:
                print('Reading {0} review #{1}'.format(type, i))

        return partial_reviews

    # Get positive/negative reviews
    pos_reviews = get_reviews(pos_dir, review_count, 'positive')
    pos_labels = [1 for i in range(review_count)]
    neg_reviews = get_reviews(neg_dir, review_count, 'negative')
    neg_labels = [0 for i in range(review_count)]

    # Create dataset
    df = pd.DataFrame(data = {'review': pos_reviews + neg_reviews, 'value': pos_labels + neg_labels})

    return df


if __name__ == '__main__':

    train_root = 'train'
    test_root = 'test'
    review_count = 12500

    print('Train data:')
    train_df = create_df(train_root, review_count)

    print('\nTest data:')
    test_df = create_df(test_root, review_count)

    train_df.to_csv('train.csv')
    test_df.to_csv('test.csv')