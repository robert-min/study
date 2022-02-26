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

t_env.execute_sql("""
CREATE TABLE print_sink1 (
    id BIGINT,
    name VARCHAR
) WITH (
    'connector' = 'print'
)
""")

t_env.execute_sql("""
CREATE TABLE print_sink2 (
    id BIGINT,
    name VARCHAR
) WITH (
    'connector' = 'print'
)
""")

statement_set = t_env.create_statement_set()
statement_set.add_insert("print_sink1", t1.where(t1.name.like("k%")))
statement_set.add_insert("print_sink2", t2)

statement_set.execute().wait()
print(statement_set.explain())