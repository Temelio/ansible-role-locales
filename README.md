locales
=======

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/Temelio/ansible-role-locales.svg?branch=master)](https://travis-ci.com/Temelio/ansible-role-locales)
[![Build Status](https://travis-ci.org/Temelio/ansible-role-locales.svg?branch=develop)](https://travis-ci.com/Temelio/ansible-role-locales)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-locales/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-locales/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-locales/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-locales/)
[![Ansible Role](https://img.shields.io/ansible/role/.svg)](https://galaxy.ansible.com/Temelio/locales/)
[![GitHub tag](https://img.shields.io/github/tag/Temelio/ansible-role-locales.svg)](https://github.com/Temelio/ansible-role-locales/tags)

Install locales package.

Requirements
------------

This role requires Ansible 2.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Default role variables


    locales_to_configure :
      - name: 'en_US.UTF-8 UTF-8'
        state: 'present'

    locales_default_lang : "eb_US.UTF-8"

    locales_default_timezone : "Europe/Paris"

    locales_config_file_owner : "root"
    locales_config_file_group : "root"
    locales_config_file_mode  : "0644"


# Default Debian vars

    locales_packages :
      - locales
      - language-pack-en (except for Stretch)

    locales_config_file_dest : "/etc/default/locale"


Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: temelio.locales }

License
-------

MIT

Author Information
------------------

L Machetel (for Temelio company)
A Chaussier (for Infopen company)
