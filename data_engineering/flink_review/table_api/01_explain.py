from pyflink.table import EnvironmentSettings, TableEnvironment

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

col_names = ["id", "name"]
data = [
    (1, "kim"),
    (2, "park"),
    (3, "keon"),
    (4, "yoon"),
]

t1 = t_env.from_elements(data, col_names)
t2 = t_env.from_elements(data, col_names)

table = t1.where(t1.name.like("k%")).union_all(t2)
print(table.to_pandas())
print(table.explain())
