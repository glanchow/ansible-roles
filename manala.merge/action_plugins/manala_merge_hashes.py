from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.six import iteritems, string_types
from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError

import re

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super(ActionModule, self).run(tmp, task_vars)

        args = {
            'hashes': self._task.args.get('hashes'),
            'prefix': self._task.args.get('prefix', ''),
            'var':    self._task.args.get('var')
        }

        if not isinstance(args['hashes'], list):
            raise AnsibleError('Invalid hashes. Expected a list, received a %s.' % type(args['hashes']))

        if not isinstance(args['prefix'], string_types):
            raise AnsibleError('Invalid prefix. Expected a string, received a %s.' % type(args['prefix']))

        if args['var'] is not None and not isinstance(args['var'], string_types):
            raise AnsibleError('Invalid var. Expected a string, received a %s.' % type(args['var']))

        hashes = []

        # Resolve hashes references
        for hash in args['hashes']:
            if isinstance(hash, string_types):
                for key, value in iteritems(task_vars):
                    if re.search('^' + hash + '$', key):
                        hashes.append(value)
            else:
                hashes.append(hash)

        print(hashes)

        facts = {}

        for hash in hashes:
            for fact_key, fact_value in iteritems(hash):
                #fact_value = templar.template(fact_value, fail_on_undefined=False)
                if (fact_key in facts) and (isinstance(facts[fact_key], list) and isinstance(fact_value, list)):
                    facts[fact_key] = facts[fact_key] + fact_value
                elif (fact_key in facts) and (isinstance(facts[fact_key], dict) and isinstance(fact_value, dict)):
                    facts[fact_key].update(fact_value)
                else:
                    facts[fact_key] = fact_value

        #if var:
        #    result['ansible_facts'] = {var: facts}
        #else:

        result['ansible_facts'] = facts

        return result





        facts = {}

        # Resolve references
        for hash in hashes:
            for key, value in iteritems(task_vars):
                if re.search('^' + hash + '$', key):
                    #print('key: ' + key)
                    #print(value)
                    if isinstance(value, dict):
                        for value_key, value_value in iteritems(value):
                            facts[prefix + value_key] = value_value


        #print(result)
        #print(task_vars)
        #print(hashes)
        #print(prefix)
        #print(var)

        if var:
            result['ansible_facts'] = {var: facts}
        else:
            result['ansible_facts'] = facts

        return result
