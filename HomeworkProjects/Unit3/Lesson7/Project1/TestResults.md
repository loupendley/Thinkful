With 1,000,000 rows used:
With CountVectorizer vectorizer, the metrics accuracy score = 86.02%
2019-06-11 22:12:44: In: vectorizer_nb 


End 
2019-06-11 22:12:44: In: vectorizer_nb End


 
We are running with TfidfVectorizer
With TfidfVectorizer vectorizer, the metrics accuracy ## score = 85.65%

With the full file:

2019-06-16 23:05:22: In: main Starting main()
2019-06-16 23:05:22: In: file_stuff Log start get filecount
There are 6,685,900 lines in data file yelp_academic_dataset_review.json.
2019-06-16 23:07:11: In: file_stuff Log end read datafile yelp_academic_dataset_review.json
there are 6,685,900 entries in  data frame df
columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object')
columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object')
we have cleaned up the dataframe.
the current time of start is 2019-06-16 23:08:52.037596
the current time of start is 2019-06-16 23:08:52.039460
train_size = 0.9, X_train is 6017310, and y_train is 6017310
test_size  = 0.1, X_test  is 668590, and y_test is 668590
2019-06-16 23:09:35: In: run_it Begin
2019-06-16 23:09:35: In: run_it We are running with a Classifier model
2019-06-16 23:09:35: In: sentiment_analyzer Begin
2019-06-16 23:09:35: In: sentiment_analyzer Now running pipeline with: BernoulliNB and parameters={}:
the metrics accuracy score = 75.81% with BernoulliNB
2019-06-16 23:21:22: In: sentiment_analyzer Finished running pipeline with: Pipeline(memory=None, steps=[('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict', dtype=<class 'numpy.int64'>, encoding='utf-8', input='content', lowercase=True, max_df=1.0, max_features=None, min_df=1, ngram_range=(1, 1), preprocessor=None, stop_words=None, strip...se, use_idf=True)), ('clf', BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True))]):
2019-06-16 23:21:22: In: sentiment_analyzer

End
2019-06-16 23:21:23: In: sentiment_analyzer Begin
2019-06-16 23:21:23: In: sentiment_analyzer Now running pipeline with: MultinomialNB and parameters={}:
the metrics accuracy score = 85.98% with MultinomialNB
2019-06-16 23:32:40: In: sentiment_analyzer Finished running pipeline with: Pipeline(memory=None, steps=[('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict', dtype=<class 'numpy.int64'>, encoding='utf-8', input='content', lowercase=True, max_df=1.0, max_features=None, min_df=1, ngram_range=(1, 1), preprocessor=None, stop_words=None, strip...inear_tf=False, use_idf=True)), ('clf', MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))]):
2019-06-16 23:32:40: In: sentiment_analyzer

End
2019-06-16 23:32:40: In: sentiment_analyzer Begin
2019-06-16 23:32:40: In: sentiment_analyzer Now running pipeline with: LogisticRegression and parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:758: ConvergenceWarning: lbfgs failed to converge. Increase the number of iterations.
  "of iterations.", ConvergenceWarning)
the metrics accuracy score = 91.08% with LogisticRegression
2019-06-16 23:49:08: In: sentiment_analyzer Finished running pipeline with: Pipeline(memory=None, steps=[('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict', dtype=<class 'numpy.int64'>, encoding='utf-8', input='content', lowercase=True, max_df=1.0, max_features=None, min_df=1, ngram_range=(1, 1), preprocessor=None, stop_words=None, strip...enalty='l2', random_state=None, solver='lbfgs', tol=0.0001, verbose=0, warm_start=False))]):
2019-06-16 23:49:08: In: sentiment_analyzer

End
2019-06-16 23:49:08: In: run_it

End
2019-06-16 23:49:08: In: main Ending main()

