from os import getenv
from typing import Dict, Iterable, List, Optional

import requests
import sh
from pydantic import BaseModel
from requests import Response


class Resource(BaseModel):
    id: str
    name: str


class Board(Resource):
    pass


class BoardList(Resource):
    pass


class Trello:
    def __init__(self, key: str, token: str):
        self.key = key
        self.token = token

    def request(self, method: str, endpoint: str, params: Dict = {}) -> Response:
        params.update(
            {
                "token": self.token,
                "key": self.key,
            }
        )
        headers = {"Accept": "application/json"}
        url = f"https://api.trello.com/1/{endpoint}"
        return requests.request(method, url, headers=headers, params=params)

    def get_boards(self) -> List[Board]:
        response = self.request("GET", "members/me/boards/")
        return [Board(**board_data) for board_data in response.json()]

    def get_lists(self, board: Board) -> List[BoardList]:
        response = self.request("GET", f"boards/{board.id}/lists/")
        return [BoardList(**list_data) for list_data in response.json()]

    def create_card(self, board_list: BoardList, name: str) -> None:
        params = {"idList": board_list.id, "name": name}
        response = self.request("POST", "cards/", params=params)
        response.raise_for_status()


def dmenu(choices: Optional[Iterable] = None) -> str:
    if choices:
        dmenu_choices = "\n".join(choices)
        return_value = sh.dmenu(sh.echo(dmenu_choices))
    else:
        return_value = sh.dmenu()
    choice = return_value.stdout.decode().strip()
    return choice


def select_resource(resources: List[Resource]) -> Resource:
    mapping = {resource.name: resource for resource in resources}
    options = [resource.name for resource in resources]
    choice = dmenu(options)
    return mapping[choice]


def main():
    trello = Trello(
        key=getenv("TRELLO_KEY"),
        token=getenv("TRELLO_TOKEN"),
    )

    boards = trello.get_boards()
    board = select_resource(boards)

    board_lists = trello.get_lists(board)
    board_list = select_resource(board_lists)

    card_name = dmenu()
    trello.create_card(board_list, card_name)


if __name__ == "__main__":
    main()
