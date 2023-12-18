# Retrieving and Processing YouTube Comment Data

## Introduction and Problem Statement
Since the organization was founded in 2005, YouTube has provided digital media to billions of consumers for anything from infamous cat videos, motivational groups, or instruction on how to work with a new coding language. Particularly, music videos after the fall of MTV have become a major component of the content delivery service provided by YouTube, allowing well known and up-and-coming artists to produce and distribute their chosen form of media.
The purpose of this experiment is to gather comments and information from music videos released by the artist Taylor Swift and show methods for using various non-relational databases to store, manipulate, and demonstrate relationships between media. Using Spark, MongoDB, Neo4j, and Cassandra, the experiment will use comment data to show the different use cases of these databases and the transfer of data between platforms. Rather than chase a specific analytical question, the intent is to show the implementation of multiple technologies for different use cases in Big Data.
Using a generalized process, the solution for the particular question of “how can a system of systems be used to interpret information about generated media” is scalable from examination of a single video to an entire library of artistic works. The goal of the program itself is to run fully with minimal manual interaction from the analyst/engineer to gather data and distribute to multiple storage solutions for analysis later. Once the data is stored for the desired number of videos, relationships can be identified as well as trends for commenting and popularity. The system itself can be applied to any artist and desired number of videos, demonstrating flexibility and scalability of the solution.
## Methodology
Generally, the program functions out of Spark with a minimal number of commands required in the Command Prompt to initialize functionality with docker-compose. Initially, the program builds the dataset with a preformatted Google Application-Program Interface (API) that iterates multiple times to gather Video Title and Comment Data; number of videos required for the analyst determines the total number of iterations to construct the dataset. Once the data is ingested by Spark in JSON format, it is stored in MongoDB. From Mongo, the data is read into Spark and stored separately into Cassandra’s wide-table format. The data is then read into Neo4j for relationship analysis with the organic Graph Database function. Spark is also used to conduct multiple Pandas representation of popular comments and to direct function for each database system employed.


## Details

This project includes

 - A **main** python notebook file that contains all the data
 - **Terminal commands** to boot up your Azure Lab Studio (assuming you have the proper docker setup)
 - Full **report** on Our findings
   
