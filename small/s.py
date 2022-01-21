url = "https://reports.adguard.com/new_issue.html?product_type=Win&product_version=7.9%20nightly%204&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DwlWyey1hGr4&referrer=&user_agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.71%20Safari%2F537.36&filters=101.118.122.123.227.11.14.16.17.1.224.2.3.4.5.6.7.9&userscripts=https%3A%2F%2Fuserscripts.adtidy.org%2Fbeta%2Fadguard-extra%2F1.0%2Fadguard-extra.user.js%2Chttps%3A%2F%2Fuserscripts.adtidy.org%2Fbeta%2Fpopup-blocker%2F2.5%2Fpopupblocker.user.js&win.wfp=true&stealth.enabled=true&stealth.hide_search_queries=true&stealth.DNT=true&stealth.x_client=true&stealth.third_party_cookies=180&stealth.disable_third_party_cache=false&stealth.webrtc=false&stealth.push=false&stealth.location=false&stealth.disable_windows_telemetry=true&stealth.turn_off_advertising_id=true&stealth.disable_windows_defender=false&stealth.disable_wap_push_message_routing_service=false&stealth.flash=false&stealth.java=false&stealth.strip_url=true&stealth.block_third_party_auth=false&dns.enabled=true&dns.timeout=5000&dns.fallback_mode=System&dns.custom_fallback=&dns.servers=https%3A%2F%2Fdns.adguard.com%2Fdns-query&dns.filters_enabled=true&dns.filters=https%3A%2F%2Ffilters.adtidy.org%2Fwindows%2Ffilters%2F15.txt%2CUser%20rules&parental_control.enabled=true&parental_control.sensitivity=EarlyChildhood&parental_control.safe_search=true&parental_control.block_exe=false&browsing_security.enabled=true&browsing_security.statistics_enabled=false"

# all parameters in the url are in the form of "key=value"
# we need to split the url into a list of strings
# and then split each string into a list of key and value


from urllib.parse import urlparse
from urllib.parse import parse_qs


parsed_url = urlparse(url)
captured_value = parse_qs(parsed_url.query)


# for key, value in captured_value.items():


for key, value in captured_value.items():

    # join teh value list into a string
    value = ",".join(value)
    # replace the . with a _ in key
    # key = key.replace(".", "_")

    print(f"{key} = \"{value}\"")
