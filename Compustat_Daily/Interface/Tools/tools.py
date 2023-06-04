import pandas as pd
import wrds as w
from datetime import date
from dateutil.relativedelta import relativedelta


class wrdsdata:

    def __init__(self):

        global wrds

        wrds = w.Connection(wrds_username='joldmixon')
        print ('Connected')

    def get_data(symbol,period,duration):

        time_period = {f'{period}' : duration}
        start = (date.today()- relativedelta(**time_period)).strftime("%m/%d/%Y")
        p = {'symbol': symbol, 'start':start}
        ohlc = wrds.raw_sql("""select *
                                    from comp_na_daily_all.secd
                                    where tic = %(symbol)s
                                    and datadate>=%(start)s""",
                                    params=p,
                                    date_cols=['date'])
        df = pd.DataFrame(ohlc).reset_index().drop(columns='index').rename(columns={"prcod": "Open", "prchd": "High", "prcld": "Low", "prccd": "Close","cshtrd": "Volume"})
        return df