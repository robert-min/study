from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes

settings = EnvironmentSettings.new_instance().in_batch_mode()\
                                .use_blink_planner().build()
table_env = TableEnvironment.create(settings)

sample_data = [
  ("KIM", 1),
  ("LEE", 2),
  ("PARK", 3),
  ("YOON", 4),
]

# src1 : col 명, schema 등을 지정해주지 않아 자동으로 지정
src1 = table_env.from_elements(sample_data)
print(src1)
src1.print_schema()
print(src1.to_pandas())

# src2: col 명 지정
col_names = ["NAME", "NUMBER"]
src2 = table_env.from_elements(sample_data, col_names)
print(src2.to_pandas())

# src3: schema col명 모두 지정
schema = DataTypes.ROW([
    DataTypes.FIELD("NAME", DataTypes.STRING()),
    DataTypes.FIELD("NUMBER", DataTypes.BIGINT())
])
src3 = table_env.from_elements(sample_data, schema)
src3.print_schema()
print(src3.to_pandas())
