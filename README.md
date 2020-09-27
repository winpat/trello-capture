# Trello Capture

Capture trello cards through [dmenu](https://tools.suckless.org/dmenu/) with a single key stroke.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install trello-capture.

```bash
pip install git  git+https://github.com/winpat/trello-capture.git
```

Alternatively, you can also use [nix](https://nixos.org/).

```bash
nix -f default.nix -i trello-capture
```


## Configuration

First you need to create a an API token on the following page.

  * https://trello.com/app-key

Then there are three ways of how you can pass configuration options.

1. Create a `.trellorc` in your home directory, consisting of key/value pairs:

```
key = ...
token = ...
list_id = ...
```

2. Export them as environment variables

```bash
export TRELLO_KEY=...
export TRELLO_TOKEN=...
export TRELLO_LIST_ID=...
```

3. Pass them as option flags

```bash
> tc --key ... --token ... --list-id ...
```

## Usage

To launch trello-capture simply type `tc` in your shell:

```bash
# If you did not configure a list id, then you will interactively
# prompted to select your board and list.
> tc
```

> You might want to configure a keyboard shortcut in your window manager/desktop
> environment to maximize the usefulness.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
