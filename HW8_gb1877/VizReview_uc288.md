# Review of Gaurav Bhardwaj's Visualization for PUI HW8
## Criteria
* **CLARITY**: Is the plot easy to read? Is it clear or confusing? Are the quantities being visualized ambiguous?
* **ESTHETIC**: Beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?
* **HONESTY**: Is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?

## Original Visualization
![Alt text](https://github.com/gauravcusp/PUI2017_gb1877/raw/master/HW8_gb1877/plot.png)
This plot gives us the information that the two varibales, log of Energy Use and log of Greenhouse Gas are faily linearly correlated.
![Alt text](https://github.com/gauravcusp/PUI2017_gb1877/raw/master/HW8_gb1877/download.png)
This figure gives us the pattern of GHG emissions across the city at zip code level.

## Review
### Clarity
For the first plot which shows the relationship between Energy Use Intensity and GHG Emission, it's very clear what he was trying to show. The plot was labeled properly with how he transformed the values and also the units of the values.

For the second plot, it looks clear that this is a map of New York City for someone who is already familiar with seeing the map of NYC but it would have been better to add to the title that the map is of New York City. The color bar is a good way of showing the intensity of the GHG emissions per zip code but it seems strange that the values only range from 0-6 in the color bar. It's a bit ambiguous what the values are really being plotted in the map. One other additional thing that he could have added was the year of the data because the values change yearly.

### Esthetic
For the first plot, the plot is of good size and the legends are readable. The colors are also distinguishable. However, I would have to say it would be good to use the alpha for the scatter plot to at least show how dense the points are the area where all the points are clumped together.

For the second plot, the color map chosen is a good one because when checked for colorblindness, the colors look different. However, since the colors seem to be close to one another in the plot, I find it hard to see the division of the zip code blocks. It would have been better to have a darker color for the outline to show the split between the zip code boundaries.

### Honesty
For the scatter plot, there's not much to say since the values are labeled properly and the transformation of the values is explicitly mentioned. One way to improve the plot would be to include an explanation why log transformation was needed for these values and why the relationship was done for the log-transformed values instead of the actual values.

For the choropleth map, since the values that are being plotted seem to be the log transformed values instead of the actual values, this might be some sort of deformity to the data. When plotting in a map, it would be better to plot actual values instead of transformed values. Also aggregating the values to zip code blocks might not be the best way to represent the data since each zip code block has different building types and sizes. The plot also does not mention what kind of aggregation was done to the values plotted in the choropleth map.
