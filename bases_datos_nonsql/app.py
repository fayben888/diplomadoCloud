import boto3

#pip3.9 install boto3. -> instalar libreria para conectar 

dynamobd = boto3.resource('dynamodb', region_name = 'us-east-1')
tabla = dynamobd.Table('tabla-daniel-henao')

response = tabla.get_item(Key = {'id': '2'}) #leer solo un elemento

print(response['Item'])


# Definir el elemento que deseas insertar
item_to_insert = {
    'id': '3',
    'nombre': 'Daniel',
    'edad': 30,
    # Otros atributos según la estructura de tu tabla
}

# Insertar el elemento en la tabla
tabla.put_item(Item=item_to_insert)

response = tabla.scan() #leer todos los elemento

print(response['Items'])

#response = tabla.delete_item(Key = {'id': '3'}) #eliminar solo un elemento

#response = tabla.scan() #leer todos los elemento

#print(response['Items'])

#ACTUALIZAR ELEMENTO

response = tabla.update_item(

    Key={

        'id': '3'  

    },

    UpdateExpression='SET edad = :val1',  # Expresión de actualización

    ExpressionAttributeValues={

        ':val1': 34  # Nuevo valor para atributo2

    }

)
response = tabla.scan() #leer todos los elemento

print(response['Items'])