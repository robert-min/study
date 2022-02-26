from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

ds = env.from_collection(["kim", "park", "keon", "yoon"], Types.STRING())
name_table = t_env.from_data_stream(ds)

t_env.create_temporary_view("firstname", name_table)

res_table = t_env.sql_query("SELECT * FROM firstname WHERE f0 like 'k%'")

res_ds = t_env.to_data_stream(res_table)

res_ds.print()
env.execute()