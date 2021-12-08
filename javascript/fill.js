// ==UserScript==
// @name         fill form
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://github.com/*/issues/new*template=*
// @icon         https://www.google.com/s2/favicons?domain=github.com
// @grant        none
// ==/UserScript==

// id="issue_form_terms_i_agree_to_follow_this_condition"
(function() {
  'use strict';


  var checkboxes = document.querySelectorAll('[id^="issue_form_prerequisites"]');
  for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = true;

  }
  document.getElementById("issue_form_terms_i_agree_to_follow_this_condition").checked = true;

  document.getElementById("issue_form_version").value = "4.0.64";




})();
