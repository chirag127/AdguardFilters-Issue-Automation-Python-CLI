// ==UserScript==
// @name         fill form
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://github.com/AdguardTeam/AdguardFilters/issues/new*&template=bug_report.yml
// @icon         https://www.google.com/s2/favicons?domain=github.com
// @grant        none
// ==/UserScript==

// id="issue_form_terms_i_agree_to_follow_this_condition"
(function () {
  "use strict";

  document.getElementById(
    "issue_form_prerequisites_this_site_does_not_contains_sexually_explicit_material_otherwise_use_nsfw-specific_form_new_template_bug_report_nsfw_yml"
  ).checked = true;
  document.getElementById(
    "issue_form_prerequisites_filters_were_updated_before_reproducing_an_issue"
  ).checked = true;
  document.getElementById(
    "issue_form_prerequisites_adguard_product_version_is_up-to-date"
  ).checked = true;
  document.getElementById(
    "issue_form_prerequisites_browser_version_is_up-to-date"
  ).checked = true;
  document.getElementById(
    "issue_form_prerequisites_if_the_site_or_app_is_broken_disabling_adguard_protection_resolves_an_issue"
  ).checked = true;
  document.getElementById(
    "issue_form_terms_i_agree_to_follow_this_condition"
  ).checked = true;

  document.getElementById("issue_form_version").value = "3.6.14";
})();
