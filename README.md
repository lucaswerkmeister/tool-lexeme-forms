# Wikidata Lexeme Forms

[This tool](https://lexeme-forms.toolforge.org/) lets users create Wikidata lexemes with pre-populated forms,
such as the declensions of a noun or the conjugations of a verb.

## Toolforge setup

On Wikimedia Toolforge, this tool runs under the `lexeme-forms` tool name,
using the [Toolforge Components Service](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Deploy_your_tool) to coordinate
building a container with the [Toolforge Build Service](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Build_Service)
and then deploying that for the webservice.
The components configuration is in the `toolforge.yaml` file.

To start a new deployment,
run the following command on Toolforge after becoming the tool account:

```sh
toolforge components deployment create
```

This should automatically kick off an image build and restart the webservice at the end.

### Details and troubleshooting

To inspect the overall deployment status, run:

```sh
toolforge components deployment show
```

To debug the image build step, it may be useful to trigger an image build explicitly –
you can add `--ref=foobar` to build from the `foobar` branch instead of the `main` branch:

```sh
toolforge build start https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms
```

The web frontent is a Flask WSGI app using gunicorn,
and runs as the `lexeme-forms` job,
which you may inspect with commands like these:

```sh
toolforge jobs show lexeme-forms
toolforge jobs logs lexeme-forms
kubectl get deployment lexeme-forms
kubectl exec -it deployment/lexeme-forms -- bash
```

### Configuration

The tool reads configuration from both the `config.yaml` file (if it exists)
and from any environment variables starting with `TOOL_*`.
The config file is more convenient for local development;
the environment variables are used on Toolforge:
list them with `toolforge envvars list`.
Nested dicts are specified with envvar names where `__` separates the key components,
so that e.g. the following are equivalent:

```sh
toolforge envvars create TOOL_OAUTH__CLIENT_ID 21e78cd6fe1e3601f89ff4356abba4bd
```

```yaml
OAUTH:
    CLIENT_ID: 21e78cd6fe1e3601f89ff4356abba4bd
```

For the available configuration variables, see the `config.yaml.example` file.

### Update

The tool should automatically be updated on every push to the `main` branch.
To trigger a manual update, run `toolforge components deployment create` as described above.

## Local development setup

You can also run the tool locally, which is much more convenient for development
(for example, Flask will automatically reload the application any time you save a file).
Note that a local setup will not actually perform edits unless you create a `config.yaml` file.

```
git clone https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms.git
cd lexeme-forms
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
