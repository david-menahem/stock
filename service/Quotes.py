import datetime
from models.Attr import Attr
from models.Quote import Quote


class Quotes:

    def set_attr(self,time_frame):
        options = ('Yesterday', 'Last week', 'Last month', 'Last year')
        now = datetime.datetime.now()
        formatted_date = "%Y-%m-%d"
        gap = ""
        time_unit = ""
        start_date = ""
        end_date = now - datetime.timedelta(days=1)
        end_date = self.check_day_of_week(end_date)
        end_date = end_date.strftime(formatted_date)

        if time_frame == options[0]:
            gap = "30"
            time_unit = "minute"
            start_date = end_date
        elif time_frame == options[1]:
            gap = "5"
            time_unit = "hour"
            start_date = now - datetime.timedelta(days=7)
            start_date = self.check_day_of_week(start_date)

        elif time_frame == options[2]:
            gap = "1"
            time_unit = "day"
            start_date = now - datetime.timedelta(days=30)
            start_date = self.check_day_of_week(start_date)
        elif time_frame == options[3]:
            gap = "3"
            time_unit = "week"
            start_date = now - datetime.timedelta(days=365)
            start_date = self.check_day_of_week(start_date)

        if time_frame != options[0]:
            start_date = start_date.strftime(formatted_date)

        attr = Attr(gap, time_unit, start_date, end_date)
        return attr

    @staticmethod
    def get_stats(data):
        try:
            info = data['results']

            open_price = info[0]['o']
            close_price = 0
            high = -1
            low = 1000000
            vol = 0
            for i, quote in enumerate(info):
                high_price = quote['h']
                if high_price > high:
                    high = high_price
                low_price = quote['l']
                if low_price < low:
                    low = low_price
                vol += quote['v']
                if i == len(info) - 1:
                    close_price = quote['c']

            quote = Quote(open_price, close_price, high, low, vol)
            return quote

        except Exception as e:
            print(e)

    @staticmethod
    def check_day_of_week(day):
        weekday = day.weekday()
        valid_days = [0, 1, 2, 3, 4]
        if weekday in valid_days:
            adjust_days = 0
        elif weekday == 5:
            adjust_days = 1
        else:
            adjust_days = 2

        return day - datetime.timedelta(days=adjust_days)