23-Jun-2019
logit 91.91%
with:
Now running pipeline with: vect = CountVectorizer, tfidf=TfidfTransformer and clf=LogisticRegression

parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 200}:
Elapsed time: 25m

mnb now running:
 2019-06-23 17:25:05: In: run_it Begin


  2019-06-23 17:25:05: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 17:25:05: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}: ###  Metrics accuracy score = 90.90% with LogisticRegression Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='lbfgs',
          tol=0.0001, verbose=0, warm_start=False))] 2019-06-23 17:27:16: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:   2019-06-23 17:27:16: In: sentiment_analyzer 


End  2019-06-23 17:27:16: In: run_it 


End  2019-06-23 17:27:16: In: main Ending main()  2019-06-23 17:27:16: In: <module> Begin


  2019-06-23 17:27:35: In: <module> 


EndHere is the shape of Tf (100000, 21004)  2019-06-23 17:28:40: In: run_it Begin


  2019-06-23 17:28:40: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 17:28:40: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 1000}: ###  Metrics accuracy score = 89.25% with LogisticRegression Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=1000, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='lbfgs',
          tol=0.0001, verbose=0, warm_start=False))] 2019-06-23 17:37:23: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:   2019-06-23 17:37:23: In: sentiment_analyzer 


End  2019-06-23 17:37:23: In: run_it 


End  2019-06-23 17:37:23: In: main Ending main()  2019-06-23 17:38:04: In: run_it Begin


  2019-06-23 17:38:04: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 17:38:04: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'liblinear', 'max_iter': 100}: 2019-06-23 17:54:23: In: run_it Begin


  2019-06-23 17:54:23: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 17:54:23: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'newton-cg', 'max_iter': 100}: 2019-06-23 17:54:44: In: main Starting main()  2019-06-23 17:54:44: In: file_stuff Log start get filecount  2019-06-23 17:55:17: In: file_stuff There are 6,685,900 lines in data file yelp_academic_dataset_review.json.  2019-06-23 17:55:25: In: file_stuff Log end read datafile yelp_academic_dataset_review.json  2019-06-23 17:55:27: In: file_stuff there are 1,000,001 entries in  data frame df  2019-06-23 17:55:27: In: file_stuff columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object')  2019-06-23 17:55:28: In: file_stuff columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object')  2019-06-23 17:55:28: In: file_stuff we have cleaned up the dataframe.  2019-06-23 17:55:28: In: make_X_and_Y the current time of start is 2019-06-23 17:55:28.964519  test_size=0.1, and train_size=0.9 train_size = 0.9, X_train is 900000, and y_train is 900000 test_size  = 0.1, X_test  is 100001, and y_test is 100001 2019-06-23 17:55:31: In: run_it Begin


  2019-06-23 17:55:31: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 17:55:31: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'newton-cg', 'max_iter': 100}: 2019-06-23 18:54:51: In: run_it Begin


  2019-06-23 18:54:51: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 18:54:51: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'newton-cg', 'max_iter': 100}: 2019-06-23 18:55:44: In: run_it Begin


  2019-06-23 18:55:44: In: run_it We are running with a Classifier model  tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000} 2019-06-23 18:55:44: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'sag', 'max_iter': 100}: ###  Metrics accuracy score = 89.53% with LogisticRegression Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='sag',
          tol=0.0001, verbose=0, warm_start=False))] 2019-06-23 18:59:49: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:   2019-06-23 18:59:49: In: sentiment_analyzer 


End  2019-06-23 18:59:49: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'saga', 'max_iter': 100}: ###  Metrics accuracy score = 89.87% with LogisticRegression Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='saga',
          tol=0.0001, verbose=0, warm_start=False))] 2019-06-23 19:04:08: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:   2019-06-23 19:04:08: In: sentiment_analyzer 


