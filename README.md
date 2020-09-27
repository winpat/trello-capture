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

2. There are three ways of how you can pass configuration options.

  1. Create a `.trellorc` in your home directory, consisting of key/value pairs:

    ```
	key = ...
	token = ...
	list_id = ...
    ```

  2. Export them as environment variables

    ```
    export TRELLO_KEY=...
    export TRELLO_TOKEN=...
    export TRELLO_LIST_ID=...
    ```

  3. Pass them as option flags

    ```
    > tc --key ... --token ... --list-id
    ```

3. Profit!

```
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
