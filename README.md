# Data-pipeline-using-EMR
ETL pipeline using different aws services

In this simple project, I used the following aws tools:
<ul>
  <li> <b>AWS Lambda</b>: To fetch data from an external API. </li>
  <li> <b>AWS S3</b>: To store the raw data retrieved from the API.</li>
  <li> <b>AWS EMR</b>: To transform and clean the incoming data, then load the processed data back into S3 using pyspark.</li>
  <li> <b>AWS Step function</b> : To orchestrate and schedule the execution of the Lambda function and EMR jobs.</li>
  <li> <b>AWS Glue</b>: To catalog and manage metadata for the cleaned data stored in S3. </li>
  <li> <b>AWS Athena</b>: To query the transformed data in S3 using SQL.</li>
</ul>
<img src='https://github.com/user-attachments/assets/2bd03164-19e9-4a5f-a89c-307c91485137'>

<h3>The following is the step function workflow</h3>
<img src='https://github.com/user-attachments/assets/dce2bcad-c5e9-4e29-9713-98e453529a9d'>

<h3>Structure</h3>
<ul>
  <li> <b>get_users.py </b>: python script to fetch the API data.</li>
  <li> <b>spark-etl.py </b> : The main Spark script used for transformation part.</li>
</ul>


<h3>Usage</h3>
you need to run the following command from the primary node of the EMR cluster:

` spark-submit spark-etl.py [s3-input-folder] [s3-output-folder] `

Replace [s3-input-folder] with the path to the input data directory and [s3-output-folder] with the path where you want to save the output.

<h3>Requirements</h3>
<ul>
  <li>Apache Spark</li>
  <li>AWS CLI</li>
  <li>An AWS account with necessary permissions to create and manage EMR clusters</li>
</ul>
