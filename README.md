Role Name
=========

[![CircleCI](https://circleci.com/gh/verygood-ops/verygood.hardening.svg?style=svg)](https://circleci.com/gh/verygood-ops/verygood.hardening)

Makes Ubuntu hard

Role Variables
--------------

- `{{ vg_hardening_shell_timeout_seconds }}` - number of seconds before an idle shell is terminated


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: verygood.hardening, vg_hardening_shell_timeout_seconds: 300 }

License
-------

BSD
