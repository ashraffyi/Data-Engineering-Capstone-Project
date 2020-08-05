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
1. Follow the instructions on [install-cliv2-windows.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
2. Run `aws configure`
3. Past access key and secret 

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

#### Update eks-cluster-sg-udacityDataEng1-349815526 security group to accept SSH:
 1. Go to EC2
 2. Under Network & Security select Security Group
 3. Select Security group ID with the name ElasticMapReduce-master
 4. Click edit Edit inbound rules
 5. Click Add rule
 6. From the first(Type) Drop-down select SSH
 7. From the next drop-down(source) select my IP
 8. Click Save rules

***putty SSH Tunnel:***
 1.  Double-click  `putty.exe`  to start PuTTY. You can also launch PuTTY from the Windows programs list.    
 3.  If necessary, in the  **Category**  list, choose  **Session**.
 4.  In the  **Host Name**  field, type  `hadoop@``MasterPublicDNS`. For example:  `hadoop@``ec2-###-##-##-###.compute-1.amazonaws.com`.
 5.  In the  **Category**  list, expand  **Connection > SSH**, and then choose  **Auth**.
 6.  For  **Private key file for authentication**, choose  **Browse**  and select the  `.ppk`  file that you generated.
 7.  In the  **Category**  list, expand  **Connection > SSH**, and then choose  **Tunnels**.
 8.  In the  **Source port**  field, type  `8157`  (an unused local port).
 9.  Leave the  **Destination**  field blank.
10.  Select the  **Dynamic**  and  **Auto**  options.
11.  Choose  **Add**  and  **Open**.
12.  Choose  **Yes**  to dismiss the PuTTY security alert.
see [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel.html)

- Configure FoxyProxy for Google Chrome
 1.  See  [https://chrome.google.com/webstore/search/foxy%20proxy](https://chrome.google.com/webstore/search/foxy%20proxy)  and follow the links and instructions to add FoxyProxy to Chrome.
    
 2.  Using a text editor, create a file named  `foxyproxy-settings.xml`  with the following contents:

 ```xml
 <?xml version="1.0" encoding="UTF-8"?>
<foxyproxy>
   <proxies>
      <proxy name="emr-socks-proxy" id="2322596116" notes="" fromSubscription="false" enabled="true" mode="manual" selectedTabIndex="2" lastresort="false" animatedIcons="true" includeInCycle="true" color="#0055E5" proxyDNS="true" noInternalIPs="false" autoconfMode="pac" clearCacheBeforeUse="false" disableCache="false" clearCookiesBeforeUse="false" rejectCookies="false">
         <matches>
            <match enabled="true" name="*ec2*.amazonaws.com*" pattern="*ec2*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*ec2*.compute*" pattern="*ec2*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="10.*" pattern="http://10.*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*10*.amazonaws.com*" pattern="*10*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*10*.compute*" pattern="*10*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" /> 
            <match enabled="true" name="*.compute.internal*" pattern="*.compute.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>
            <match enabled="true" name="*.ec2.internal* " pattern="*.ec2.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>	  
	   </matches>
         <manualconf host="localhost" port="8157" socksversion="5" isSocks="true" username="" password="" domain="" />
      </proxy>
   </proxies>
</foxyproxy>

 ```
    
 3.  Manage extensions in Chrome (go to  **chrome://extensions**).
    
 4.  Choose  **Options**  for FoxyProxy Standard.
    
 5.  On the  **FoxyProxy**  page, choose  **Import/Export**.
    
 6.  On the  **Import/Export**  page, choose  **Choose File**, browse to the location of the  `foxyproxy-settings.xml`  file you created, select the file, and choose  **Open**.
    
 7.  Choose  **Replace**  when prompted to overwrite the existing settings.
    
 8.  For  **Proxy mode**, choose  **Use proxies based on their predefined patterns and priorities**.
 see [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html)


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
eyJoaXN0b3J5IjpbMjAxNDUxNjA2LDE5ODA1NjE0NDUsLTU5OD
c2NzE2OCwtMTk4NTg0MDQxMywxNTQ2NTc2Mzk4LDE5NzYyMDY2
NDEsMTI4NTgwODc4NCwyMDE1MTU4ODc0XX0=
-->