from typing import TypedDict


class IegcViolMsgsFetcherResp(TypedDict):
    isSuccess: bool
    status: int
    message: str
    data: list
