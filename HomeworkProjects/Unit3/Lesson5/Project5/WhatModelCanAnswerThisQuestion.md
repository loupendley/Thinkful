#### You now have a fairly substantial starting toolbox of supervised learning methods that you can use to tackle a host of exciting problems.  

#### To make sure all of these ideas are organized in your mind, please go through the list of problems below. 

#### For each, identify which supervised learning method(s) would be best for addressing that particular problem.  

#### Explain your reasoning and discuss your answers with your mentor.

1.  Predict the running times of prospective Olympic sprinters using data from the last 20 Olympics.  
__This would be regression model, as the running times are a real number, seconds.  Potential candidate could be: Linear Regression, with multiple independent variables.  Ridge Regression is another candidate, that seeks to minimize the minimize the overfitting of the model, by reducing the size of the coefficients.  Lasso Regression is another candide that looks to prevent overfitting, by dropping small parameter estimates from the model, by effectively doing feature selection.__  

1.  You have more features (columns) than rows in your dataset.  
__This could be a great candidate for Lasso or Ridge Regression, that perform Feature Selection, and eliminate any low performing features.__  

1.  Identify the most important characteristic predicting likelihood of being jailed before age 20.  
__A classifier model, perhaps  KNN.  Finding out the leading highly correlated behaviors that lead to getting jailed before the age of 20 would be a starting place.__

1.  Implement a filter to “highlight” emails that might be important to the recipient  
__This would most likely be a Naive Bayes model, as we are looking to classify e-mail by certain keywords.__  

1.  You have 1000+ features.  
__Lasso Regression could be a great candidate here, effectively eliminating non-contributing features.  In addition Ridge Regression could be a potential model, by removing low performer features.__
1.  Predict whether someone who adds items to their cart on a website will purchase the items.  
__This would be a naive bayes model.__  

1.  Your dataset dimensions are 982400 x 500  
__This would be a good candidate for Lasso or Ridge Regression.__  

1.  Identify faces in an image.  
__This would be a great candidate for PCA__. 

1.  Predict which of three flavors of ice cream will be most popular with boys vs girls.   
__This would be a Naive Bayes Multinomial model, resulting in giving the top 3 flavors selected, given boys vs girls.__