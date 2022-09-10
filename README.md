# Wikidata Lexeme Forms

[This tool](https://lexeme-forms.toolforge.org/) lets users create Wikidata lexemes with pre-populated forms,
such as the declensions of a noun or the conjugations of a verb.

## Toolforge setup

On Wikimedia Toolforge, this tool runs under the `lexeme-forms` tool name.
Source code resides in `~/www/python/src/`,
a virtual environment is set up in `~/www/python/venv/`,
logs end up in `~/uwsgi.log`.
The `uwsgi.ini` configuration file in the source code repository
is symlinked into `~/www/python/uwsgi.ini`.

To update the tool, assuming there were no changes in the Python environment:
```
git fetch
git log -p @..@{u} # inspect changes
git rebase
kubectl rollout restart deployment lexeme-forms
```

If there were new changes in the Python environment (e.g. new dependencies),
add the following steps after the `git rebase`:
```
webservice shell
source ~/www/python/venv/bin/activate
pip-sync ~/www/python/src/requirements.txt
```

If you’re fully restarting the webservice,
also update the Kubernetes deployment created by the `webservice` command afterwards:
```
webservice stop
# do whatever you need to do (new Python version -> new venv?)
webservice start
kubectl patch deployment lexeme-forms -p "$(<~/www/python/src/patch-add-startup-probe.yml)"
```

## Local development setup

You can also run the tool locally, which is much more convenient for development
(for example, Flask will automatically reload the application any time you save a file).
Note that a local setup will not actually perform edits unless you create a `config.yaml` file.

```
git clone https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms.git
cd tool-lexeme-forms
pip3 install -r requirements.txt
FLASK_APP=app.py FLASK_ENV=development flask run --extra-files i18n/en.json
```

If you want, you can do this inside some virtualenv too.

## Contributing

Yay contributions! <3

### Templates

To propose new templates for the tool,
please head to [its page on Wikidata](https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms)
and follow the instructions there.

### Code

To send a patch, you can submit a
[pull request on GitHub](https://github.com/lucaswerkmeister/tool-lexeme-forms) or a
[merge request on GitLab](https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms).
(E-mail / patch-based workflows are also acceptable.)
It’s best to reach out to the maintainer(s) in advance, though,
to see if the contribution is likely to be accepted or not.

Additions or changes to the templates or translations
should always be made on-wiki (see [above](#templates)),
not sent as patches.

## License

The code in this repository is released under the AGPL v3,
the translations and templates under CC BY-SA 3.0.
See the LICENSE file for details.
