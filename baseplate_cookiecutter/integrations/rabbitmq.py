from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from cookiecutter.utils import rmtree

from . import Integration


class RabbitMQIntegration(Integration):
    slug = "rabbitmq"
    name = "RabbitMQ"

    variables = {
        "dependencies": {
            "apt": [
                "rabbitmq-server",
            ],

            "python": [
                "kombu",
            ],
        },

        "imports": {
            "external": [
                "from baseplate.context.rabbitmq import queue_connection_from_config, CQLMapperContextFactory",
            ],
        },

        "puppet_modules": [
            "rabbitmq",
        ],
    }

    def prune(self, variables):
        rmtree("puppet/modules/rabbitmq")
