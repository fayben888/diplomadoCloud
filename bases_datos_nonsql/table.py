import boto3

# Conectar con DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

#CREAR UNA TABLA


# # Definir el esquema de la tabla
# table_name = 'tabla-daniel-henao-2'
# key_schema = [
#     {
#         'AttributeName': 'id',
#         'KeyType': 'HASH'  # Clave de partición
#     }
# ]
# attribute_definitions = [
#     {
#         'AttributeName': 'id',
#         'AttributeType': 'S'  # Tipo de dato: String (puedes usar 'N' para números)
#     }
# ]
# provisioned_throughput = {
#     'ReadCapacityUnits': 5,    # Capacidad de lectura por segundo
#     'WriteCapacityUnits': 5    # Capacidad de escritura por segundo
# }

# # Crear la tabla
# response = dynamodb.create_table(
#     TableName=table_name,
#     KeySchema=key_schema,
#     AttributeDefinitions=attribute_definitions,
#     ProvisionedThroughput=provisioned_throughput
# )

# # Imprimir respuesta
# print(f'Respuesta de creación de tabla: {response}')

#ELIMINAR TABLA

# Nombre de la tabla a eliminar
table_name = 'tabla-daniel-henao-2'

# Eliminar la tabla
response = dynamodb.delete_table(
    TableName=table_name
)
