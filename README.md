# Analysis of NYC 311 Service Requests

##  Final Project for CS GY 6513 Big Data 
### New York University - Tandon School of Engineering

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

NYC 311 is a service provided by the city of New York that allows residents to report non-emergency issues and request city services. The service was launched in 2003 as a way to improve communication between the city and its residents, and to provide a single point of contact for non-emergency issues.
The objective of analyzing NYC 311 service requests was to to gain insights into the needs and concerns of New York City residents, and to help the city improve its services.


## Dataset 
The data used in this project was obtained from NYC Open Data's 311 Service Requests from 2010 to Present. 311 Service Requests encompass all non-emergency requests from the city, including but not limited to noise complaints, air quality issues and reports of unsanitary conditions etc. The 311 calls in New York City (NYC) are publicly available. 311 service request dataset is available at https://data.cityofnewyork.us/Social-Services/311- Service-Requests- from-2010-to-Present/erm2-nwe9 . 

This project uses a subset of the data from 2022 that was accessed with the API - https://data.cityofnewyork.us/resource/erm2-nwe9.json which has fetched the data for the months of November and December 2022. 

## Technologies Used
1. Apache Kafka [2.0.2] Apache Kafka is a framework implementation of a software bus using stream-processing.The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.
2. Apache Spark [3.3.1] Apache Spark is an open source unified analytics engine for large scale data processing Spark provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.
3. Python [3.8] Python is an interpreted high level general purpose programming language Python's design philosophy emphasizes code readability with its notable use of significant indentation.
4. PySpark [3.3.1] PySpark is an interface for Apache Spark in Python It not only allows you to write Spark applications using Python APIs, but also provides the PySpark shell for interactively analyzing your data in a distributed environment.
5. Git /GitHub It is a provider of Internet hosting for software development and version control using Git It offers the distributed version control and source code management functionality of Git.

## How to Run the Project
1. Install all the requirements from requirements.txt using 
```
pip install requirements.txt
```
2. Run Zookeeper to maintain Kafka, command to be run from Kafka root dir
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
3. Start Kafka server, aditional servers can be added as per requirement.
```
bin/kafka-server-start.sh config/server.properties
```
4. Create a kafka topic,to allow the users to send and receive data between Kafka Servers
```
 bin/kafka-topics.sh --create --topic bigdata  --bootstrap-server localhost:9092
```
5. Start prod.py to start reading data from the API stream and store it in ```bigdata``` topic
6. Start consumer.ipynb  to consume the stream from the ```bigdata``` topic
7. The data will be stored locally in a folder called bdprojj
8. This data will then be fetched by ```Big Data Project (1).ipynb ``` to analyze and create insightful visualizations on the Dashboard
9. The visualisations will be seen on the Dashboard on 
```
127.0.0.1:8050
````















