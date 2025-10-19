from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

d_indicator = [{"id": 1, "name": "rashod_vody", "category_id": 1 }, {"id": 2, "name": "vyrabotka_el_en", "category_id": 2}, 
               {"id": 3, "name": "nagryzka", "category_id": 2}, {"id": 4, "name": "hour_remont", "category_id": 3}]
d_type =  [{"id": 1, "category": "norm"} ,{"id": 2, "category": "fact"} , {"id": 3, "category": "vremya"}]

df_indicator=spark.createDataFrame(d_indicator)
df_type=spark.createDataFrame(d_type)

print(df_indicator.show())
print(df_type.show())

df_indicator = df_indicator.where("category_id = 2")
df_result = df_indicator.\
    join(df_type, df_indicator.category_id == df_type.id, "inner").\
        select(df_indicator.id, df_indicator.name, df_type.category)
print("Result DataFrame:")
print(df_result.show())
