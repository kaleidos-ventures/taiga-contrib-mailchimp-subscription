from settings.testing import *

if "taiga_contrib_mailchimp_subscription" not in INSTALLED_APPS:
    INSTALLED_APPS += ["taiga_contrib_mailchimp_subscription"]
MAILCHIMP_API_KEY = "X-X"
MAILCHIMP_NEWSLETTER_ID = "Y"
