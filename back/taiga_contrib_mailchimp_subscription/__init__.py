# Copyright (C) 2014-2016 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2016 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2016 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2016 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__version__ = (1, 10, 0)

default_app_config = "taiga_contrib_mailchimp_subscription.apps.MailChimpSubscriptionAppConfig"


from django.core import checks

@checks.register()
def check_mailchimp_installed(app_configs, **kwargs):
    try:
        import mailchimp
    except ImportError:
        return [checks.Error("mailchimp must be installed, check the requirements.txt",
                             id="newsletter_subscription.A003")]
    return []


@checks.register()
def check_mailchimp_api_key(app_configs, **kwargs):
    from django.conf import settings

    mailchimp_api_key = getattr(settings, "MAILCHIMP_API_KEY", None)
    if mailchimp_api_key is not None:
        return []

    return [checks.Error("MAILCHIMP_API_KEY must be set on settings",
                         id="newsletter_subscription.A001")]


@checks.register()
def check_imailchimp_newsletter_id(app_configs, **kwargs):
    from django.conf import settings

    newsletter_id = getattr(settings, "MAILCHIMP_NEWSLETTER_ID", None)
    if newsletter_id is not None:
        return []

    return [checks.Error("MAILCHIMP_NEWSLETTER_ID must be set on settings",
                         id="newsletter_subscription.A002")]
