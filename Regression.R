b<-read.csv("C:/Users/aruka/Desktop/A.csv")
library(rpart)
fit <- rpart(T ~ NO2.GT.+CO.GT.+NMHC.GT.+C6H6.GT.+NOx.GT.,
             method="anova", data=b)
printcp(fit)
summary(fit)
par(mfrow=c(1,2)) # two plots on one page 
rsq.rpart(fit) # visualize cross-validation results  	

plot(fit, uniform=TRUE, 
     main="Regression Tree for Mileage ")
text(fit, use.n=TRUE, all=TRUE, cex=.8)
post(fit, file = "C:\folder",title = "Regression Tree")
library(party)
fit <- ctree(T ~ NO2.GT., 
             data=b)
plot(fit, main="Regression Tree")
duration = b$T   
waiting = b$NOx.GT.  
cor(duration, waiting)

library(car)
fit <- lm(T ~ NO2.GT., data=b)

outlierTest(fit) # Bonferonni p-value for most extreme obs
qqPlot(fit, main="QQ Plot") #qq plot for studentized resid 
leveragePlots(fit) # leverage plots

library(rpart)

# grow tree 
fit <- rpart(T ~ NO2.GT., 
             method="anova", data=b)

printcp(fit) # display the results 
plotcp(fit) # visualize cross-validation results 
summary(fit) # detailed summary of splits

plot(fit, uniform=TRUE, 
     main="Regression Tree for Mileage ")
text(fit, use.n=TRUE, all=TRUE, cex=.8)


