# Ansible Role: Merge [![Build Status](https://travis-ci.org/manala/ansible-role-merge.svg?branch=master)](https://travis-ci.org/manala/ansible-role-merge)

:exclamation: [Report issues](https://github.com/manala/ansible-roles/issues) and [send Pull Requests](https://github.com/manala/ansible-roles/pulls) in the [main Ansible Role repository](https://github.com/manala/ansible-roles) :exclamation:

This role will deal with the merging of ansible variables.

It's part of the [Manala Ansible stack](http://www.manala.io) but can be used as a stand alone component.

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2+

Using ansible galaxy cli:

```bash
ansible-galaxy install manala.merge
```

Using ansible galaxy requirements file:

```yaml
- src: manala.merge
```

## Role Handlers

None.

## Role Variables

### Definition

| Name                  | Default | Type  | Description |
| --------------------- | ------- | ----- | ----------- |
| `manala_merge_hashes` | []      | Array | Hashes      |

### Examples

Merge hashes and store results elements as facts

```yaml
- hosts: all
  vars:
    foo: bar
    hash_1: # First hash
      foo: foo
      bar: qux
    hash_2: # Second hash
      bar: bar
      baz: baz
    hash_3: # Third hash
      qux: qux
    manala_merge_hashes:
      - hashes:
          - hash_1 # First hash name
          - hash_2 # Second hash name
          - hash_3 # Third hash name
  roles:
    - manala.merge
  tasks:
    - debug:
        var: foo # -> foo
    - debug:
        var: bar # -> bar
    - debug:
        var: baz # -> baz
    - debug:
        var: qux # -> qux
```

# Licence

MIT

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
