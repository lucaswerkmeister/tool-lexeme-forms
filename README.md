# Wikidata Lexeme Forms

[This tool](https://lexeme-forms.toolforge.org/) lets users create Wikidata lexemes with pre-populated forms,
such as the declensions of a noun or the conjugations of a verb.

## Toolforge setup

On Wikimedia Toolforge, this tool runs under the `lexeme-forms` tool name,
from a container built using the [Toolforge Build Service](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Building_container_images).

### Image build

To build a new version of the image,
run the following command on Toolforge after becoming the tool account:

```sh
toolforge build start --use-latest-versions https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms
```

The image will contain all the dependencies listed in `requirements.txt`,
as well as the commands specified in the `Procfile`.

### Webservice

The web frontend of the tool runs as a webservice using the `buildpack` type.
The web service runs the first command in the `Procfile` (`web`),
which runs the Flask WSGI app using gunicorn.

```
webservice start
```

Or, if the `~/service.template` file went missing:

```
webservice --mount=none buildservice start
```

If it’s acting up, try the same command with `restart` instead of `start`.

### Configuration

The tool reads configuration from both the `config.yaml` file (if it exists)
and from any environment variables starting with `TOOL_*`.
The config file is more convenient for local development;
the environment variables are used on Toolforge:
list them with `toolforge envvars list`.
Nested dicts are specified with envvar names where `__` separates the key components,
and the tool lowercases keys in nested dicts,
so that e.g. the following are equivalent:

```sh
toolforge envvars create TOOL_OAUTH__CONSUMER_KEY 1fdd6b7040497a2a942369fec07cd598
```

```yaml
OAUTH:
    CONSUMER_KEY: 1fdd6b7040497a2a942369fec07cd598
```

For the available configuration variables, see the `config.yaml.example` file.

### Update

To update the tool, build a new version of the image as described above,
then restart the webservice:

```sh
toolforge build start --use-latest-versions https://gitlab.wikimedia.org/toolforge-repos/lexeme-forms
webservice restart
```

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
