from pyflink.table import (
    EnvironmentSettings, TableEnvironment, Schema, DataTypes, TableDescriptor
)

# SQL 문 없이 csv 파일 불러오기
t_env = TableEnvironment.create(
    EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

input_path = "./sample.csv"

t_env.create_temporary_table(
    "source",
    TableDescriptor.for_connector("filesystem").schema(Schema.new_builder().column("NAME", DataTypes.STRING())
                                                       .column("NUMBER", DataTypes.BIGINT())
                                                       .build()).option("path", input_path).format("csv").build()
)

src = t_env.from_path("source")
print(src.to_pandas())