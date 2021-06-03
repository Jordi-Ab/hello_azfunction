import logging
import json
from .src.hello import Hello

import azure.functions as func
from pyspark.sql import SparkSession
#import pyspark.sql.functions as F
#from pyspark.sql.functions import countDistinct
#from pyspark.sql.functions import count


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    name = req_body.get('name')

    spark = SparkSession.builder.appName('abc').getOrCreate()

    say_hello = Hello(name)
    response = {
        'name': say_hello(),
        'message':'some message',
        'status': 'success'
    }

    return func.HttpResponse(
        json.dumps(response),
        status_code=200
    )
