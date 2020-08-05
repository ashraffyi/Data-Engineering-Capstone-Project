# Data Engineering Nanodegree
## Capstone Project
Ashraf Hussain 
August 3, 2020

Data Engineer Nanodegree: 

## I. Definition

### Project Overview
The purpose of the data engineering capstone project is to give a chance to combine what you've learned throughout the program. This project will be an important part of your portfolio that will help you achieve your data engineering-related career goals.

In this project, you can choose to complete the project provided for you, or define the scope and data for a project of your own design. Either way, you'll be expected to go through the same steps outlined below.

### Problem Statement


### Prerequisites

#### IAM user:
 1. Create a new IAM user in your AWS account
 2. Give it `AdministratorAccess`, From `Attach existing policies directly` Tab
 3. Take note of the access key and secret 

#### Install AWS CLI and Configure
 1. Follow the instructions on 
	 - [Installing the AWS CLI version 2 on Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
	 - [Configure the AWS CLI on a Raspberry Pi](https://ownthe.cloud/posts/configure-aws-cli-on-raspberry-pi/)
3. Run `aws configure`
4. Past access key and secret 

#### Generate An AWS Key Pair for Airflow
 1. create an Amazon EC2 key pair:
 2. Go to the Amazon EC2 console
 3. In the Navigation pane, click Key Pairs
 4. On the Key Pairs page, click Create Key Pair
 5. In the Create Key Pair dialog box, enter a name for your key pair, such as, mykeypair
 6. Make sure that you select ppk under File format
 7. Click Create
 8. Save the resulting PEM file in a safe location

#### Update eks-cluster-sg-udacityDataEng1-349815526 security group to accept SSH:
 1. Go to EC2
 2. 
 3. Under Network & Security select Security Group
 4. Select Security group ID with the name ElasticMapReduce-master
 5. Click edit Edit inbound rules
 6. Click Add rule
 7. From the first(Type) Drop-down select SSH
 8. From the next drop-down(source) select my IP
 9. Click Save rules


## II Database

###  Schema Design

### ELT Pipeline

### Project Datasets

### Fact Table


### Dimension Tables


## III. Conclusion





## Addressing other scenarios

### Data Increased by 100x:


### The pipelines would be run on a daily basis by 7 am every day:


### The database needed to be accessed by 100+ people:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEwODY3MzY2OCw0NzkxMDgzNDMsMTk4MD
U2MTQ0NSwtNTk4NzY3MTY4LC0xOTg1ODQwNDEzLDE1NDY1NzYz
OTgsMTk3NjIwNjY0MSwxMjg1ODA4Nzg0LDIwMTUxNTg4NzRdfQ
==
-->