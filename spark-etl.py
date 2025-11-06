import sys
import logging
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import datetime


def create_spark_session():

    '''
    This function responsible for creating a Spark session.
    Returns:
        spark (SparkSession): Spark session object
    '''
    spark = SparkSession\
            .builder\
            .appName("SparkETL")\
            .getOrCreate()
    return spark

def transform_data(spark):
    '''
    This function responsible for transforming the data.
    Args:
        spark (SparkSession): Spark session object
    '''
    # read JSON file
    df = spark.read.option("multiline", "true").json(sys.argv[1])

    # explode the results array to get individual user records
    users_df = df.select(explode(col("results")).alias("user")).select("user.*")

    # select and rename required fields
    users=users_df.select(
        col('dob.date').alias('dob'),
        col('email'),
        col('gender'),
        col('location.city').alias('city'),
        col('location.country').alias('country'),
        col('location.coordinates').alias('coordinates'),
        col('location.postcode').alias('postcode'),
        col('location.state').alias('state'),
        col('location.street').alias('street'),
        col('location.timezone').alias('timezone'),
        concat(col('name.title'), lit('.'),col('name.first'), lit(' '), col('name.last')).alias('full_name'),
        col('phone')
    )

    users=users.withColumn('dob',to_timestamp('dob'))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(sys.argv[2], f"load_dt={timestamp}")

    try:
        users.write.parquet(output_path, mode='overwrite')
        logging.info("CSV file written successfully to %s", sys.argv[2])
    except Exception as e:
        logging.error("Error writing parquet file: %s", e)

if __name__ == "__main__": 
    if (len(sys.argv) != 3):
            logging.info("Usage: spark-etl [input-folder] [output-folder]")
            sys.exit(0)
    spark=create_spark_session()
    transform_data(spark)