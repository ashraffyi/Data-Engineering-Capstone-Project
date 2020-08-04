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

### Installing

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

#### Create a 

#### Create Kubernetes cluster on AWS
1. Go to [https://console.aws.amazon.com/eks/](https://console.aws.amazon.com/eks/)
2. Click `Create cluster`
3. Name the cluster, leave all as default
4. Select `EKS - Cluster` Role



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
eyJoaXN0b3J5IjpbLTE5ODU4NDA0MTMsMTU0NjU3NjM5OCwxOT
c2MjA2NjQxLDEyODU4MDg3ODQsMjAxNTE1ODg3NF19
-->