from pyflink.table import (
    EnvironmentSettings, TableEnvironment, DataTypes, CsvTableSource
)

settings = EnvironmentSettings.new_instance().in_batch_mode()\
                                .use_blink_planner().build()
table_env = TableEnvironment.create(settings)

field_names = ["NAME", "NUMBER"]
field_types = [DataTypes.STRING(), DataTypes.BIGINT()]

source = CsvTableSource(
    "./sample.csv",
    field_names,
    field_types,
    ignore_first_line=False # header 있을 때 True
)

table_env.register_table_source("nametable", source)
table = table_env.from_path("nametable")

print(table.to_pandas())