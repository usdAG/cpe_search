#!/usr/bin/env python3

import os
import unittest

from cpe_search import search_cpes

class TestSearches(unittest.TestCase):

    def test_search_wp_100_42_3(self):
        self.maxDiff = None
        query = 'WordPress 100.42.3'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:wordpress:wordpress:100.42.3:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:wordpress:wordpress:-:*:*:*:*:*:*:*', 0.7889609186783934)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_apache_airflow_100_42_3(self):
        self.maxDiff = None
        query = 'Airflow 100.42.3'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:apache:airflow:100.42.3:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:apache:airflow:0.1:*:*:*:*:*:*:*', 0.45357155662782184)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_apache_airflow_no_version(self):
        self.maxDiff = None
        query = 'Airflow'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:apache:airflow:*:*:*:*:*:*:*:*', -1)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_jquery_100_42_3(self):
        self.maxDiff = None
        query = 'jQuery 100.42.3'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:jquery:jquery:100.42.3:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:jquery:jquery:-:*:*:*:*:*:*:*', 0.7889609186783934), ('cpe:2.3:a:jquery:jquery:1.0.1:*:*:*:*:*:*:*', 0.6789861763163321), ('cpe:2.3:a:jquery:jquery_ui:100.42.3:rc1:*:*:*:*:*:*', -1), ('cpe:2.3:a:jquery:jquery_ui:1.10.0:rc1:*:*:*:*:*:*', 0.6461795551396173)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_jfrog_artifactory_4_29_0(self):
        self.maxDiff = None
        query = 'jfrog artifactory 4.29.0'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:jfrog:artifactory:4.29.0:-:*:*:*:-:*:*', -1), ('cpe:2.3:a:jfrog:artifactory:1.3.0:-:*:*:*:-:*:*', 0.7618540942296063), ('cpe:2.3:a:jfrog:artifactory:4.29.0:beta3:*:*:*:-:*:*', -1), ('cpe:2.3:a:jfrog:artifactory:1.3.0:beta3:*:*:*:-:*:*', 0.7039954631573018)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_dell_omsa_9_4_0_2(self):
        self.maxDiff = None
        query = 'dell omsa 9.4.0.2'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:dell:openmanage_server_administrator:9.4.0.2:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:dell:openmanage_server_administrator:5.2.0:*:*:*:*:*:*:*', 0.9356286465015572), ('cpe:2.3:a:dell:openmanage_server_administrator_installer:9.4.0.2:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:dell:openmanage_server_administrator_installer:1.0.0:*:*:*:*:*:*:*', 0.8355902246901327), ('cpe:2.3:a:dell:openmanage_server_administrator_lite:9.4.0.2:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:dell:openmanage_server_administrator_lite:5.4.1:*:*:*:*:*:*:*', 0.8355902246901327)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_citrix_adc_13_1_42_47(self):
        self.maxDiff = None
        query = 'citrix adc 13.1-42.47'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:citrix:application_delivery_controller:13.1:42.47:*:*:-:*:*:*', -1), ('cpe:2.3:a:citrix:application_delivery_controller:13.1-42.47:*:*:*:-:*:*:*', -1), ('cpe:2.3:a:citrix:application_delivery_controller:13.1:*:*:*:-:*:*:*', 0.9443356111798746), ('cpe:2.3:h:citrix:application_delivery_controller:13.1:*:*:*:*:*:*:*', -1), ('cpe:2.3:h:citrix:application_delivery_controller:13.1:42.47:*:*:*:*:*:*', -1), ('cpe:2.3:h:citrix:application_delivery_controller:13.1-42.47:*:*:*:*:*:*:*', -1), ('cpe:2.3:h:citrix:application_delivery_controller:-:*:*:*:*:*:*:*', 0.9195900759823715)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_citrix_adc_no_version(self):
        self.maxDiff = None
        query = 'citrix adc'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes =  [('cpe:2.3:h:citrix:application_delivery_controller:-:*:*:*:*:*:*:*', 0.9640085266327638), ('cpe:2.3:a:citrix:application_delivery_controller:*:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:citrix:application_delivery_controller:12.1:*:*:*:-:*:*:*', 0.9003316339465728), ('cpe:2.3:o:citrix:application_delivery_controller_firmware:*:*:*:*:*:*:*:*', -1), ('cpe:2.3:o:citrix:application_delivery_controller_firmware:10.1:*:*:*:*:*:*:*', 0.8609356974951642)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_openssh_83_p4(self):
        self.maxDiff = None
        query = 'openssh 8.3 p4'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes =  [('cpe:2.3:a:openssh:openssh:8.3:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:openssh:openssh:8.3:p4:*:*:*:*:*:*', -1), ('cpe:2.3:a:openssh:openssh:8.3_p4:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:openssh:openssh:-:*:*:*:*:*:*:*', 0.74544047460131), ('cpe:2.3:a:openssh:openssh:9.1:*:*:*:*:*:*:*', 0.7258247616391765), ('cpe:2.3:a:openbsd:openssh:8.3:p4:*:*:*:*:*:*', -1), ('cpe:2.3:a:openbsd:openssh:8.3_p4:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:openbsd:openssh:8.3:*:*:*:*:*:*:*', 0.7032799679449337)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_datatables_1_9_4(self):
        self.maxDiff = None
        query = 'datatables 1.9.4'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:datatables:datatables.net:1.9.4:-:*:*:*:node.js:*:*', -1), ('cpe:2.3:a:datatables:datatables.net:1.10.0:-:*:*:*:node.js:*:*', 0.43397267978578885), ('cpe:2.3:a:datatables:datatables.net:1.9.4:beta1:*:*:*:node.js:*:*', -1), ('cpe:2.3:a:datatables:datatables.net:1.10.0:beta1:*:*:*:node.js:*:*', 0.41674310186320396), ('cpe:2.3:a:sprymedia:datatables:1.9.4:*:*:*:*:jquery:*:*', -1), ('cpe:2.3:a:sprymedia:datatables:1.9.2:*:*:*:*:jquery:*:*', 0.40060727459547485)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])

    def test_search_microsoft_sql_server_2019_15_00_2000_00_RTM(self):
        self.maxDiff = None
        query = 'microsoft sql_server 2019 15.00.2000.00;RTM'
        result = search_cpes(query)['pot_cpes']
        expected_related_cpes = [('cpe:2.3:a:microsoft:sql_server:2019:15.00.2000.00:*:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_server:2019:15.00.2000.00:RTM:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_server:2019_15.00.2000.00_RTM:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_server:2019:*:*:*:*:*:*:*', 0.7523479560247002), ('cpe:2.3:a:microsoft:sql_server:-:*:*:*:*:*:*:*', 0.6899566027601122), ('cpe:2.3:a:microsoft:sql_srv:2019:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_srv:2019:15.00.2000.00:*:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_srv:2019:15.00.2000.00:RTM:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_srv:2019_15.00.2000.00_RTM:*:*:*:*:*:*:*', -1), ('cpe:2.3:a:microsoft:sql_srv:-:*:*:*:*:*:*:*', 0.6899566027601122)]
        for i, (expected_related_cpe, match_score) in enumerate(expected_related_cpes):
            self.assertEqual(expected_related_cpe, result[i][0])
            self.assertAlmostEqual(match_score, result[i][1])


if __name__ == '__main__':
    os.environ['IS_CPE_SEARCH_TEST'] = 'true'
    unittest.main()
