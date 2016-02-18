Taiga Contrib MailChimp Subscription
====================================

Taiga plugin to subscribe and unsubscribe users to the newsletter in [MailChimp]("http://mailchimp.com/").


Installation
------------
### Production env

#### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-mailchimp-subscription` with:

```bash
  pip install -e "git+https://github.com/taigaio/taiga-contrib-mailchimp-subscription.git@stable#egg=taiga-contrib-mailchimp-subscription&subdirectory=back"
```

Then modify in `taiga-back` your `settings/local.py` and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["taiga_contrib_mailchimp_subscription"]
```


#### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-mailchimp-subscription` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/taigaio/taiga-contrib-mailchimp-subscription/branches/stable/front/dist" "mailchimp-subscription"
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailchimp-subscription/mailchimp-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailchimp-subscription/mailchimp-subscription.json"
    ]
...
```

### Dev env

#### Taiga Back

Clone the repo and

```bash
  cd taiga-contrib-mailchimp-subscription/back
  workon taiga
  pip install -e .
```

Then modify in `taiga-back` your `settings/local.py` and include this line:

```python
  MAILCHIMP_NEWSLETTER_ID = "my-newsletter"
  MAILCHIMP_API_KEY = "XXXXXXXXXXXXXXXXX"

  INSTALLED_APPS += ["taiga_contrib_mailchimp_subscription"]
```

#### Taiga Front

After clone the repo link `dist` in `taiga-front` plugins directory:

```bash
  cd taiga-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../taiga-contrib-mailchimp-subscription/front/dist mailchimp-subscription
```

Include in your `dist/conf.json` in the `contribPlugins` list the value `"/plugins/mailchimp-subscription/mailchimp-subscription.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/mailchimp-subscription/mailchimp-subscription.json"
    ]
...
```

In the plugin source dir `taiga-contrib-mailchimp-subscription` run

```bash
npm install
```
and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.


Tests
-----
```bash
  cd taiga-back
  workon taiga
  py.test ../taiga-contrib-mailchimp-subscription/back/taiga_contrib_mailchimp_subscription_tests
```
