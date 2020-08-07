class SqlQueries:
    
    #Drop Tables
    table_drop= """
     DROP TABLE IF EXISTS {}
     """


    #Create Tables
    table_create_covidcases_stage= ("""
	CREATE TABLE IF NOT EXISTS covidcases_stage(
			FIPS                 integer NOT NULL,
			Last_Update          timestamp NOT NULL,
			Province_State       varchar(50),
			Country_Region       varchar(50),
			Lat                  decimal(18,0),
			Long_                decimal(18,0),
			Confirmed            integer,
			Deaths               integer,
			Recovered            integer,
			Active               integer,
			Incident_Rate        decimal(18,0),
			People_Tested        integer,
			People_Hospitalized  integer,
			Mortality_Rate       decimal(18,0),
			UID                  integer,
			ISO3                 integer,
			Testing_Rate         decimal(18,0),
			Hospitalization_Rate decimal(18,0)
			);

			COMMENT ON TABLE covidcases_stage IS 'This table contains an aggregation of each USA State level data.';

			COMMENT ON COLUMN covidcases_stage.FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN covidcases_stage.Province_State IS 'The name of the State within the USA.';
			COMMENT ON COLUMN covidcases_stage.Country_Region IS 'The name of the Country (US).';
			COMMENT ON COLUMN covidcases_stage.Lat IS 'Latitude.';
			COMMENT ON COLUMN covidcases_stage.Long_ IS 'Longitude';
			COMMENT ON COLUMN covidcases_stage.Confirmed IS 'Aggregated case count for the state.';
			COMMENT ON COLUMN covidcases_stage.Deaths IS 'Aggregated death toll for the state.';
			COMMENT ON COLUMN covidcases_stage.Recovered IS 'Aggregated Recovered case count for the state.';
			COMMENT ON COLUMN covidcases_stage.Active IS 'Aggregated confirmed cases that have not been resolved  (Active cases = total cases - total recovered - total deaths).';
			COMMENT ON COLUMN covidcases_stage.Incident_Rate IS 'cases per 100,000 persons.';
			COMMENT ON COLUMN covidcases_stage.People_Tested IS 'Total number of people who have been tested.';
			COMMENT ON COLUMN covidcases_stage.People_Hospitalized IS 'Total number of people hospitalized.';
			COMMENT ON COLUMN covidcases_stage.Mortality_Rate IS 'Number recorded deaths * 100/ Number confirmed cases.';
			COMMENT ON COLUMN covidcases_stage.UID IS 'Unique Identifier for each row entry.';
			COMMENT ON COLUMN covidcases_stage.ISO3 IS 'Officialy assigned country code identifiers.';
			COMMENT ON COLUMN covidcases_stage.Testing_Rate IS 'Total test results per 100,000 persons.';
			COMMENT ON COLUMN covidcases_stage.Hospitalization_Rate IS 'US Hospitalization Rate (%): = Total number hospitalized / Number cases.';
			COMMENT ON COLUMN covidcases_stage.Last_Update IS 'The most recent date the file was pushed.';
    """)
    
    table_create_hospital_stage = ("""
	CREATE TABLE IF NOT EXISTS hospital_stage(
			STATE_FIPS                      integer NOT NULL,
			X                               decimal(18,0),
			Y                               decimal(18,0),
			OBJECTID                        integer,
			HOSPITAL_NAME                   varchar(50),
			HOSPITAL_TYPE                   varchar(50),
			HQ_ADDRESS                      varchar(50),
			HQ_ADDRESS1                     varchar(50),
			HQ_CITY                         varchar(50),
			HQ_STATE                        varchar(50),
			HQ_ZIP_CODE                     integer,
			COUNTY_NAME                     varchar(50),
			STATE_NAME                      varchar(50),
			CNTY_FIPS                       integer,
			NUM_LICENSED_BEDS               integer,
			NUM_STAFFED_BEDS                integer,
			NUM_ICU_BEDS                    integer,
			ADULT_ICU_BEDS                  integer,
			PEDI_ICU_BEDS                   integer,
			BED_UTILIZATION                 decimal(18,0),
			Potential_Increase_In_Bed_Capac integer,
			AVG_VENTILATOR_USAGE            integer
			);

			COMMENT ON TABLE hospital_stage IS 'This resource includes data on numbers of licensed beds, staffed beds, ICU beds, and the bed utilization rate for the hospitals in the United States.';

			COMMENT ON COLUMN hospital_stage.STATE_FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN hospital_stage.X IS 'Latitude.';
			COMMENT ON COLUMN hospital_stage.Y IS 'Longitude';
			COMMENT ON COLUMN hospital_stage.OBJECTID IS 'unique Hospital identifier';
			COMMENT ON COLUMN hospital_stage.HOSPITAL_NAME IS 'Name of the hospital';
			COMMENT ON COLUMN hospital_stage.HOSPITAL_TYPE IS 'Type of the hospital (see below for different types)';
			COMMENT ON COLUMN hospital_stage.HQ_ADDRESS IS 'line 1 Civic street address of the hospital';
			COMMENT ON COLUMN hospital_stage.HQ_ADDRESS1 IS 'line 2 of Civic street address of the hospital';
			COMMENT ON COLUMN hospital_stage.HQ_CITY IS 'City of the hospital';
			COMMENT ON COLUMN hospital_stage.HQ_STATE IS 'State of the hospital';
			COMMENT ON COLUMN hospital_stage.HQ_ZIP_CODE IS 'Zip Code of the hospital';
			COMMENT ON COLUMN hospital_stage.COUNTY_NAME IS 'County of the hospital';
			COMMENT ON COLUMN hospital_stage.STATE_NAME IS 'State name in which hospital is located';
			COMMENT ON COLUMN hospital_stage.CNTY_FIPS IS 'Full Federal Information Processing Standard County code (FIPS) of the hospital in which it is locate';
			COMMENT ON COLUMN hospital_stage.NUM_LICENSED_BEDS IS 'Full Federal Information Processing Standard County code (FIPS) of the hospital in which it is located';
			COMMENT ON COLUMN hospital_stage.NUM_STAFFED_BEDS IS 'is the maximum number of beds for which a hospital holds a license to operate;';
			COMMENT ON COLUMN hospital_stage.NUM_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital_stage.ADULT_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital_stage.PEDI_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital_stage.BED_UTILIZATION IS 'is calculated based on metrics from the Medicare Cost Report: Bed Utilization Rate = Total Patient Days (excluding nursery days)/Bed Days Available';
			COMMENT ON COLUMN hospital_stage.Potential_Increase_In_Bed_Capac IS 'This metric is computed by subtracting “Number of Staffed Beds from Number of Licensed beds” (Licensed Beds – Staffed Beds).';
			COMMENT ON COLUMN hospital_stage.AVG_VENTILATOR_USAGE IS 'number of average ventilators are use';
    """)

    table_create_masternode_stage = ("""
	CREATE TABLE IF NOT EXISTS masternode_stage(
			FIPS           integer NOT NULL,
			UID            integer NOT NULL,
			iso2           varchar(50) NOT NULL,
			iso3           varchar(50) NOT NULL,
			code3          integer NOT NULL,
			Admin2         varchar(50) NOT NULL,
			Province_State varchar(50) NOT NULL,
			Country_Region varchar(50) NOT NULL,
			Lat            decimal(18,0) NOT NULL,
			Long_          decimal(18,0) NOT NULL,
			Combined_Key   varchar(50) NOT NULL,
			Population     integer NOT NULL
			);

			COMMENT ON TABLE masternode_stage IS 'This table contains the UID Lookup Table Logic for Federal Information Processing Standard County code (FIPS) mapping to State, Lat, Long etc...';

			COMMENT ON COLUMN masternode_stage.FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN masternode_stage.UID IS 'State';
			COMMENT ON COLUMN masternode_stage.iso2 IS 'US states: UID = 840 (country code3) + 000XX (state FIPS code). Ranging from 8400001 to 84000056.';
			COMMENT ON COLUMN masternode_stage.iso3 IS 'ISO country code';
			COMMENT ON COLUMN masternode_stage.code3 IS 'Officialy assigned country code identifiers.';
			COMMENT ON COLUMN masternode_stage.Admin2 IS 'County name. US only.';
			COMMENT ON COLUMN masternode_stage.Province_State IS 'Province, state or dependency name.';
			COMMENT ON COLUMN masternode_stage.Country_Region IS 'Country, region or sovereignty name. The names of locations included on the Website correspond with the official designations used by the U.S. Department of State.';
			COMMENT ON COLUMN masternode_stage.Lat IS 'Center point of State in latitude';
			COMMENT ON COLUMN masternode_stage.Long_ IS 'Center point of State in longitude';
			COMMENT ON COLUMN masternode_stage.Combined_Key IS 'Admin2 + Province_State + Country_Region';
			COMMENT ON COLUMN masternode_stage.Population IS 'population of the State';
    """)

    table_create_covidcases = ("""
	CREATE TABLE IF NOT EXISTS covidcases(
			FIPS                 integer NOT NULL,
			Last_Update          timestamp NOT NULL,
			Confirmed            integer,
			Deaths               integer,
			Recovered            integer,
			Active               integer,
			Incident_Rate        decimal(18,0),
			People_Tested        integer,
			People_Hospitalized  integer,
			Mortality_Rate       decimal(18,0),
			Testing_Rate         decimal(18,0),
			Hospitalization_Rate decimal(18,0)
			);

			COMMENT ON TABLE covidcases IS 'This table contains an aggregation of each USA State level data.';

			COMMENT ON COLUMN covidcases.FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN covidcases.Confirmed IS 'Aggregated case count for the state.';
			COMMENT ON COLUMN covidcases.Deaths IS 'Aggregated death toll for the state.';
			COMMENT ON COLUMN covidcases.Recovered IS 'Aggregated Recovered case count for the state.';
			COMMENT ON COLUMN covidcases.Active IS 'Aggregated confirmed cases that have not been resolved  (Active cases = total cases - total recovered - total deaths).';
			COMMENT ON COLUMN covidcases.Incident_Rate IS 'cases per 100,000 persons.';
			COMMENT ON COLUMN covidcases.People_Tested IS 'Total number of people who have been tested.';
			COMMENT ON COLUMN covidcases.People_Hospitalized IS 'Total number of people hospitalized.';
			COMMENT ON COLUMN covidcases.Mortality_Rate IS 'Number recorded deaths * 100/ Number confirmed cases.';
			COMMENT ON COLUMN covidcases.Testing_Rate IS 'Total test results per 100,000 persons.';
			COMMENT ON COLUMN covidcases.Hospitalization_Rate IS 'US Hospitalization Rate (%): = Total number hospitalized / Number cases.';
			COMMENT ON COLUMN covidcases.Last_Update IS 'The most recent date the file was pushed.';
    """)

    table_create_masternode = ("""
	CREATE TABLE IF NOT EXISTS masternode(
			FIPS           integer NOT NULL,
			Province_State varchar(50) NOT NULL,
			Lat            decimal(18,0) NOT NULL,
			Long_          decimal(18,0) NOT NULL,
			Population     integer
			);

			COMMENT ON TABLE masternode IS 'This table contains the UID Lookup Table Logic for Federal Information Processing Standard County code (FIPS) mapping to State, Lat, Long etc...';
	
			COMMENT ON COLUMN masternode.FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN masternode.Province_State IS 'Province, state or dependency name.';
			COMMENT ON COLUMN masternode.Lat IS 'Center point of State in latitude';
			COMMENT ON COLUMN masternode.Long_ IS 'Center point of State in longitude';
			COMMENT ON COLUMN masternode.Population IS 'population of the State';

    """)

    table_create_hospital = ("""
	CREATE TABLE IF NOT EXISTS hospital(
			FIPS                      		integer NOT NULL,
			HOSPITAL_NAME                   varchar(50) NOT NULL,
			HOSPITAL_TYPE                   varchar(50) NOT NULL,
			NUM_LICENSED_BEDS               integer NOT NULL,
			NUM_STAFFED_BEDS                integer NOT NULL,
			NUM_ICU_BEDS                    integer NOT NULL,
			ADULT_ICU_BEDS                  integer NOT NULL,
			PEDI_ICU_BEDS                   integer NOT NULL,
			BED_UTILIZATION                 decimal(18,0) NOT NULL,
			Potential_Increase_In_Bed_Capac integer NOT NULL,
			AVG_VENTILATOR_USAGE            integer NOT NULL
			);

			COMMENT ON TABLE hospital IS 'This resource includes data on numbers of licensed beds, staffed beds, ICU beds, and the bed utilization rate for the hospitals in the United States.';

			COMMENT ON COLUMN hospital.FIPS IS 'Federal Information Processing Standards code that uniquely identifies counties within the USA.';
			COMMENT ON COLUMN hospital.HOSPITAL_NAME IS 'Name of the hospital';
			COMMENT ON COLUMN hospital.HOSPITAL_TYPE IS 'Type of the hospital (see below for different types)';
			COMMENT ON COLUMN hospital.NUM_LICENSED_BEDS IS 'Full Federal Information Processing Standard County code (FIPS) of the hospital in which it is located';
			COMMENT ON COLUMN hospital.NUM_STAFFED_BEDS IS 'is the maximum number of beds for which a hospital holds a license to operate;';
			COMMENT ON COLUMN hospital.NUM_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital.ADULT_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital.PEDI_ICU_BEDS IS 'are qualified based on definitions by CMS, Section 2202.7, 22-8.2.';
			COMMENT ON COLUMN hospital.BED_UTILIZATION IS 'is calculated based on metrics from the Medicare Cost Report: Bed Utilization Rate = Total Patient Days (excluding nursery days)/Bed Days Available';
			COMMENT ON COLUMN hospital.Potential_Increase_In_Bed_Capac IS 'This metric is computed by subtracting “Number of Staffed Beds from Number of Licensed beds” (Licensed Beds – Staffed Beds).';
			COMMENT ON COLUMN hospital.AVG_VENTILATOR_USAGE IS 'number of average ventilators are use';
    """)
    
    
    #Insert
    table_insert_covidcases = ("""
        SELECT FIPS, Last_Update, Confirmed, Deaths, Recovered, Active, Incident_Rate, People_Tested, People_Hospitalized, Mortality_Rate, Testing_Rate, Hospitalization_Rate
        FROM covidcases_stage
        WHERE Last_Update IS NULL AND FIPS <=100
    """)

    table_insert_masternode = ("""
        SELECT FIPS, Province_State, Lat, Long_, Population
        FROM masternode_stage
		WHERE Country_Region = 'US' AND Admin2 IS  NULL AND Province_State IS NOT NULL AND FIPS <=100
    """)

    table_insert_hospital = ("""
        SELECT STATE_FIPS AS FIPS, HOSPITAL_NAME, HOSPITAL_TYPE, NUM_LICENSED_BEDS, NUM_STAFFED_BEDS, NUM_ICU_BEDS, ADULT_ICU_BEDS, PEDI_ICU_BEDS, BED_UTILIZATION, Potential_Increase_In_Bed_Capac, AVG_VENTILATOR_USAGE
        FROM hospital_stage
		WHERE STATE_FIPS<100
    """)
    
    copy_sql = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        IGNOREHEADER 1
        DELIMITER ','
    """