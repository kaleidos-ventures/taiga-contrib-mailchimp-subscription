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

from django.apps import AppConfig


def connect_signals():
    from taiga.auth.signals import user_registered as user_registered_signal
    from taiga.users.signals import user_cancel_account as user_cancel_account_signal
    from . import signal_handlers as handlers
    user_registered_signal.connect(handlers.subscribe_to_newsletter,
                                   dispatch_uid="subscribe_registered_user_to_newsletter")
    user_cancel_account_signal.connect(handlers.unsubscribe_from_newsletter,
                                       dispatch_uid="unsubscribe_user_from_newsletter")


def disconnect_signals():
    from taiga.auth.signals import user_registered as user_registered_signal
    from taiga.users.signals import user_cancel_account as user_cancel_account_signal
    user_registered_signal.disconnect(dispatch_uid="subscribe_registered_user_to_newsletter")
    user_cancel_account_signal.disconnect(dispatch_uid="unsubscribe_user_from_newsletter")


class MailChimpSubscriptionAppConfig(AppConfig):
    name = "taiga_contrib_mailchimp_subscription"
    verbose_name = "MailChimp Subscription App Config"

    def ready(self):
        connect_signals()
