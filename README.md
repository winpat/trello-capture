# Trello Capture

Capture trello cards through [dmenu](https://tools.suckless.org/dmenu/) with a single key stroke.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install trello-capture.

```bash
pip install git  git+https://github.com/winpat/trello-capture.git
```

## Usage

1. Create a an API token on the following page.

  * https://trello.com/app-key

2. Export API key and token as environment variables or pass them as arguments.

```
export TRELLO_KEY=...
export TRELLO_TOKEN=...

# OR

> tc --key ... --token ...
```

3. Profit!

```
# By default you can choose the right board and list interactively.
> tc

# You can can also specify a default list which cards get pushed to..
> tc --list-id 5e2d1fc020c51d025010f02a
```

> You might want to configure a keyboard shortcut in your window manager/desktop
> environment to maximize the usefulness.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
