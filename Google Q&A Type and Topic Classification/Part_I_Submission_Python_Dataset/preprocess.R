# train process
# read data
train <- read.csv("/Users/yanqishi/Documents/Course/Text Analytics/Project/Dataset_GoogleQuestQ&A_Jennie/train.csv")

# select type fields
train_type <- select(train, c(1,23:31,38:40))
question_target_mix <- c()
question_target_detailed <- c()
answer_target_mix <- c()
answer_target_detailed <- c()
q_detailed_num <- c()
a_detailed_num <- c()

# find the fields with largest score
for (i in 1:dim(train_type)[1]){
  show(i/dim(train_type)[1]*100)
  q_max <- max(train_type[i, 2:10])
  a_max <- max(train_type[i, 11:13])
  q_type <- colnames(train_type)[1+which(train_type[i,2:10]==q_max)]
  a_type <- colnames(train_type)[10+which(train_type[i,11:13]==a_max)]
  if (length(q_type)>1){
    question_target_mix <- c(question_target_mix, "question_type_mixed")
    question_target_detailed <- c(question_target_detailed, q_type)
    q_detailed_num <- c(q_detailed_num,length(q_type))
  }
  else{
    question_target_mix <- c(question_target_mix, q_type)
    question_target_detailed <- c(question_target_detailed, q_type)
    q_detailed_num <- c(q_detailed_num,length(q_type))
  }
  if (length(a_type)>1){
    answer_target_mix <- c(answer_target_mix, "answer_type_mixed")
    answer_target_detailed <- c(answer_target_detailed, a_type)
    a_detailed_num <- c(a_detailed_num,length(a_type))
  }
  else{
    answer_target_mix <- c(answer_target_mix, a_type)
    answer_target_detailed <- c(answer_target_detailed, a_type)
    a_detailed_num <- c(a_detailed_num,length(a_type))
  }
}
# create target variables
processed_train <- cbind(train, question_target_mix, rep(NA, dim(train)[1]), answer_target_mix, rep(NA, dim(train)[1]))
colnames(processed_train) <- c(colnames(train), "question_target_mix", "question_target_detailed", "answer_target_mix", "answer_target_detailed")
a_index <- 1
q_index <- 1
for (i in 1:dim(processed_train)[1]){
  processed_train[i,43] <- paste(question_target_detailed[q_index:(q_index+q_detailed_num[i]-1)], collapse = ", ")
  processed_train[i,45] <- paste(answer_target_detailed[a_index:(a_index+a_detailed_num[i]-1)], collapse = ", ")
  a_index <- a_index + a_detailed_num[i]
  q_index <- q_index + q_detailed_num[i]
}

# write file
write.csv(processed_train, "/Users/yanqishi/Documents/Course/Text Analytics/Project/Processed_train.csv")






