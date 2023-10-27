# Hacktoberfest 2023 project: building ETL and RAG pipelines with open source 

# **Team's project:** Extract Transform Load (ETL) pipeline of Adidas sales and further product information, with an analytics component for sales trends and successful product identification, competitive research, and more
*All team members have completed all steps in the [set up](setup.md) document.*

## Description 

We've developed an ETL (Extract, Transform, Load) pipeline for data analysis automation, specific to Adidas sales and main competitor sales, based on the provided datasets on section **Data sources**. This we think, can help address several important business problems and drive informed decision-making, for Adidas and for anyone in hopes of better understanding one's business as the ideas discussed here are universal. 

We hope our project provides Adidas with a comprehensive understanding of its sales and customer data on a simple Dashboard over an easy to mantain, modify and improve data process. This knowledge can be used to make data-driven decisions, tailor marketing strategies, optimize product offerings, improve customer satisfaction, and align business strategies with customer needs and preferences.

Appart from the contribution of our own insights displayed through our EDA (Exploratory Data Analysis); With the help of the good people from [Ploomber](https://ploomber.io/), we've build an application (Dashboard) with [JupySQL](https://jupysql.ploomber.io/en/latest/quick-start.html) + [Voila](https://voila.readthedocs.io/en/stable/index.html) as framework, with the use of a pipeline to prepare the data (ETL) automatically by tasks (see .yaml), and in the process generate subsecuent products as reports or logs (metadata), and Dashboard updates. We perform dataset extraction from 3 different Kaggle sources, cleaning, organizing and saving to an in-memory database [DuckDB](https://duckdb.org/) once prepared for storage and subsequent data analysis. Application is [Dockerized](https://www.docker.com/) as well. We used [MotherDuck](https://motherduck.com/docs/intro) for in-cloud data storage for our application.

## Data sources

The following are the used data sources, all of public domain: 
1. [adidas-sales-dataset](https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset) by Heemali Chaudhari licensed under CC0 1.0.
    * Adidas sales dataset is a collection of data that includes information on the sales of Adidas products. This type of dataset may include details such as the number of units sold, the total sales revenue, the location of the sales, the type of product sold, and any other relevant information.
    * It contains 9652 rows and 14 columns in total. (698.66 kB)
2. [adidas-vs-nike](https://www.kaggle.com/datasets/kaushiksuresh147/adidas-vs-nike/) by Kaushik Suresh licensed under CC0 1.0.
    * Contains product information about Nike and Adidas (Adidas is further divided into sub-brands), feature information including their ratings, discount, sales price, listed price, product description, and the number of reviews.
    * It contains 3268 rows and 10 columns in total. (1.21 MB)
3. [customer-shopping-trends-dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data) by Sourav Banerjee licensed under CC0 1.0.
    * The Customer Shopping Preferences Dataset offers valuable insights into consumer behavior and purchasing patterns. This dataset captures a wide range of customer attributes including age, gender, purchase history, preferred payment methods, frequency of purchases, and more.
    * It contains 3900 rows and 18 columns in total. (453.25 kB)

*Specific provenance is listed for all datasets in the respective Kaggle websites.*

## Methods / Métodos

Describe the methods you are using. Include a description of the tools you are using.

## User interface your project will have / Interfaz de usuario que tendrá su proyecto

Describe the user interface your project will have. Include a description of the tools you are using.

Options: 

1. FastAPI application
2. Chainlit application
3. Voila dashboard

## Team members/ Miembros del equipo

* Alvaro Gabriel de la Torre Navarro. [delatorrena2016](https://github.com/delatorrena2016)
* Eduardo Padron. [fullmakeralchemist](https://github.com/fullmakeralchemist)
