# Data Engineering Nanodegree
## Capstone Project
Ashraf Hussain 
August 3, 2020

Data Engineer Nanodegree: 

## I. Definition

### Project Overview
On 31 December, 2019, the World Health Organization (WHO) was informed of an outbreak of “pneumonia of unknown cause” detected in Wuhan City, Hubei Province, China. Initially identified as coronavirus disease 2019, it quickly came to be known widely as COVID-19 and has resulted in an ongoing global pandemic. As of 5 Augest, 2020, more than 18.95 million cases have been reported across 188 countries and territories, resulting in more than 0.7 million deaths. More than 12.14 million people have recovered.[^1]

In response to this ongoing public health emergency, Johns Hopkins University (JHU), a private research university in Maryland, USA, developed an interactive web-based dashboard hosted by their Center for Systems Science and Engineering (CSSE). The dashboard visualizes and tracks reported cases in real-time, illustrating the location and number of confirmed COVID-19 cases, deaths and recoveries for all affected countries. It is used by researchers, public health authorities, news agencies and the general public.

In that project we will desgine a ETL procress to import csv files form [csse_covid_19_daily_reports_us](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us) by JHU which enriched by mapping USA Hospital Beds data from [USA Hospital Beds - COVID-19 | Definitive Healthcare](https://console.aws.amazon.com/dataexchange/home?region=us-east-1#/subscriptions/prod-ydzs6f2cju6qc). The fact table we will use [UID_ISO_FIPS_LookUp_Table.csv](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv "UID_ISO_FIPS_LookUp_Table.csv")

This project will tackel the ETL procress using the following tools:
 - [AWS CloudFormation](https://aws.amazon.com/cloudformation/): allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This gives you a single source of truth for your AWS and third party resources.
 - [Apache Airflow](https://airflow.apache.org/): Platform created by the community to programmatically author, schedule and monitor workflows.
 - [Amazon Redshift](https://aws.amazon.com/redshift/): The most popular and fastest cloud data warehouse
 - [AWS Data Exchange](https://aws.amazon.com/data-exchange/): makes it easy to find, subscribe to, and use third-party data in the cloud. Qualified data providers include category-leading brands such as Reuters, who curate data from over 2.2 million unique news stories per year in multiple languages; Change Healthcare, who process and anonymize more than 14 billion healthcare transactions and $1 trillion in claims annually; Dun & Bradstreet, who maintain a database of more than 330 million global business records; and Foursquare, whose location data is derived from 220 million unique consumers and includes more than 60 million global commercial venues

Hear are the summary of the steps we will take to ETL the data into redshift:

- AWS CloudFormation to setup our infrastructure.  
- AWS CloudFormation to bring in data from [JHU COVID-19 git repo](https://github.com/CSSEGISandData/COVID-19)
- AWS Data Exchange to subcribe to [USA Hospital Beds - COVID-19 | Definitive Healthcare](https://console.aws.amazon.com/dataexchange/home?region=us-east-1#/subscriptions/prod-ydzs6f2cju6qc).
- We will use Apache Airflow DAGs to select data for US only, marge the data into one table and move data from S3 to redshift


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

#### Set up the infrastructure
This procress could take up

##### Setup Redshift
1. Download [Data-Engineering-Capstone-Project-Redshift.yaml](https://github.com/sahussain/Data-Engineering-Capstone-Project/blob/master/Infrastructure/Data-Engineering-Capstone-Project-Redshift.yaml "Data-Engineering-Capstone-Project-Redshift.yaml")
2. Go to AWS Cloud Formation page
3. Click Create stack
4. Click upload file and choose [Data-Engineering-Capstone-Project-Redshift.yaml](https://github.com/sahussain/Data-Engineering-Capstone-Project/blob/master/Infrastructure/Data-Engineering-Capstone-Project-Redshift.yaml "Data-Engineering-Capstone-Project-Redshift.yaml")
5. Fill in the stack name as `redshift`
6. Fill in the `Parameters` and click `Next`
7. Don't fill any thing on `Configure stack options` and Click `Next`
8. On Review page click `Create stack`

##### Setup Airflow
```
The stack resources take around 15 minutes to create, while the airflow installation and bootstrap 
another 3 to 5 minutes. After that you can already access the Airflow UI and deploy your own Airflow DAGs.
```
1. Go to [Turbine git repo](https://github.com/villasv/aws-airflow-stack)
2. Scroll down until you see 'Deploy the stack` and click Launch stack
3. On the Create stack page click `Next`
4. Name your stack airflow and click `Next`. You don't need to change anything on this page
5. Don't fill any thing on `Configure stack options` and Click `Next`
6. On Review page Scroll down to `Capabilities` and check both 
	- I acknowledge that AWS CloudFormation might create IAM resources with custom names.
	- I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND
7. Click `Create stack`

#### Update Airflow security group to accept HTTP:
 1. Go to EC2 Dashboard
 2. Click Running instances
 3. Find 
 4. Select it the Instance with the name `turbine-webserver`
 5. Under Security Group select the group which contains the name `webserver`
 6. Click on Security group ID for the `webserver`
 7. Under inbound rules
 8. Click edit Edit inbound rules
 9. Click Add rule
 10. From the first(Type) Drop-down select Custom TCP
 11. In the port Range type 8080
 12. From the next drop-down(source) select my IP
 13. Click Save rules

#### Accessing Airflow:
1. Go to EC2 Dashboard
2.  Click Running instances
3. Find 
4. Select it the Instance with the name `turbine-webserver`
5. copy the `Public DNS (IPv4)`
6. open a browser window
7. past the link and add `:8080`



### IMPORTANT: Don't forget to shutdown everything. This is very simple
1. Go to AWS CloudFormation console 
2. Select stacks
3. Select `redshift` click `Delete`
4. Select `airflow` click `Delete`
5. The stack will shutdown everything correctly, do not delete Nested stacks or delete es2, s3 buckets independently. It will take up to 15 to 20 minutes to delete. If you don't have any CloudFormation then everything deleted correctly. 
6. Sometimes you will get an error `DELETE_FAILED` in this case you will have to go into `Events` and check why it failed to delete. There is a known error where the current Airflow is not emptying the S3 buckets if they are not empty. The workaround is to run the delete stack once then you get an error then go to S3 and empty the buckets and rerun delete stack. 

## II Database

### Step 1: Scope the Project and Gather Data
The following datasets will be used:
#### [JHU CSSE COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us) 
Provided By: Johns Hopkins University (JHU) via GitRepo

**Data Description**
This table contains an aggregation of each USA State level data.

**File naming convention**
MM-DD-YYYY.csv in UTC.

**Field description**
- **Province_State**  - The name of the State within the USA.
- **Country_Region**  - The name of the Country (US).
- **Last_Update**  - The most recent date the file was pushed.
- **Lat**  - Latitude.
- **Long_**  - Longitude.
- **Confirmed**  - Aggregated case count for the state.
- **Deaths**  - Aggregated death toll for the state.
- **Recovered**  - Aggregated Recovered case count for the state.
- **Active**  - Aggregated confirmed cases that have not been resolved (Active cases = total cases - total recovered - total deaths).
- **FIPS**  - Federal Information Processing Standards code that uniquely identifies counties within the USA.
- **Incident_Rate**  - cases per 100,000 persons.
- **People_Tested**  - Total number of people who have been tested.
- **People_Hospitalized**  - Total number of people hospitalized.
- **Mortality_Rate**  - Number recorded deaths * 100/ Number confirmed cases.
- **UID**  - Unique Identifier for each row entry.
- **ISO3**  - Officialy assigned country code identifiers.
- **Testing_Rate**  - Total test results per 100,000 persons. The "total test results" are equal to "Total test results (Positive + Negative)" from  [COVID Tracking Project](https://covidtracking.com/).
- **Hospitalization_Rate**  - US Hospitalization Rate (%): = Total number hospitalized / Number cases. The "Total number hospitalized" is the "Hospitalized – Cumulative" count from  [COVID Tracking Project](https://covidtracking.com/). The "hospitalization rate" and "Total number hospitalized" is only presented for those states which provide cumulative hospital data.

**Update frequency**
-   Once per day between 04:45 and 05:15 UTC.

**Formats**
-   CSV

**Data sources**
Refer to the  [mainpage](https://github.com/CSSEGISandData/COVID-19).

#### [USA Hospital Beds - COVID-19 | Definitive Healthcare](https://aws.amazon.com/marketplace/pp/USA-Hospital-Beds-COVID-19-Definitive-Healthcare/prodview-yivxd2owkloha)

Provided By: [Definitive Healthcare](https://www.definitivehc.com/) via AWS Data Exchange

**Data Description**
This resource includes data on numbers of licensed beds, staffed beds, ICU beds, and the bed utilization rate for the hospitals in the United States.

**Field description**
- **HOSPITAL_NAME** - Name of the hospital
- **HOSPITAL_TYPE** - Type of the hospital (see below for different types)
- **HQ_ADDRESS** - Civic street address of the hospital
- **HQ_ADDRESS1** - If there is a po box
- **HQ_CITY** - City of the hospital
- **HQ_STATE** - State of the hospital
- **HQ_ZIP_CODE** - Zip Code of the hospital
- **COUNTY_NAME** - County of the hospital
- **STATE_NAME** - State name in which hospital is located
- **STATE_FIPS** - Federal Information Processing Standard State code (FIPS) of the hospital in which it is located
- **CNTY_FIPS** - Full Federal Information Processing Standard County code (FIPS) of the hospital in which it is located
- **FIPS** - Federal Information Processing Standard County code (FIPS) of the hospital in which it is located
- **NUM_LICENSED_BEDS** - is the maximum number of beds for which a hospital holds a license to operate; however, many hospitals do not operate all the beds for which they are licensed. This number is obtained through DHC Primary Research. Licensed beds for Health Systems are equal to the total number of licensed beds of individual Hospitals within a given Health System.
- **NUM_STAFFED_BEDS** - is defined as an "adult bed, pediatric bed, birthing room, or newborn ICU bed (excluding newborn bassinets) maintained in a patient care area for lodging patients in acute, long term, or domiciliary areas of the hospital." Beds in labor room, birthing room, post-anesthesia, postoperative recovery rooms, outpatient areas, emergency rooms, ancillary departments, nurses and other staff residences, and other such areas which are regularly maintained and utilized for only a portion of the stay of patients (primarily for special procedures or not for inpatient lodging) are not termed a bed for these purposes. Definitive Healthcare sources Staffed Bed data from the Medicare Cost Report or Proprietary Research as needed. As with all Medicare Cost Report metrics, this number is self-reported by providers. Staffed beds for Health Systems are equal to the total number of staffed beds of individual Hospitals within a given Health System. Total number of staffed beds in the US should exclude Hospital Systems to avoid double counting. ICU beds are likely to follow the same logic as a subset of Staffed beds.
- **NUM_ICU_BEDS** - are qualified based on definitions by CMS, Section 2202.7, 22-8.2. These beds include ICU beds, burn ICU beds, surgical ICU beds, premature ICU beds, neonatal ICU beds, pediatric ICU beds, psychiatric ICU beds, trauma ICU beds, and Detox ICU beds.
- **ADULT_ICU_BEDS** - are qualified based on definitions by CMS, Section 2202.7, 22-8.2. These beds include ICU beds, burn ICU beds, surgical ICU beds, premature ICU beds, neonatal ICU beds, pediatric ICU beds, psychiatric ICU beds, trauma ICU beds, and Detox ICU beds. (Adult beds)
- **PEDI_ICU_BEDS** - are qualified based on definitions by CMS, Section 2202.7, 22-8.2. These beds include ICU beds, burn ICU beds, surgical ICU beds, premature ICU beds, neonatal ICU beds, pediatric ICU beds, psychiatric ICU beds, trauma ICU beds, and Detox ICU beds. (Pediatric beds)
- **BED_UTILIZATION** - is calculated based on metrics from the Medicare Cost Report: Bed Utilization Rate = Total Patient Days (excluding nursery days)/Bed Days Available
- **Potential_Increase_In_Bed_Capac** - This metric is computed by subtracting “Number of Staffed Beds from Number of Licensed beds” (Licensed Beds – Staffed Beds). This would provide insights into scenario planning for when staff can be shifted around to increase available bed capacity as needed.
- **AVG_VENTILATOR_USAGE** - number of average ventilators are use

**Hospital Definition:**  Definitive Healthcare defines a hospital as a healthcare institution providing inpatient, therapeutic, or rehabilitation services under the supervision of physicians. In order for a facility to be considered a hospital it must provide inpatient care.

_Hospital types are defined by the last four digits of the hospital’s Medicare Provider Number. If the hospital does not have a Medicare Provider Number, Definitive Healthcare determines the Hospital type by proprietary research._

**Hospital Types**

***Short Term Acute Care Hospital (STAC)***
-   Provides inpatient care and other services for surgery, acute medical conditions, or injuries
-   Patients care can be provided overnight, and average length of stay is less than 25 days

***Critical Access Hospital (CAH)***
-   25 or fewer acute care inpatient beds
-   Located more than 35 miles from another hospital
-   Annual average length of stay is 96 hours or less for acute care patients
-   Must provide 24/7 emergency care services
-   Designation by CMS to reduce financial vulnerability of rural hospitals and improve access to healthcare
-   Religious Non-Medical Health Care Institutions
-   Provide nonmedical health care items and services to people who need hospital or skilled nursing facility care, but for whom that care would be inconsistent with their religious beliefs

***Long Term Acute Care Hospitals***
-   Average length of stay is more than 25 days
-   Patients are receiving acute care - services often include respiratory therapy, head trauma treatment, and pain management
-   Rehabilitation Hospitals
-   Specializes in improving or restoring patients' functional abilities through therapies

***Children’s Hospitals***
-   Majority of inpatients under 18 years old

***Psychiatric Hospitals***
-   Provides inpatient services for diagnosis and treatment of mental illness 24/7
-   Under the supervision of a physician

***Veteran's Affairs (VA) Hospital***
-   Responsible for the care of war veterans and other retired military personnel
-   Administered by the U.S. VA, and funded by the federal government

***Department of Defense (DoD) Hospital***
-   Provides care for military service people (Army, Navy, Air Force, Marines, and Coast Guard), their dependents, and retirees (not all military service retirees are eligible for VA services)

**Update frequency**
-   Daily

**Formats**
-   AWS Data Exchange to S3 as CSV

#### [UID Lookup Table Logic](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv)

**Data Description**
This table contains the UID Lookup Table Logic for Federal Information Processing Standard County code (FIPS) mapping to State, City etc... .

**File naming convention**
UID_ISO_FIPS_LookUp_Table.csv

**Field description**
1.  All countries without dependencies (entries with only Admin0).

-   None cruise ship Admin0: UID = code3. (e.g., Afghanistan, UID = code3 = 4)
-   Cruise ships in Admin0: Diamond Princess UID = 9999, MS Zaandam UID = 8888.

2.  All countries with only state-level dependencies (entries with Admin0 and Admin1).

-   Demark, France, Netherlands: mother countries and their dependencies have different code3, therefore UID = code 3. (e.g., Faroe Islands, Denmark, UID = code3 = 234; Denmark UID = 208)
-   United Kingdom: the mother country and dependencies have different code3s, therefore UID = code 3. One exception: Channel Islands is using the same code3 as the mother country (826), and its artificial UID = 8261.
-   Australia: alphabetically ordered all states, and their UIDs are from 3601 to 3608. Australia itself is 36.
-   Canada: alphabetically ordered all provinces (including cruise ships and recovered entry), and their UIDs are from 12401 to 12415. Canada itself is 124.
-   China: alphabetically ordered all provinces, and their UIDs are from 15601 to 15631. China itself is 156. Hong Kong, Macau and Taiwan have their own code3.
-   Germany: alphabetically ordered all admin1 regions (including Unknown), and their UIDs are from 27601 to 27617. Germany itself is 276.
-   Italy: UIDs are combined country code (380) with  `codice_regione`, which is from  [Dati COVID-19 Italia](https://github.com/pcm-dpc/COVID-19). Exceptions: P.A. Bolzano is 38041 and P.A. Trento is 38042.

3.  The US (most entries with Admin0, Admin1 and Admin2).

-   US by itself is 840 (UID = code3).
-   US dependencies, American Samoa, Guam, Northern Mariana Islands, Virgin Islands and Puerto Rico, UID = code3. Their Admin0 FIPS codes are different from code3.
-   US states: UID = 840 (country code3) + 000XX (state FIPS code). Ranging from 8400001 to 84000056.
-   Out of [State], US: UID = 840 (country code3) + 800XX (state FIPS code). Ranging from 8408001 to 84080056.
-   Unassigned, US: UID = 840 (country code3) + 900XX (state FIPS code). Ranging from 8409001 to 84090056.
-   US counties: UID = 840 (country code3) + XXXXX (5-digit FIPS code).
-   Exception type 1, such as recovered and Kansas City, ranging from 8407001 to 8407999.
-   Exception type 2, only the New York City, which is replacing New York County and its FIPS code.
-   Exception type 3, Diamond Princess, US: 84088888; Grand Princess, US: 84099999.
-   Exception type 4, municipalities in Puerto Rico are regarded as counties with FIPS codes. The FIPS code for the unassigned category is defined as 72999.

4.  Population data sources.

-   United Nations, Department of Economic and Social Affairs, Population Division (2019). World Population Prospects 2019, Online Edition. Rev. 1.  [https://population.un.org/wpp/Download/Standard/Population/](https://population.un.org/wpp/Download/Standard/Population/)
-   eurostat:  [https://ec.europa.eu/eurostat/web/products-datasets/product?code=tgs00096](https://ec.europa.eu/eurostat/web/products-datasets/product?code=tgs00096)
-   The U.S. Census Bureau:  [https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html)
-   Mexico population 2020 projection:  [Proyecciones de población](http://sniiv.conavi.gob.mx/(X(1)S(kqitzysod5qf1g00jwueeklj))/demanda/poblacion_proyecciones.aspx?AspxAutoDetectCookieSupport=1)
-   Brazil 2019 projection: ftp://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2019/
-   Peru 2020 projection:  [https://www.citypopulation.de/en/peru/cities/](https://www.citypopulation.de/en/peru/cities/)
-   India 2019 population:  [http://statisticstimes.com/demographics/population-of-indian-states.php](http://statisticstimes.com/demographics/population-of-indian-states.php)
-   The Admin0 level population could be different from the sum of Admin1 level population since they may be from different sources.

Disclaimer: *The names of locations included on the Website correspond with the official designations used by the U.S. Department of State. The presentation of material therein does not imply the expression of any opinion whatsoever on the part of JHU concerning the legal status of any country, area or territory or of its authorities. The depiction and use of boundaries, geographic names and related data shown on maps and included in lists, tables, documents, and databases on this website are not warranted to be error free nor do they necessarily imply official endorsement or acceptance by JHU.


The end case is to have the data avaliable in Redshift so that we can build on my other project [Udacity-MLEN-CapstoneProject](https://github.com/sahussain/Udacity-MLEN-CapstoneProject) to forecast number of people cases (Confirmed, Deaths, Recovered, Active), Bed Utilization Rate caused by COVID-19 for a time duration of 30-days in United States based on historical data. This will help hospitals to better manage hospital's resource utilization.

**Update frequency**
-   Only when a new FIPS code added by U.S. Department of State.

**Formats**
-   CSV

### Step 2: Explore and Assess the Data
All data set is very clean and null fields are still used a case to filter for example in UID_ISO_FIPS_LookUp_Table a null value in Admin2 field is to donate a state level details. Since we will be only looking at US data the following filters are needed:

**UID_ISO_FIPS_LookUp_Table.csv**: will be used as fact table with the following filters, which will make sure that we only have US States. 
**Filters**:
- Country_Region = "US"
- Admin2 = NULL
- Province_State != Null
- FIPS <=100

**Columns that will be imported**: 
- FIPS
- Province_State
- Country_Region
- Lat
- Long_
- Population

**Sample**:
| FIPS | Province_State           | Country_Region | Lat     | Long_     | Population |
|------|--------------------------|----------------|---------|-----------|------------|
| 60   | American Samoa           | US             | -14.271 | -170.132  | 55641      |
| 66   | Guam                     | US             | 13.4443 | 144.7937  | 164229     |
| 69   | Northern Mariana Islands | US             | 15.0979 | 145.6739  | 55144      |
| 78   | Virgin Islands           | US             | 18.3358 | -64.8963  | 107268     |
| 72   | Puerto Rico              | US             | 18.2208 | -66.5901  | 2933408    |
| 1    | Alabama                  | US             | 32.3182 | -86.9023  | 4903185    |
| 2    | Alaska                   | US             | 61.3707 | -152.4044 | 731545     |
| 4    | Arizona                  | US             | 33.7298 | -111.4312 | 7278717    |
| 5    | Arkansas                 | US             | 34.9697 | -92.3731  | 3017804    |
| 6    | California               | US             | 36.1162 | -119.6816 | 39512223   |
| 8    | Colorado                 | US             | 39.0598 | -105.3111 | 5758736    |
| 9    | Connecticut              | US             | 41.5978 | -72.7554  | 3565287    |
| 10   | Delaware                 | US             | 39.3185 | -75.5071  | 973764     |
| 11   | District of Columbia     | US             | 38.8974 | -77.0268  | 705749     |
| 12   | Florida                  | US             | 27.7663 | -81.6868  | 21477737   |
| 13   | Georgia                  | US             | 33.0406 | -83.6431  | 10617423   |
| 15   | Hawaii                   | US             | 21.0943 | -157.4983 | 1415872    |
| 16   | Idaho                    | US             | 44.2405 | -114.4788 | 1787065    |
| 17   | Illinois                 | US             | 40.3495 | -88.9861  | 12671821   |
| 18   | Indiana                  | US             | 39.8494 | -86.2583  | 6732219    |
| 19   | Iowa                     | US             | 42.0115 | -93.2105  | 3155070    |


**JHU CSSE COVID-19 Dataset**: will be used as a dimension table and the following fields and filters will be imported:
 

### Step 3: Define the Data Model
### Step 4: Run ETL to Model the Data

Fellow the steps below to Run the ETL

#### Uploading Dags
On Raspberry Pi
1. Create a airflow folder in your home directory you can just use 
2. In terminal Clone git repo [turbine](https://github.com/villasv/aws-airflow-stack) by running `git clone https://github.com/villasv/aws-airflow-stack.git`
3. Copy airflow content form git repo to your airflow folder
4. Copy makefile to home folder
5. go to terminal and run the following command from your home dir 'make deploy stack-name=airflow'
6. if you get an error code 255 make sure that your aws config under .aws which is in your home folder only have the following line 
```
	[default]
	region = us-west-2
```
#### Add AWS credentials to Airflow Connections
use Airflow's UI to configure your AWS credentials and connection to Redshift.
1. To go to the Airflow UI
2. Click on the **Admin** tab and select **Connections**.
3. Under **Connections**, select **Create**.
4. On the create connection page, enter the following values:
	-   **Conn Id**: Enter  `aws_credentials`.
	-   **Conn Type**: Enter  `Amazon Web Services`.
	-   **Login**: Enter your  **Access key ID**  from the IAM User credentials you downloaded earlier.
	-   **Password**: Enter your  **Secret access key**  from the IAM User credentials you downloaded earlier.

Once you've entered these values, select  **Save**.

#### Add AWS redshift to Airflow Connections
Getting redshift connection settings:
1. Go to AWS CloudFormation console
2. click on redshift click on outputs
	here you'll find all the settings for redshift
3. To go to the Airflow UI
4. Click on the **Admin** tab and select **Connections**.
5. Under **Connections**, select **Create**.
6. On the create connection page, enter the following values:
	-   **Conn Id**: Enter  `redshift`.
	-   **Conn Type**: Enter  `Postgres`.
	-   **Host**: Enter the endpoint of your Redshift cluster, excluding the port at the end. **IMPORTANT: Make sure to  NOT**  include the port at the end of the Redshift endpoint string.
	-   **Schema**: Enter  `dev`. This is the Redshift database you want to connect to.
	-   **Login**: Enter  `awsuser`.
	-   **Password**: Enter the password you created when launching your Redshift cluster.
	-   **Port**: Enter  `5439`.

Once you've entered these values, select  **Save**.

### Step 5: Complete Project Write Up

## III. Conclusion





## Addressing other scenarios

### Data Increased by 100x:


### The pipelines would be run on a daily basis by 7 am every day:


### The database needed to be accessed by 100+ people:


------
# Appendix A
[^1]:[COVID-19 Dashboard](https://systems.jhu.edu/research/public-health/ncov/) by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University (JHU)". ArcGIS. Johns Hopkins University. Retrieved 20 June 2020.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkxMDIwNDQ5MCwtMTAyMjIwNjY4MywtOT
Y0NjY3NDM0LDE1ODkwMzYyMTMsOTczNDI5NzMzLC0xODAwOTY2
ODEwLDczMDgwNzI2OSwtMTk3MDQyMDU5OCw5NjEwMDc5MDMsMT
g4NjgyMjEzOSwxODg1ODE1NzY4LDExNjc4NDE4NSwxNDUwNjg2
Mjg4LDE2OTc5NTQ2ODcsLTI1MDYyMTU4MywyMDg5NDE2NzQ2LC
0xODYzOTc0OTg3LDEwMDYxODIzNjMsLTE2MTkxNDIxNTgsLTEz
NDc3MTYyNTRdfQ==
-->