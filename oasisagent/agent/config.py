# Copyright 2014 - Rackspace Hosting
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Config options for Oasis Agent service."""


from oslo_config import cfg

AGENT_SERVICE_OPTS = [
    cfg.StrOpt('topic',
               default='oasis-agent',
               help='The queue to add agent tasks to.'),
    cfg.IntOpt('agent_life_check_timeout',
               default=4,
               help=('RPC timeout for the conductor liveness check that is '
                     'used for bay locking.')),
    # cfg.StrOpt('function_location',
    #            help='Function file location',
    #            default='/etc/oasis-agent/functions/oasis/bin')
    cfg.StrOpt('function_location',
               help='Function file location',
               default='/opt/venv_oasis/bin')
]

opt_group = cfg.OptGroup(
    name='agent',
    title='Options for the oasis-agent service')
cfg.CONF.register_group(opt_group)
cfg.CONF.register_opts(AGENT_SERVICE_OPTS, opt_group)
