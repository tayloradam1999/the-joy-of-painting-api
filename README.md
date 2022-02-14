# the-joy-of-painting-api

## Resources
- [Bob Ross Episode Data CSV](https://intranet.hbtn.io/rltoken/X5EpmCHlJFa4Ve11jJvKaw)
- [Bob Ross Paint Color Details CSV](https://intranet.hbtn.io/rltoken/LkOkYqhJjneq4PSWxRSLOQ)

## Project Context
In this project we are going to explore the idea of ETL (Extract, Transform, Load), which is the process of taking data from multiple unique sources, modifying them in some way, and then storing them in a centralized database. This is a very common practice when collecting data from systems in order to utilize that data in another system. This data may come in the form of CSV, JSON, XML, API requests with other custom formats, etc - it might even be that you have direct access to several databases with different, but relatable data that you want to be merged into another database in order to gain insight from it in some way.

## Presented Problem
Your local public broadcasting station has an overwhelming amount of requests for information on The Joy of Painting. Their viewers want a website that allows them to filter the 403 episodes based on the following criteria:
  
- Month of original broadcast  
  - This will be useful for viewers who wish to watch paintings that were done during that same month of the year  
- Subject Matter  
  - This will be useful for viewers who wish to watch specific items get painted  
- Color Palette  
  - This will be useful for viewers who wish to watch specific colors being used in a painting  

Your local broadcasting station has already done some leg work to gather data, however it is spread out across multiple different files and formats, which makes the data unusable in its current form. They’ve also already hired another team to build a front-end to allow their viewers to filter episodes of The Joy of Painting and now they’ve hired you to help them with the process of designing and building a database that will house this collected data in a way that is usable and also build an API to access it.

## Supplied Datasets
***Internal download links***
- [Dataset 1](https://intranet.hbtn.io/rltoken/S6crSk1ADjQ720PLhC74Ug)
- [Dataset 2](https://intranet.hbtn.io/rltoken/5NbBTeENaBzGoRMpfVTtRQ)
- [Dataset 3](https://intranet.hbtn.io/rltoken/sph2Amdu_N58D7HTfbttsQ)

## Workflow
- Design a Database
  - Create a design document using UML documentation for the database
  - Create the SQL scripts required to create database from scratch
    - SQL scripts must run locally
	- Free choice of SQL databases (I chose PostgreSQL)
- Extract, Transform, Load
  - Write custom scripts in python that import our datasets correctly from the given files into our new database.
  - Validate all data matches correctly before commiting to storage.
    - Handle data validation via script or via the data-cleanup process
- Create the API
- Endpoints must handle the following
  - Month of original broadcast
    - This will be useful for viewers who wish to watch paintings that were done during that same month of the year
  - Subject Matter
    - This will be useful for viewers who wish to watch specific items get painted
  - Color Palette
    - This will be useful for viewers who wish to watch specific colors being used in a painting
- API Requirements:
  - Must run locally and communication with your database to get data to the user
  - Must acccept parameters via the URL, query parameters, or even as POST data in the body
  - Must return JSON with a list of episode information.
- **Note:** Multiple filters should be usable at the same time and filters should allow the user to select multiple items (like selecting multiple colors to filter by). 
  - When multiple filters are selected, the user should be able to specify if the filter should look for episodes that match all of the selected filters (meaning all filters must apply to every episode that is returned) OR be able to set the filters to look for an episode that includes one or more matches (a union of the filters, for example: one episode matches one of the colors selected but not the object painted while another episode matches on the month it aired, but not the color or object drawn).
  
## Deadline Reached
As the deadline was reached, I was not able to meet all of this project's requirements. I fell short in time when it came to creating the API, but I was able to achieve the following:
- Creating the database with the format of my UML design document (using PostgreSQL, a database which I have never used prior to working on this project)
- Using Pandas to handle the ETL process
- Using DBeaver's GUI to view my local postgres database
- Validate all data matches correctly before commiting to storage  
  
At the end of it all, I am very happy with my takeaway from this project. I am now exponentially more comfortable with the ETL process alongside utilizing data visualization applications and interfaces. Luckily enough, our next project expands on everything I have learned through the duration of this project, and I am very excited to continue expanding my knowledge of ETL and data visualization.