End  2019-06-23 19:04:08: In: sentiment_analyzer Begin


 running with path=A  ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'liblinear', 'max_iter': 100}: 2019-06-23 19:22:31: In: run_it Begin


 
 2019-06-23 19:22:31: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-23 19:22:31: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-23 19:37:59: In: main Starting main() 
 2019-06-23 19:37:59: In: file_stuff Log start get filecount 
 2019-06-23 19:38:30: In: file_stuff There are 6,685,900 lines in data file yelp_academic_dataset_review.json. 
 2019-06-23 19:39:24: In: file_stuff Log end read datafile yelp_academic_dataset_review.json 
 2019-06-23 19:40:06: In: file_stuff there are 6,685,900 entries in  data frame df 
 2019-06-23 19:40:06: In: file_stuff columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object') 
 2019-06-23 19:40:14: In: file_stuff columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object') 
 2019-06-23 19:40:14: In: file_stuff we have cleaned up the dataframe. 
 2019-06-23 19:40:28: In: make_X_and_Y the current time of start is 2019-06-23 19:40:28.140461 
 test_size=0.1, and train_size=0.9
 train_size = 0.9, X_train is 6017310, and y_train is 6017310
 test_size  = 0.1, X_test  is 668590, and y_test is 668590
 2019-06-23 19:40:56: In: run_it Begin


 
 2019-06-23 19:40:56: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-23 19:40:56: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 ###  Metrics accuracy score = 91.08% with LogisticRegression
 Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='lbfgs',
          tol=0.0001, verbose=0, warm_start=False))]
 2019-06-23 19:57:47: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:  
 2019-06-23 19:57:47: In: sentiment_analyzer 


End 
 2019-06-23 19:57:47: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=MultinomialNB
parameters={}:
 ###  Metrics accuracy score = 85.98% with MultinomialNB
 Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))]
 2019-06-23 20:09:10: In: sentiment_analyzer Finished running pipeline with:
MultinomialNB:  
 2019-06-23 20:09:10: In: sentiment_analyzer 


End 
 2019-06-23 20:09:10: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=BernoulliNB
