# Wikidata Lexeme Forms

[This tool](https://tools.wmflabs.org/lexeme-forms/) lets users create Wikidata lexemes with pre-populated forms,
such as the declensions of a noun or the conjugations of a verb.

## Toolforge setup

On Wikimedia Toolforge, this tool runs under the `lexeme-forms` tool name.
Source code resides in `~/www/python/src/`,
a virtual environment is set up in `~/www/python/venv/`,
logs end up in `~/uwsgi.log`.

If the web service is not running for some reason, run the following command:
```
webservice --backend=kubernetes python start
```
If it’s acting up, try the same command with `restart` instead of `start`.

To update the service, run the following commands after becoming the tool account:
```
source ~/www/python/venv/bin/activate
cd ~/www/python/src
git fetch
git diff @ @{u} # inspect changes
git merge --ff-only @{u}
pip3 install -r requirements.txt
webservice --backend=kubernetes python restart
```
However, the `venv` and `pip3` parts are only necessary when new packages are required –
if only `templates.py` and/or `translations.py` were updated, you can skip those.

## Local development setup

You can also run the tool locally, which is much more convenient for development
(for example, Flask will automatically reload the application any time you save a file).
Note that a local setup will not actually perform edits unless you create a `config.yaml` file.

```
git clone https://phabricator.wikimedia.org/source/tool-lexeme-forms.git
cd tool-lexeme-forms
pip3 install -r requirements.txt
FLASK_APP=app.py FLASK_ENV=development flask run
```

If you want, you can do this inside some virtualenv too.

## Contributing

Yay contributions! <3

### Templates

To propose new templates for the tool,
please head to [its page on Wikidata](https://www.wikidata.org/wiki/User:Lucas_Werkmeister/Wikidata_Lexeme_Forms)
and follow the instructions there.

### Code

To send a patch, you can use any of the following methods:

* [Create a Diff on Phabricator.](https://phabricator.wikimedia.org/differential/diff/create/)
  Make sure to add @LucasWerkmeister as subscriber.
* Use `git send-email`.
  (Send the patch(es) to the email address from the Git commit history.)
* Upload a diff on [GitHub Gist](https://gist.github.com/)
  and send the link to the tool’s maintainer(s) via email, Twitter, on-wiki message, or whatever.

## License

The code in this repository is released under the AGPL v3,
the translations and templates under CC BY-SA 3.0.
See the LICENSE file for details.
