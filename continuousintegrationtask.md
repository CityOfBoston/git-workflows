Case Study: Using a basic CI workflow for Github

Sample Case Description: A CSV describes the information for our database. The question now is how to best manage data
migrations and additions to this CSV file in the most efficient/pain-free matter which minimizes risk.

CI: A backup of our database should be taken in csv format, which should be tested with previously working
applications to ensure minimal downtime should a failed migration take place. Continuous integration will try to build a
simple app that tests the csv file, 

CD: A python script powered by 
