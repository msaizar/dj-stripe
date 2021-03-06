Settings
=========

djstripe has two settings modules:

* ``djstripe.settings``
* ``djstripe.safe_settings``

The reason for this is to accomodate how djstripe handles interaction with Django 1.5+ custom user models.
Because of how ``django.contrib.auth.get_user_model()`` works, it's possible to call that out of order and throw an ``django.core.exceptions.ImproperlyConfigured`` error, even when you are properly configured. Therefore, some settings values are available in an intermediary ``djstripe.safe_settings`` module. 

``djstripe.safe_settings`` are listed at the end of this document page.


DJSTRIPE_DEFAULT_PLAN (=None)
-----------------------------

Payment plans default. 

Possibly deprecated in favor of model based plans.

DJSTRIPE_INVOICE_FROM_EMAIL (="billing@example.com")
-------------------------------------------------------

Invoice emails come from this address.

DJSTRIPE_PLANS (={})
--------------------

Payment plans. 

Possibly deprecated in favor of model based plans.

Example:

.. code-block:: python

    DJSTRIPE_PLANS = {
        "monthly": {
            "stripe_plan_id": "pro-monthly",
            "name": "Web App Pro ($24.99/month)",
            "description": "The monthly subscription plan to WebApp",
            "price": 2499,  # $24.99
            "currency": "usd",
            "interval": "month",
            "image": "img/pro-monthly.png"
        },
        "yearly": {
            "stripe_plan_id": "pro-yearly",
            "name": "Web App Pro ($199/year)",
            "description": "The annual subscription plan to WebApp",
            "price": 19900,  # $19900
            "currency": "usd",
            "interval": "year",
            "image": "img/pro-yearly.png"
        }
    }


DJSTRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS (=())
-------------------------------------------------------

Used by ``djstripe.middleware.SubscriptionPaymentMiddleware``

Rules:

* "(app_name)" means everything from this app is exempt
* "[namespace]" means everything with this name is exempt
* "namespace:name" means this namespaced URL is exempt
* "name" means this URL is exempt
* The entire djtripe namespace is exempt

Example:

.. code-block:: python

    DJSTRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = (
        "(allauth)",  # anything in the django-allauth URLConf
        "[blogs]",  # Anything in the blogs namespace
        "products:detail",  # A ProductDetail view you want shown to non-payers
        "home",  # Site homepage
    )

TRIAL_PERIOD_FOR_RELATED_MODEL_CALLBACK (=None)
--------------------------------------------------

TODO: Document!



DJSTRIPE_WEBHOOK_URL (=r"^webhook/$")
----------------------------------------

This is where you can set *Stripe.com* to send webhook response. You can set this to what you want to prevent unnecessary hijinks from unfriendly people.

As this is embedded in the URLConf, this must be a resolvable regular expression.



DJSTRIPE_CUSTOMER_RELATED_MODEL (=User)
------------------------------

Model for ``Customer.related_model``.


DJSTRIPE_CUSTOMER_RELATED_MODEL_PLUGIN (="djstripe.plugins.default.DefaultPlugin")
--------------------------------------------------------------

Backend to customize related_model and admin.py behavior. See ``djstripe.plugins.default.DefaultPlugin``. You'll need to write one if you decide to change ``DJSTRIPE_CUSTOMER_RELATED_MODEL``.


DJSTRIPE_RELATED_MODEL_NAME_FIELD (="username")
-----------------------------------------------

``DJSTRIPE_CUSTOMER_RELATED_MODEL`` field for name used in Management and ``admin.py``


DJSTRIPE_RELATED_MODEL_BILLING_EMAIL_FIELD (="email")
-----------------------------------------------------

``DJSTRIPE_CUSTOMER_RELATED_MODEL`` field for billing email used in Stripe, receipt emails and ``admin.py``


Safe Settings
-------------------

These are values generated by djstripe to help you build your projects

djstripe.safe_settings.PLAN_CHOICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a models/forms choices formatted tuple of tuples.