from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Integration(object):
    variables = {}

    def prune(self, variables):
        pass


def load_all():
    from .cassandra import CassandraIntegration
    from .events import EventsIntegration
    from .hvac import HvacIntegration
    from .memcache import MemcacheIntegration
    from .redis import RedisIntegration
    from .sqlalchemy import SQLAlchemyIntegration
    from .rabbitmq import RabbitMQIntegration

    return [
        CassandraIntegration(),
        EventsIntegration(),
        HvacIntegration(),
        MemcacheIntegration(),
        RedisIntegration(),
        SQLAlchemyIntegration(),
        RabbitMQIntegration(),
    ]
