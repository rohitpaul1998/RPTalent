# Boston Crime Analysis 

1. Setup a Dataproc cluster on Google Cloud, extracted Boston Crimes data from the CSV file using Hadoop and stored it on HDFS in a distributed manner, resulting in a 50% decrease in data processing time

2. Extracted, cleansed, transformed, loaded 300,000 + records using PySpark in a PySpark dataframe and stored the resulting data in a CSV file, reducing data redundancy by 15% and improving data accuracy by 90%

3. Leveraged Hive by creating a database, conducted in-depth data analysis through querying and filtering the data, revealing key insights that can aid in criminal investigation and prevention

4. Automated the entire data processing pipeline using a Spark-submit job, saving approximately 2 hours of manual work and improving overall efficiency

5. Designed and implemented an end-to-end data pipeline in AWS, using S3 for creating data lakes, Athena for data analysis, and Glue ETL jobs for transforming and loading structured data, thereby achieving a reduction in data processing time by 40%

Note: The code and results of this project are present in the "Big Data Project" directory. Inside you will find scripts for PySpark for performing data transformation/data cleaning of the Boston Crimes dataset, you will find a text file for Google dataproc that has code for PySpark programmed on the spark-shell, leveraged HDFS and Hive for faster data processing as well. You will also find files for AWS glue ETL. Unfortunately, I was not able to download the PySpark script I manually coded in the AWS Glue ETL job for data transformation. But I am attaching few snapshots here for reference.

![image](https://user-images.githubusercontent.com/113409553/220561578-b366a324-d5bd-48cc-a730-3629255b4a7d.png)

<img width="960" alt="image" src="https://user-images.githubusercontent.com/113409553/220561820-f87c7289-a32e-4e7d-8551-ca0d0d390892.png">

<img width="960" alt="image" src="https://user-images.githubusercontent.com/113409553/220561965-60b9f66b-56ba-4cdf-ad9d-f3dc9e36047e.png">




# Restaurant Recommendation System

I have created a database system whose sole purpose is to recommend best restaurants in California.

1. The database system is created upon multiple parameters like Restaurant name, Address, Contact, Location, Foursquare ratings and TripAdvisor ratings 
2. Created an AWS RDS database instance for PostgreSQL for restaurant data storage and linked my database server with Dbeaver tool for data querying
3. Scraped restaurant data from yellowpages.com from multiple pages using BeautifulSoup library in Python and received 800+ records worth of structured data
4. Cleaned the scraped data using Pandas library in Python, reformatted the data as per database structure and eliminated redundant work by code optimization
5. Modeled a relational data model in E/R Studio Data Architect for the Restaurant Recommedation System and established meaningful relationships
6. Created tables in Dbeaver, loaded clean data efficiently using Psycopg2 library, achieving 0 load failures and utilized the data model to answer business questions efficiently
7. Successfully extracted restaurant recommendation data from Dbeaver and imported into Microsoft Power BI for data visualization and analysis, resulting in effective representation and illustration of insights

Note: You can locate the project in "DEProject1" folder. Inside the folder you will find 4 python files that includes scraping file, connection file, datacleaning file and load file. You will also find PostgreSQL files from Dbeaver and DM1 file for data model from E/R Studio.
 

# Human Resources Officer

I have programmed and developed a GUI window-based application using Java in NetBeans IDE.
Curated a UI that facilitates Human Resource processes like creating, reading, updating and deleting employees’ records and other 
confidential data.



