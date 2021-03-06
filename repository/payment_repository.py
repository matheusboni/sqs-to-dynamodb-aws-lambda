import uuid

import boto3

from model.environment import Environment as envs


class PaymentRepository:
    def __init__(self):
        self.__dynamo = boto3.resource("dynamodb", region_name=envs.AWS_REGION)
        self.__table = self.__dynamo.Table(envs.TABLE)

    def save(self, payment: dict):
        payment['id'] = str(uuid.uuid4())
        self.__table.put_item(Item=payment)
