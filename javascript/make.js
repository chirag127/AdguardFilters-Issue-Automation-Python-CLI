// id="issue_form_prerequisites_this_site_does_not_contains_sexually_explicit_material_otherwise_use_nsfw-specific_form_new_template_bug_report_nsfw_yml"
// id="issue_form_prerequisites_filters_were_updated_before_reproduced_an_issue"
// id="issue_form_prerequisites_adguard_product_version_is_up-to-date"
// id="issue_form_prerequisites_browser_version_is_up-to-date"
// id="issue_form_prerequisites_if_the_site_or_app_is_broken_disabling_adguard_protection_resolves_an_issue"
// id="issue_title"

// ==UserScript==
// @name         Auto make the adgurad issues
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  just by click make issues.
// @author       chirag
// @match        *://*/*
// @icon         https://www.google.com/s2/favicons?domain=github.com
// @grant        none
// ==/UserScript==

(function () {
  "use strict";

  var url = window.location.href;

  var domain = window.location.hostname;

  window.open(
    "https://github.com/chirag127/test/issues/new?assignees=&template=bug_report.yml",
    "_self"
  );

  console.log(url);

  console.log(domain);

  // code to type the domain in the title
  var title = document.getElementById("issue_title");
  title.value = domain;

  document.getElementById(
    "issue_form_prerequisites_this_site_does_not_contains_sexually_explicit_material_otherwise_use_nsfw-specific_form_new_template_bug_report_nsfw_yml"
  ).checked = true;
  document.getElementById(
    "issue_form_prerequisites_filters_were_updated_before_reproduced_an_issue"
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
})();
