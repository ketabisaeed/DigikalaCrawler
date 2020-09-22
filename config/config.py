"""
Author: Saeed Ketabi
Email: saeed.ketabi@gmail.com
Telegram: @Sbooki / @Sboooki
http://Boooki.ir

2020 september 21

*********************************************************
*********************************************************
                THIS IS TEMPLATE FILE
*********************************************************
*********************************************************

"""



class Config:
    RABBITMQ = {
        'digikala_comments': {
            'transport': 'amqp',
            'host': '',
            'port': 5672,
            'username': '',
            'password': '',
            'exchange_type': '',
            'exchange_name': '',
            'queue_name': '',
            'routing_key': ''
        },
        'digikala_products': {
            'transport': 'amqp',
            'host': '',
            'port': 5672,
            'username': '',
            'password': '',
            'exchange_type': '',
            'exchange_name': '',
            'queue_name': '',
            'routing_key': ''
        },
    }

    MONGODB = {

    }

    ELASTIC = {

    }

    CRAWLERS = {
        'digikala_comments':{
            'output': 'CSV'
        }
    }