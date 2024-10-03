def create():
    print("Initializing Spark session ...")
    from pyspark.sql import SparkSession

    spark = (
        SparkSession.builder.appName("Data and Analytics using Apache Spark")
        .master("local")
        .getOrCreate()
    )
    sc = spark.sparkContext
    print("Initialized")

    return (spark, sc)
