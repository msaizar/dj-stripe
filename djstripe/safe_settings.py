from __future__ import unicode_literals

try:
    # For Python 2.7 and Python 3.x users
    from collections import OrderedDict
except ImportError:
    # For Python 2.6 users
    from ordereddict import OrderedDict

from django.conf import settings


STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
INVOICE_FROM_EMAIL = getattr(
    settings,
    "DJSTRIPE_INVOICE_FROM_EMAIL",
    "billing@example.com"
)
PAYMENTS_PLANS = getattr(settings, "DJSTRIPE_PLANS", {})
PAYMENT_PLANS = OrderedDict(sorted(PAYMENTS_PLANS.items(), key=lambda t: t[1]['price']))

PLAN_CHOICES = [
    (plan, PAYMENT_PLANS[plan].get("name", plan))
    for plan in PAYMENT_PLANS
]
PASSWORD_INPUT_RENDER_VALUE = getattr(
    settings, 'DJSTRIPE_PASSWORD_INPUT_RENDER_VALUE', False)
PASSWORD_MIN_LENGTH = getattr(
    settings, 'DJSTRIPE_PASSWORD_MIN_LENGTH', 6)
DJSTRIPE_CUSTOMER_RELATED_MODEL_PLUGIN = getattr(settings, "DJSTRIPE_CUSTOMER_RELATED_MODEL_PLUGIN", "djstripe.plugins.default.DefaultPlugin")
DJSTRIPE_RELATED_MODEL_NAME_FIELD = getattr(settings, "DJSTRIPE_RELATED_MODEL_NAME_FIELD", "username")
DJSTRIPE_RELATED_MODEL_BILLING_EMAIL_FIELD = getattr(settings, "DJSTRIPE_RELATED_MODEL_BILLING_EMAIL_FIELD", "email")