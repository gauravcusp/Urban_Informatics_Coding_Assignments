## README for Assignment Week2

url:https://github.com/gauravcusp/PUI2017_gb1877/tree/master/HW2_gb1877

###Assignment 1

Filename: show_bus_locations_gb1877.py

I created a python file that takes input from user(API key and bus route) and returns the details about the active buses on that route. The output consists of the route number entered by the user, number of active buses and the latitude and longitude for each of the active buses.


###Assignment 2

Filename: get_bus_info_gb1877.py

This assignment asked for the details of next stop for each of the active bus and store it to a CSV file with name of the bus route. I created a python file that takes API key, bus route and bus_route.csv as arguments and processes the data of active buses. The output of this program is a csv file with latitude, longitude of each bus along with the name of next stop and the current status of the bus. Also, there were some entries in the data with empty values under stop name and stop status, which I had replaced with 'N/A'.


###Assignment 3

Filename: HW2_3_gb1877.py

For this assignment, I picked a data file for NYPD data on collisions on road from the data facility. As i couldn't access the data facility through environment variable, I had hard coded the path for the directory. Here i created a python file that drops every other column on the dataset, apart from latitude and longitude of each collision. As there were a few NaN values in both the columns, I had to remove them for better plotting. Also, there were some records with (0,0) which is not geographically possible for data recorded in NYC, so I had removed that data as well(Total 8 rows with (0,0) data). The output will display the head of the entire table, head of just the two remaining columns and the plot between the latitude and longitude of the collisions.

###Assignment 3 Extra Credit

Filename: HW2_3_ExtraCredit_gb1877.py

In this assignment we had to pick a column with Date/Time and any other column with numerical values. I chose the Date column and Number of persons injured per collision per day. The output consists the head of raw data, head of columns Date and Number of persons injured and the plot between the two columns. As the data was enormous(990,880 entries), the plot couldn't show the exact dates, so only year is displayed.
