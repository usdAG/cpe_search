#!/usr/bin/env python3

import unittest
from cpe_search import search_cpes

class TestSearches(unittest.TestCase):

    def test_search_wp_572(self):
        result = str(search_cpes(queries='WordPress 5.7.2'))
        self.assertEqual(result, "{'WordPress 5.7.2': [('cpe:2.3:a:wordpress:wordpress:5.7.2:*:*:*:*:*:*:*', 0.9805804786431419), ('cpe:2.3:a:wordpress:wordpress:-:*:*:*:*:*:*:*', 0.7071067811865475), ('cpe:2.3:a:adenion:blog2social:5.7.2:*:*:*:*:wordpress:*:*', 0.6859944446591075)]}")
    
    def test_search_apache_2425(self):
        result = str(search_cpes(queries='Apache 2.4.25'))
        self.assertEqual(result, "{'Apache 2.4.25': [('cpe:2.3:a:apache:http_server:2.4.25:*:*:*:*:*:*:*', 0.737210014936463), ('cpe:2.3:a:apache:apache-airflow-providers-apache-hive:-:*:*:*:*:*:*:*', 0.600000153741923), ('cpe:2.3:a:apache:apache-airflow-providers-apache-pig:-:*:*:*:*:*:*:*', 0.600000153741923)]}")
    
    def test_search_proftpd_133c(self):
        result = str(search_cpes(queries='Proftpd 1.3.3c'))
        self.assertEqual(result, "{'Proftpd 1.3.3c': [('cpe:2.3:a:proftpd:proftpd:1.3.3:c:*:*:*:*:*:*', 0.8333337218752717), ('cpe:2.3:a:proftpd:proftpd:1.3.3:*:*:*:*:*:*:*', 0.8006406081365984), ('cpe:2.3:a:proftpd:proftpd:1.3.2:c:*:*:*:*:*:*', 0.6666669775002174)]}")

    def test_search_thingsboard_341(self):
        result = str(search_cpes(queries='Thingsboard 3.4.1'))
        self.assertEqual(result, "{'Thingsboard 3.4.1': [('cpe:2.3:a:thingsboard:thingsboard:3.4.1:*:*:*:*:*:*:*', 0.9805804786431419), ('cpe:2.3:a:thingsboard:thingsboard:1.0:*:*:*:*:*:*:*', 0.6324555256696553), ('cpe:2.3:a:emberjs:ember.js:3.4.1:*:*:*:*:*:*:*', 0.4714045207910316)]}")

    def test_search_redis_323(self):
        result = str(search_cpes(queries='Redis 3.2.3'))
        self.assertEqual(result, "{'Redis 3.2.3': [('cpe:2.3:a:redis:redis:3.2.3:*:*:*:*:*:*:*', 0.9805804786431419), ('cpe:2.3:a:redislabs:redis:3.2.3:*:*:*:*:*:*:*', 0.9128707750749131), ('cpe:2.3:a:redis:redis:-:*:*:*:*:*:*:*', 0.7071067811865475)]}")

    def test_search_piwik_045(self):
        result = str(search_cpes(queries='Piwik 0.4.5'))
        self.assertEqual(result, "{'Piwik 0.4.5': [('cpe:2.3:a:joinbookwyrm:bookwyrm:0.4.5:*:*:*:*:*:*:*', 0.4714045207910316), ('cpe:2.3:a:jubat:jubatus:0.4.5:*:*:*:*:*:*:*', 0.4714045207910316), ('cpe:2.3:a:kavitareader:kavita:0.4.5:*:*:*:*:*:*:*', 0.4714045207910316)]}")

    def test_search_vmware_spring_framework_5326(self):
        result = str(search_cpes(queries='VMWare Spring Framework 5.3.26'))
        self.assertEqual(result,"{'VMWare Spring Framework 5.3.26': [('cpe:2.3:a:vmware:spring_framework:3.0.0:-:*:*:*:*:*:*', 0.75), ('cpe:2.3:a:laravel:framework:5.3.26:*:*:*:*:*:*:*', 0.5773500383793437), ('cpe:2.3:a:vmware:spring_security:-:*:*:*:*:*:*:*', 0.5773500383793437)]}")

    def test_search_zulip_server_48(self):
        result = str(search_cpes(queries='Zulip server 4.8'))
        self.assertEqual(result, "{'Zulip server 4.8': [('cpe:2.3:a:zulip:zulip:4.8:*:*:*:*:*:*:*', 0.8006406081365984), ('cpe:2.3:a:zulip:zulip_server:1.1.5:*:*:*:*:*:*:*', 0.7001398086317259), ('cpe:2.3:a:zulip:zulip_server:1.2.0:-:*:*:*:*:*:*', 0.7001398086317259)]}")

    def test_search_electron_1317(self):
        result = str(search_cpes(queries='Electron 13.1.7'))
        self.assertEqual(result, "{'Electron 13.1.7': [('cpe:2.3:a:electronjs:electron:13.1.7:*:*:*:*:*:*:*', 0.8164962545126949), ('cpe:2.3:a:markdown-electron_project:markdown-electron:-:*:*:*:*:*:*:*', 0.4714045207910316), ('cpe:2.3:a:diagrams:drawio:13.1.7:*:*:*:*:*:*:*', 0.44721383028334494)]}")

if __name__ == '__main__':
    unittest.main()