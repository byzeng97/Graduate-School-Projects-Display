[Google Q&A Type and Topic Classification](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Google%20Q%26A%20Type%20and%20Topic%20Classification)
**To what degree is computer be like human who is able to ask and answer questions with multidimensional understanding and thinking**


*Part1- Q&A Topic Classification*

1. In Q&A Category Classification part, Google pairs of questions and answers are classified into **5 topics**, including life/arts, culture, science, technology, and stackoverflow by application of supervised machine learning technique along with text analytics.

2. The process of the methodology implementation are set up as below:
   - Step 1. Preliminary steps - Set up packages | Load Text | Initial exploratory | Text Preprocessing
   - Step 2. Text Preprocessing - Stopwords Removal, Stemming, Lowercase, ...etc
   - Step 3. Feature Engineering - TFIDF features
   - Step 4. Oversampling - Handle unbalanced class problem with TFIDF features
   - Step 5. Model Building - SVM | Naive Bayes | Random Forest | Decision Tree
   - Step 6. Model Selection - Model Comparison & Selection - Metrics: Accuracy rate on training data
   - Step 7. Model Evaluation - Metrics: Accuracy, F1 Score, Precision Score, Recall Score
   - Step 8. Conclusion
   - Appendix - Evaluate other features + models that were tried before the best features and best models are created
   - Reference Note: Questions and Answers are categorized seperately
 
*Part2- Q&A Type Classification*

1. In Q&A Type Classification part, Google questions are classified into **10 types** and Google answers are classified into **4 types**, by application of supervised machine learning technique along with text analytics.

2. Since the test data set provided by Kaggle do not provide the probabilities scores of each types, we could not generate the labels for the target. In this case, we will parition our pre-processed train data set with labels into.

3. Our target variable for question is question_target_mixed and our target variable for answer is answer_target_mixed.

4. We assigned the labels by using the highest probabilities score from each question type variables. If the observation contains more than one highest score, we label that obersvation as mixed type.

5. The process of the methodology implementation are set up as below:
   - Step 1. Preliminary steps - Set up packages | Load Text | Initial exploratory | Text Preprocessing
   - Step 2. Text Preprocessing - Stopwords Removal, Stemming, Lowercase, ...etc
   - Step 3. Feature Engineering - TFIDF features
   - Step 4. Oversampling - Handle unbalanced class problem with TFIDF features
   - Step 5. Model Building - SVM | Naive Bayes |
   - Step 6. Model Selection - Model Comparison & Selection - Metrics: Accuracy rate on training data
   - Step 7. Model Evaluation - Metrics: Accuracy, F1 Score, Precision Score, Recall Score
   - Step 8. TensorFlow | LSTM - Feature Encoder | Fit Model | Evaluate Model
   - Step 9. Conclusion
   - Appendix - Evaluate other features + models that were tried before the best features and best models are created
   - Reference Note: Questions and Answers are categorized seperately

