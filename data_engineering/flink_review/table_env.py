from pyflink.table import EnvironmentSettings, TableEnvironment, StreamTableEnvironment
from pyflink.datastream import StreamExecutionEnvironment

# batch Environment
batch_settings = EnvironmentSettings.new_instance().in_batch_mode()\
                                    .use_blink_planner().build()
batch_table_env = TableEnvironment.create(batch_settings)

# stream Environment
stream_settings = EnvironmentSettings.new_instance().in_streaming_mode()\
                                    .use_blink_planner().build()
stream_table_env = TableEnvironment.create(stream_settings)

# datastream enviroment
datastream_env = StreamExecutionEnvironment.get_execution_environment()
table_env = StreamTableEnvironment.create(datastream_env)