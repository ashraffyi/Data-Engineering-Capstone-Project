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

#### Subscribe to Airflow Container
1. Go to [AWS Marketplace](https://aws.amazon.com/marketplace)
2. Search for Apache Airflow Scheduler Container Solution
3. Click Continue to `Subscribe`
4. wait for subscription to be activate
5. Click `Continue to Configuration`
6. Under `Delivery Method` select `Apache Airflow Scheduler`
7. Under `Software Version` select `1.10.10-3 (Jun 08, 2020)`
8. Click `Continue to Launch`
9. Click `View container image details` under `Container Images`
10. On the product fulfillment page, copy the URL to the AWS Marketplace registry. This URL also contains the container name and tag. You will need these details in the next step.

#### Create IAM Role for Kubernetes control plane to manage AWS resources on your behalf

1. Go to [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)
2. Click on Roles
3. Click Create Role
4. Under `Choose a use case` select EKS
5. Select `EKS - Cluster` 
6. Create the Role

#### IAM user:
 1. Create a new IAM user in your AWS account
 2. Give it `AdministratorAccess`, From `Attach existing policies directly` Tab
 3. Take note of the access key and secret 

#### Install AWS CLI
Follow the instructions on [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)

#### Generate An AWS Key Pair For The Worker Nodes
 1. create an Amazon EC2 key pair:
 2. Go to the Amazon EC2 console
 3. In the Navigation pane, click Key Pairs
 4. On the Key Pairs page, click Create Key Pair
 5. In the Create Key Pair dialog box, enter a name for your key pair, such as, mykeypair
 6. Make sure that you select ppk under File format
 7. Click Create
 8. Save the resulting PEM file in a safe location

#### Create Kubernetes cluster on AWS 
****This Could take up to 30 minutes****
1. Go to [https://console.aws.amazon.com/eks/](https://console.aws.amazon.com/eks/)
2. Click `Create cluster`
3. Name the cluster, leave all as default
4. Select `EKS - Cluster` Role
5. Click Next
6. Select Defaults for `Networking`
7. Under Cluster endpoint access select Public
8. Configure logging Optional
9. Click Next
10. Click Create

#### Update ElasticMapReduce-master security group to accept SSH:
 1. Go to EC2
 2. Under Network & Security select Security Group
 3. Select Security group ID with the name ElasticMapReduce-master
 4. Click edit Edit inbound rules
 5. Click Add rule
 6. From the first(Type) Drop-down select SSH
 7. From the next drop-down(source) select my IP
 8. Click Save rules


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
eyJoaXN0b3J5IjpbLTMwMjI0ODEzMSwtNTk4NzY3MTY4LC0xOT
g1ODQwNDEzLDE1NDY1NzYzOTgsMTk3NjIwNjY0MSwxMjg1ODA4
Nzg0LDIwMTUxNTg4NzRdfQ==
-->