Taiga Contrib MailChimp Subscription
====================================

Taiga plugin to subscribe and unsubscribe users to the newsletter in [MailChimp]("http://mailchimp.com/").


Installation
------------

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-mailchimp-subscription` with:

```bash
  pip install -e "git+https://github.com/taigaio/taiga-contrib-mailchimp-subscription.git@stable#egg=taiga-contrib-mailchimp-subscription&subdirectory=back"
```

Then modify your settings/local.py and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["taiga_contrib_mailchimp_subscription"]
```

Then run the migrations to generate the new need table:


### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-mailchimp-subscription` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/taigaio/taiga-contrib-mailchimp-subscription/branches/stable/front/dist" "mailchimp-subscription"
```

Include in your dist/conf.json in the contribPlugins list the value `"/plugins/mailchimp-subscription/mailchimp-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailchimp-subscription/mailchimp-subscription.json"
    ]
...
```
