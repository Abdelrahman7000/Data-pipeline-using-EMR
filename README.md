# Data-pipeline-using-EMR
ETL pipeline using different aws services

In this simple project, I used the following aws tools:
<ul>
  <li> <b>AWS Lambda</b>: To fetch data from an external API. </li>
  <li> <b>AWS S3</b>: To store the raw data retrieved from the API.</li>
  <li> <b>AWS EMR</b>: To transform and clean the incoming data, then load the processed data back into S3 using pyspark.</li>
  <li> <b>AWS Step functions</b> : To orchestrate and schedule the execution of the Lambda function and EMR jobs.</li>
  <li> <b>AWS Glue</b>: To catalog and manage metadata for the cleaned data stored in S3. </li>
  <li> <b>AWS Athena</b>: To query the transformed data in S3 using SQL.</li>
</ul>
<img src='https://github.com/user-attachments/assets/2bd03164-19e9-4a5f-a89c-307c91485137'>

<h2>The following is the step function workflow</h2>
<img src='https://github.com/user-attachments/assets/dce2bcad-c5e9-4e29-9713-98e453529a9d'>
