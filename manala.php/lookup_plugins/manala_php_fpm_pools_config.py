from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def format_row(self, key, value, type):
        result = ''
        if type == 'env':
            if not isinstance(value, dict):
                raise AnsibleError('Expected a dict for key "env" in manala_php_fpm_pools config ')
            for envKey in sorted(value):
                envValue = value.get(envKey)
                if not isinstance(envValue, (basestring, int, float)) or isinstance(envValue, bool):
                    raise AnsibleError("Expected a string, an integer or a float for key \"%s\" in manala_php_fpm_pools config env" % envKey)
                result += "env[%s] = \"%s\"\n" % (envKey, envValue)

        return result

    def run(self, terms, variables=None, **kwargs):

        wantrow        = kwargs.pop('wantrow', None)
        wantrowtype    = kwargs.pop('wantrowtype', None)
        wantrowdefault = kwargs.pop('wantrowdefault', None)

        config = self._flatten(terms[0])

        for row in config:
            for key, value in row.iteritems():
                if key == wantrow:
                    return self.format_row(key, value, wantrowtype)

        if wantrowdefault:
            return wantrowdefault
