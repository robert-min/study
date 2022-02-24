import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
t_env = StreamTableEnvironment.create(env, environment_settings=settings)

# apache kafka SQL Connector
kafka_jar_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "./",
    "flink-sql-connector-kafka_2.11-1.14.3.jar"
)
t_env.get_config().get_configuration().set_string(
    "pipeline.jars", f"file://{kafka_jar_path}"
)

source_query = f"""
CREATE TABLE source(
    NAME STRING,
    NUMBER INT
) WITH (
    'connector' = 'kafka',
    'topic' = 'flink-kafka',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'test-group',
    'format' = 'csv',
    'scan.startup.mode' = 'earliest-offset'
)
"""

t_env.execute_sql(source_query)

sink_query = """
CREATE TABLE blackhole (
    NAME STRING,
    NUMBER INT
) WITH (
    'connector' = 'blackhole'
)
"""

t_env.execute_sql(sink_query)
t_env.from_path("source").insert_into("blackhole")
t_env.execute("flink_kafka_consumer_sql")
