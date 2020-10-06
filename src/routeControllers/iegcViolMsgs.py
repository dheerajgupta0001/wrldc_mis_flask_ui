from flask import Blueprint, jsonify, render_template, request
import datetime as dt
import os
from src.appConfig import getConfig
from src.fetcherServices.iegcViolMsgsFetcher import IegcviolMsgsFetcherHandler

# get application config
appConfig = getConfig()

fetchIegcViolMsgsPage = Blueprint('iegcViolMsgs', __name__,
                              template_folder='templates')

@fetchIegcViolMsgsPage.route('/', methods=['GET', 'POST'])
def fetchIegcViolMsgs():
    # in case of post request, fetch iegc viol msgs and return json response
    if request.method == 'POST':
        startDate = request.form.get('startDate')
        endDate = request.form.get('endDate')
        iegcViolMsgsFetcher = IegcviolMsgsFetcherHandler(
            appConfig['iegcViolMsgsFetcherServiceUrl'])
        startDate = dt.datetime.strptime(startDate, '%Y-%m-%d')
        endDate = dt.datetime.strptime(endDate, '%Y-%m-%d')
        resp = iegcViolMsgsFetcher.fetchIegcviolMsgs(startDate, endDate)
        msg= resp['data']
        return render_template('fetchIegcMsgs.html.j2', msgData= msg)
    # in case of get request just return the html template
    return render_template('fetchIegcMsgs.html.j2')