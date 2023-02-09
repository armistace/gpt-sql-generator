# Intalgo

Intalgo (Integration Algorithms) is chat-gpt enable Data Modelling platform. 

It leverages [DBT](https://github.com/dbt-labs/dbt-core) to provide a platform agnostic modelling backend and links it to the power of chat gpt to provide a human language input that can be converted to sql

## Quickstart
Start the docker service and then execute compose_up_cmd.sh
```
systemctl start docker
./compose_up_cmd.sh
```

## What it currently Does
Currently it just has two endpoint /run and /test that will test some of the DBT stuff

## The Core Architecture

There are two ways to instantiate a connection. The first is to manually provide a [DBT profile](https://docs.getdbt.com/docs/get-started/connection-profiles) by adding it to the config directory of this repo when you pull and build the [DBT docker](https://github.com/dbt-labs/dbt-core/tree/main/docker)

If the app hasn't received this file on first start it will trigger the "First Start" page which will ask a series of questions and use the answers to create one for you. This process can be quite time consuming but requires no knowledge of DBT (It does require knowledge of how to connect to your source data.)

Once the connection between intalgo and the source data is established via dbt it will then ask for things like the name you wish to give the project, how you would like to materialise the models you create whether you would like to store the dbt project on disc, on a network drive, or in source control (if you choose source bontrol you will need to provide the remote url and any login information)

All these options are not set in stone and can be changed at any time.

Once this is done we need to train chat gpt on the source data. 

To do this we leverage [Datahub](https://github.com/datahub-project/datahub) (TBD.. should I create my own schema inferer?) by converting the DBT profile into a [datahub integration recipe](https://datahubproject.io/docs/metadata-ingestion/)  and scraping the source system for it's metadata. It is important to note that this will be a one time thing and need to be retriggered if the schema changes. There will be a datahub ui available that allows for searching of the schema.  We then generate a [DBT sources yaml](https://docs.getdbt.com/docs/build/sources) that we point chat-gpt to and allow it to learn the schema.

- This will leverage the ability of datahub to identify primary and foreign keys in some systems as well providing all the information it can garner for chat gpt to learn about the schema or metadata of our data to build the sql

With this source yaml configured and chat gpt now having a file to interpret our question against we are now presented with the Question interface. 

This question interface is our direct link between chat-gpt and DBT.

You have two options, analysis, and model. The difference between these is quite simple. questions asked in analysis will generate a question under the [DBT analysis concept](https://docs.getdbt.com/docs/build/analyses) and models will generate query using the [models concept in DBT](https://docs.getdbt.com/docs/build/sql-models) The core difference is analysis are not materialised in dbt run whereas models are. These models are stored in dbt and can be seen by there name in the flask app that is autogenerated (it can also be renamed to something more relevant if required) this allows you to not only ask question ofyour data but ask questions of your questions. 

When you have finished creating your dbt project you can configure a deployment method for the etl pipelines you have created.

### Supported orchestration platforms

1. [Apache Airflow](https://airflow.apache.org)
2. [Databricks](https://www.databricks.com)
3. [Dagster](https://dagster.io)
4. (???) Any other platform that supports DBT

[Flask](https://flask.palletsprojects.com/en/2.2.x/) is used to provide glue between the frontend and dbt and chat gpt as well as performing any backend git work to ensure the dbt project is stored and deployable


