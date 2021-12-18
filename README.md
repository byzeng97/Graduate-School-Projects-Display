# Graduate-School-Projects-Display
This repository is mainly for projects I have done at Fordham University Gabelli School 

## 1. [Group Pyramid Final Project](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Group%20Pyramid%20Final%20Project)
**Analyzing the effect of youth tobacco consumption on mortality rate**

*Why Important?* 
1. Present Limitation:
   - According to Tobacco twenty-One website, only 31 of the 51 states are “Tobacco 21 state”. 
   - FDA's Youth Tobacco Prevention Plan mainly pays attention to e-cigarette instead of other tobacco.
   - Current policies pays more attention on alcohol instead of tobacco.
2. Preventing tobacco product use among youth is critical to ending the tobacco epidemic in the United States.
3. The project results will support related national youth-limited tobacco policies released by Federal government. 

*Project Aim:*
1. To explore if there is a correlation between youth tobacco consumption and four types of mortality.
2. Mortailities include cancer, heart disease, drug overdose and stroke.
3. Addressing the correlation will have:
   - practical benefits for preventing tobacco use among middle school and high school students .
   - contribute to understanding of the widespread smoking phenomenon among youth.

*Data Description:* 
1. Period: 2014 - 2017; Variables: 12 variables; Rows: 10601 rows
2. Size = 4*12*10601 = 508848
3. [Primary data link](https://chronicdata.cdc.gov/Survey-Data/Youth-Tobacco-Survey-YTS-Data/4juz-x2tp)

*Tool Selection:*
1. Tableau: exploratory data analysis and visualization. 
2. Python: dataset cleansing, statistical machine learning model building.

*Conclusions & Future Research:*
1. This study would find out how different demographic features would affect the smoking rates.
2. This study would find out the magnitude of different mortality rates correlated with the smoking rates.
3. This study would have one ANOVA model testing the differences of treatment among different smoking groups.
4. This study would open some new ways for researchers to examine more detailed causal effects of youth smoking on mortality.


## 2. [Amazon Fine Food Reviews](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Amazon%20fine%20food%20reviews)
- [Check out raw dataset here](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/master/Desktop/MSBA%20/Big%20Data%20Analytics/project/Amazon%20fine%20food%20reviews) 

*Background & Purposes:*
1. Amazon credits recommender systems with 35% of their revenue. They credit recommender systems with a 29% increase in total sales, bringing their yearly sales volume in 2016 up to 135.99 Billion.
2. Build user-based top-10 and item-based top-10 recommendation systems
3. Shopping websites keep showing correct recommended products for a customer

*Data Description:*
1. Data source: https://www.kaggle.com/snap/amazon-fine-food-reviews
2. Data size: 301 MB (10 columns * 568,454 rows)
3. Data information: 568,454 reviews, 256,059 users, 74,258 products, 260 users with more than 50 reviews

![Methodology Illustation](https://github.com/byzeng97/Graduate-School-Projects-Display/blob/main/Amazon%20fine%20food%20reviews/Methodology%20Illustration.png)

*Expected Results:*
1. A ranking list of word to indicate the positive or the negative reviews
2. A chart show some of the most popular product in Amazon fine food
3. Obtain models with different accuracy rates on predicting the positive and negative reviews & refocused on the best model 


## 3. [Student Query Tool](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Student%20Query%20Tool)
**A Python mini program to apply queries modified for school administration office demand**

*Goal:* 

To build a program using python language (Note: the user interface is via the console):
1. Display all student records.
2. Display students whose last name begins with a certain string (case insensitive).
3. Display all records for students whose graduating year is a certain year.
4. Display a summary report of number and percent of students in each program, for students graduating on/after a certain year.

Note: venv was built in Pycharm


## 4. [Google Q&A Type and Topic Classification](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Google%20Q%26A%20Type%20and%20Topic%20Classification)
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


## [Art Gallery Database Generated by Oracle Modeler](https://github.com/byzeng97/Graduate-School-Projects-Display/tree/main/Art%20Gallery%20Database%20Generated%20by%20Oracle%20Modeler)