parameters={}:
 ###  Metrics accuracy score = 75.81% with BernoulliNB
 Steps information: [('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)), ('tfidf', TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)), ('clf', BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True))]
 2019-06-23 20:20:30: In: sentiment_analyzer Finished running pipeline with:
BernoulliNB:  
 2019-06-23 20:20:30: In: sentiment_analyzer 


End 
 2019-06-23 20:20:30: In: run_it 


End 
 2019-06-23 20:20:30: In: main Ending main() 
 2019-06-23 20:20:30: In: <module> Begin


 
 2019-06-23 20:20:57: In: <module> 


EndHere is the shape of Tf (100000, 21339) 
 2019-06-23 20:53:59: In: run_it Begin


 
 2019-06-23 20:53:59: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-23 20:53:59: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with: vect = CountVectorizer,  tfidf=TfidfTransformer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-23 20:54:36: In: run_it Begin


 
 2019-06-23 20:54:36: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-23 20:54:36: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-24 19:31:49: In: main Starting main() 
 2019-06-24 19:31:49: In: file_stuff Log start get filecount 
 2019-06-24 19:32:20: In: file_stuff There are 6,685,900 lines in data file yelp_academic_dataset_review.json. 
 2019-06-24 19:33:16: In: file_stuff Log end read datafile yelp_academic_dataset_review.json 
 2019-06-24 19:34:05: In: file_stuff there are 6,685,900 entries in  data frame df 
 2019-06-24 19:34:05: In: file_stuff columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object') 
 2019-06-24 19:34:12: In: file_stuff columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object') 
 2019-06-24 19:34:12: In: file_stuff we have cleaned up the dataframe. 
 2019-06-24 19:34:26: In: make_X_and_Y the current time of start is 2019-06-24 19:34:26.615857 
 2019-06-24 19:35:52: In: run_it Begin


 
 2019-06-24 19:35:52: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-24 19:35:52: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-24 19:36:01: In: run_it Begin


 
 2019-06-24 19:36:01: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-24 19:36:01: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-24 19:36:16: In: main Starting main() 
 2019-06-24 19:36:16: In: file_stuff Log start get filecount 
 2019-06-24 19:37:07: In: file_stuff There are 6,685,900 lines in data file yelp_academic_dataset_review.json. 
 2019-06-24 19:39:08: In: file_stuff Log end read datafile yelp_academic_dataset_review.json 
 2019-06-24 19:40:42: In: file_stuff there are 6,685,900 entries in  data frame df 
 2019-06-24 19:40:42: In: file_stuff columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object') 
 2019-06-24 19:40:55: In: file_stuff columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object') 
 2019-06-24 19:40:55: In: file_stuff we have cleaned up the dataframe. 
 2019-06-24 19:41:32: In: make_X_and_Y the current time of start is 2019-06-24 19:41:32.333660 
 test_size=0.1, and train_size=0.9
 train_size = 0.9, X_train is 6017310, and y_train is 6017310
 test_size  = 0.1, X_test  is 668590, and y_test is 668590
 2019-06-24 19:43:07: In: run_it Begin


 
 2019-06-24 19:43:07: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (2, 2), 'max_df': 0.5, 'min_df': 15, 'max_features': 50000}
 2019-06-24 19:43:07: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 2019-06-24 22:16:29: In: main Starting main() 
 2019-06-24 22:16:29: In: file_stuff Log start get filecount 
 2019-06-24 22:17:01: In: file_stuff There are 6,685,900 lines in data file yelp_academic_dataset_review.json. 
 2019-06-24 22:17:09: In: file_stuff Log end read datafile yelp_academic_dataset_review.json 
 2019-06-24 22:17:11: In: file_stuff there are 1,000,001 entries in  data frame df 
 2019-06-24 22:17:11: In: file_stuff columns=Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date'], dtype='object') 
 2019-06-24 22:17:12: In: file_stuff columns are Index(['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'message', 'date', 'sentiment_label', 'message_length'], dtype='object') 
 2019-06-24 22:17:12: In: file_stuff we have cleaned up the dataframe. 
 2019-06-24 22:17:12: In: make_X_and_Y the current time of start is 2019-06-24 22:17:12.605287 
 test_size=0.1, and train_size=0.9
 train_size = 0.9, X_train is 900000, and y_train is 900000
 test_size  = 0.1, X_test  is 100001, and y_test is 100001
 2019-06-24 22:17:12: In: run_it Begin


 
 2019-06-24 22:17:12: In: run_it We are running with a Classifier model 
 tfidf_parms={'stop_words': 'english', 'ngram_range': (1, 3), 'max_df': 0.8, 'min_df': 0.1, 'max_features': 50000}
 2019-06-24 22:17:12: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=LogisticRegression
parameters={'C': 1e+20, 'solver': 'lbfgs', 'max_iter': 100}:
 ###  Metrics accuracy score = 76.24% with LogisticRegression
 Steps information: [('tfidf', TfidfVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.float64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=0.8, max_features=50000, min_df=0.1,
        ngram_range=(1, 3), norm='l2', preprocessor=None, smooth_idf=True,
        stop_words='english', strip_accents=None, sublinear_tf=False,
        token_pattern='(?u)\\b\\w\\w+\\b', tokenizer=None, use_idf=True,
        vocabulary=None)), ('clf', LogisticRegression(C=1e+20, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='lbfgs',
          tol=0.0001, verbose=0, warm_start=False))]
 2019-06-24 22:26:05: In: sentiment_analyzer Finished running pipeline with:
LogisticRegression:  
 2019-06-24 22:26:05: In: sentiment_analyzer 


End 
 2019-06-24 22:26:16: In: sentiment_analyzer Begin


 running with path=A 
 ####  Now running pipeline with:  tfidf=TfidfVectorizer and clf=MultinomialNB
parameters={}:
