import datetime


class Attr:
    def set_attr(self, time_frame):
        OPTIONS = ('Yesterday', 'Last week', 'Last month', 'Last year')
        now = datetime.datetime.now()
        formatted_date = "%Y-%m-%d"
        gap = ""
        time_unit = ""
        start_date = ""
        end_date = now - datetime.timedelta(days=1)
        end_date = end_date.strftime(formatted_date)

        if time_frame == OPTIONS[0]:
            gap = "30"
            time_unit = "minute"
            start_date = end_date
        elif time_frame == OPTIONS[1]:
            gap = "5"
            time_unit = "hour"
            start_date = now - datetime.timedelta(days=7)
        elif time_frame == OPTIONS[2]:
            gap = "1"
            time_unit = "day"
            start_date = now - datetime.timedelta(days=30)
        elif time_frame == OPTIONS[3]:
            gap = "3"
            time_unit = "week"
            start_date = now - datetime.timedelta(days=365)

        if time_frame != OPTIONS[0]:
            start_date = start_date.strftime(formatted_date)
        attr = {"gap": gap, "time_unit": time_unit, "start_date": start_date, "end_date": end_date}
        return attr