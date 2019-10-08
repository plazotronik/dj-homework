from _datetime import datetime, date


class DateConverter:
    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: date) -> str:
        return value.strftime('%Y-%m-%d')