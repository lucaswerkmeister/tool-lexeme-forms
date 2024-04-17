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
webservice restart
```

If there were new changes in the Python environment (e.g. new dependencies),
add the following steps after the `git rebase`:
```
webservice shell
source ~/www/python/venv/bin/activate
pip-sync ~/www/python/src/requirements.txt
```

## Local development setup

You can also run the tool locally, which is much more convenient for development
(for example, Flask will automatically reload the application any time you save a file).
Note that a local setup will not actually perform edits unless you create a `config.yaml` file.

```
git clone https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms.git
cd tool-lexeme-forms
pip3 install -r requirements.txt -r dev-requirements.txt
flask --debug run --extra-files i18n/en.json
```

If you want, you can do this inside some virtualenv too.

## Contributing

Yay contributions! <3

### Templates

To propose new templates for the tool, or make changes to the existing templates,
please head to [the tool’s page on Wikidata](https://www.wikidata.org/wiki/Wikidata:Wikidata_Lexeme_Forms)
and follow the instructions there (especially the “Language support” section).

### Translations

You can [translate the tool’s user interface](https://translatewiki.net/w/i.php?title=Special:Translate&group=wikidata-lexeme-forms)
on translatewiki.net.
(Links to the translations are also included on the wiki pages with the templates.)

### Code

To send a patch, you can submit a
[pull request on GitHub](https://github.com/lucaswerkmeister/tool-lexeme-forms) or a
[merge request on GitLab](https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms).
(E-mail / patch-based workflows are also acceptable.)
It’s best to reach out to the maintainer(s) in advance, though,
to see if the contribution is likely to be accepted or not.

Additions or changes to the templates
should always be made on-wiki, as mentioned [above](#templates).
(If you really want to, you can send corresponding patches as well,
but again, it’s best to reach out in advance.)

The translations are automatically updated from translatewiki.net;
only `en.json` and `qqq.json` should be changed directly in this source code repository.

## License

The code in this repository is released under the AGPL v3,
the translations and templates under CC BY-SA 4.0.
See the LICENSE file for details.
