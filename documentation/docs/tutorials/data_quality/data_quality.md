# Data Quality Tests Documentation

## Overview
This documentation outlines the data quality checks implemented for the Adventureworks database, specifically focusing on the `department` and other related tables. The tests ensure the integrity and validity of the data to maintain high-quality standards.

## Files Structure
The data quality checks are defined in three YAML files:


### 1. `check_integrity.yml`
This file contains checks to ensure the integrity and validity of data in the `department` table. The following checks are performed:

- **Row Count**: Ensures the row count is between 1 and 23.
- **Missing Department IDs**: Checks that there are no missing department IDs.
- **Invalid Department IDs**: Validates that all department IDs are within the range of 1 to 30.
- **Duplicate Department IDs**: Ensures there are no duplicate department IDs.
- **Duplicate Names**: Ensures there are no duplicate names.
- **Valid Names**: Checks that the `name` column contains exactly four valid entries: 
  - 'Marketing'
  - 'Sales'
  - 'Gambiarra Analyst'
  - 'Tech Lead'

### 2. `check_schema.yml`
This file contains schema checks for multiple tables within the `humanresources` schema.

- **HumanresourcesDepartment Table**:
  - Checks for missing required columns: `departmentid`, `name`, `groupname`, `modifieddate`
  - Validates column types:
    - `departmentid`: integer
    - `name`: text
    - `groupname`: text
    - `modifieddate`: timestamp

- **HumanresourcesEmployee Table**:
  - Checks for missing required columns: `businessentityid`, `nationalidnumber`, `loginid`, `jobtitle`, `birthdate`, `maritalstatus`, `gender`, `hiredate`, `salariedflag`, `vacationhours`, `sickleavehours`, `currentflag`, `rowguid`, `modifieddate`, `organizationnode`
  - Validates column types:
    - `businessentityid`: integer
    - `nationalidnumber`: text
    - `loginid`: text
    - `jobtitle`: text
    - `birthdate`: date
    - `maritalstatus`: character
    - `gender`: character
    - `hiredate`: date
    - `salariedflag`: boolean
    - `vacationhours`: smallint
    - `sickleavehours`: smallint
    - `currentflag`: boolean
    - `rowguid`: uuid
    - `modifieddate`: timestamp
    - `organizationnode`: text

- **Other Tables**: Similar schema checks are defined for the `HumanresourcesEmployeedepartmenthistory`, `HumanresourcesEmployeepayhistory`, `HumanresourcesJobcandidate`, and `HumanresourcesShift` tables, ensuring all required columns and correct data types are validated.

### 3. `configuration.yml`
This file contains the configuration details for connecting to the PostgreSQL database.

```yaml
data_source conn_postgres:
  type: postgres
  connection:
    host: 172.21.121.140
    port: '5435'
    username: postgres
    password: postgres
    database: Adventureworks
    schema: humanresources
```

## How to Run the Data Quality Checks?

1 - Activate the Virtual Environment 

2 - Run command:
```
soda scan -d conn_postgres -c configuration.yml check_integrity.yml
soda scan -d conn_postgres -c configuration.yml check_schema.yml
```
