import requests
import datetime as dt
from src.typeDefs.iegcViolMsgsFetcherResp import IegcViolMsgsFetcherResp

class IegcviolMsgsFetcherHandler():
    iegcViolMsgsFetcherUrl = ''

    def __init__(self, iegcViolMsgsFetcherUrl):
        self.iegcViolMsgsFetcherUrl = iegcViolMsgsFetcherUrl

    def fetchIegcviolMsgs(self, startDate: dt.datetime, endDate: dt.datetime) -> IegcViolMsgsFetcherResp:
        """fetch iegc violation messages using the api service

        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date

        Returns:
            IegcViolMsgsFetcherResp: Result of the iegc violation fetcher operation
        """
        createIegcViolMsgsPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.get(self.iegcViolMsgsFetcherUrl,
                            params=createIegcViolMsgsPayload)

        operationResult: IegcViolMsgsFetcherResp = {
            "isSuccess": False,
            'status': res.status_code,
            'data':  [],
            'message': 'Unable to show iegc violation messages...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['data'] = resJSON['data']
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
        return operationResult
