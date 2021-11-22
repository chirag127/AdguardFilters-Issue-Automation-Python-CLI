/* <div>
      <div class="mb-2">
        <input type="checkbox" name="issue_form[prerequisites][filters_were_updated_before_reproducing_an_issue]" id="issue_form_prerequisites_filters_were_updated_before_reproducing_an_issue" value="Filters were updated before reproducing an issue;" aria-label="Filters were updated before reproducing an issue;" required="required">

        <label required="required" class="text-normal f5 ml-1" aria-required="true" for="issue_form_prerequisites_filters_were_updated_before_reproducing_an_issue">Filters were updated before reproducing an issue;</label>
         <span class="color-fg-danger">*</span> 
      </div>
      <div class="mb-2">
        <input type="checkbox" name="issue_form[prerequisites][adguard_product_version_is_up-to-date]" id="issue_form_prerequisites_adguard_product_version_is_up-to-date" value="AdGuard product version is up-to-date;" aria-label="AdGuard product version is up-to-date;" required="required">

        <label required="required" class="text-normal f5 ml-1" aria-required="true" for="issue_form_prerequisites_adguard_product_version_is_up-to-date">AdGuard product version is up-to-date;</label>
         <span class="color-fg-danger">*</span> 
      </div>
      <div class="mb-2">
        <input type="checkbox" name="issue_form[prerequisites][browser_version_is_up-to-date]" id="issue_form_prerequisites_browser_version_is_up-to-date" value="Browser version is up-to-date;" aria-label="Browser version is up-to-date;" required="required">

        <label required="required" class="text-normal f5 ml-1" aria-required="true" for="issue_form_prerequisites_browser_version_is_up-to-date">Browser version is up-to-date;</label>
         <span class="color-fg-danger">*</span> 
      </div>
      <div class="mb-2">
        <input type="checkbox" name="issue_form[prerequisites][if_the_site_or_app_is_broken_disabling_adguard_protection_resolves_an_issue]" id="issue_form_prerequisites_if_the_site_or_app_is_broken_disabling_adguard_protection_resolves_an_issue" value="If the site or app is broken, disabling AdGuard protection resolves an issue." aria-label="If the site or app is broken, disabling AdGuard protection resolves an issue." required="required">

        <label required="required" class="text-normal f5 ml-1" aria-required="true" for="issue_form_prerequisites_if_the_site_or_app_is_broken_disabling_adguard_protection_resolves_an_issue">If the site or app is broken, disabling AdGuard protection resolves an issue.</label>
         <span class="color-fg-danger">*</span> 
      </div>
  </div> */

// ==UserScript==
// @name         fill form
// @version      0.1
// @description  fill the bug report form.
// @author       You
// @match        https://github.com/AdguardTeam/AdguardFilters/issues/new*&template=bug_report.yml
// @icon         https://www.google.com/s2/favicons?domain=github.com
// @grant        none
// ==/UserScript==

(function () {
  "use strict";

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
  document.getElementById("issue_form_version").value = "3.6.14";
  document.getElementById("issue_form_body").value = "bug report";
})();
