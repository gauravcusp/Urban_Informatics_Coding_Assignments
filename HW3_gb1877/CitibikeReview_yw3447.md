<b>a. verify that their Null and alternative hypotheses are formulated correctly</b>

The two hypothesises are a little bit confusing. 
Null hypothesis: The total percentage of New Yorkers using bike is as much if not less than the total percentage of Tourists riding a bike in any given week
Alternative hypothesis: Tourists use as many citibike as NewYorkers in any given week

I would rephrase the hypothesis to be more precise about the measurements.
For example:
Null hypothesis: The total percentage of New Yorkers using bike is at least as high or higher than the total percentage of Tourists riding a bike in any given week
Alternative hypothesis: The total percentage of New Yorkers using bike is less than the total percentage of Tourists riding a bike in any given week

<b>b. verify that the data supports the project</b>

The data in Citi Bike only provides "Subscriber" and "Customer". It is hard to say that Citi bike subscribers are all New Yorkers and Citi bike customers are all tourists. The definition of New Yorker is confusing as well. Does it mean New York citizens or residents？And there must be some one-time user who lives in New York but doesn't use bike often.
I would suggest to change "New Yorkers" and "Tourists" in hypothesis to "Subscribers" and "Customers".

<b>c. chose an appropriate test to test H0 given the type of data, and the question asked</b>

According to the guidance from "How to choose the right statistical test?" (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/), the first point of guidance is:
<br><br>
<i>Question 1: Is there a difference between groups that are unpaired? Groups or data sets are regarded as unpaired if there is no possibility of the values in one data set being related to or being influenced by the values in the other data sets. Different tests are required for quantitative or numerical data and qualitative or categorical data as shown in Fig. 1.</i>

For this hypothesis test, the groups are unpaired. We are measuring the frequency of rides. It is numerical. The next point of difference is whether the data is parametric or not. Since we have no assumption about the distribution of rides for subscriber and customer, I conclude that the data is non-parametric and select the <b>Chi-square test</b>.

FBB good
