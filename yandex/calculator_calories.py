"""В файле homework.py содержится 4 класса - Record, Calculator,
CashCalculator и CaloriesCalculator. Record хранит записи о покупках или
потраченных калориях. CashCalculator и CaloriesCalculator наследуются от
Calculator и ведут подсчёты денег и калорий соответственно."""

import datetime as dt


class Record:
    """Хранит сумму/калории, дату и комментарий."""

    def __init__(self, amount: float, comment: str, date: str = None):
        """Принимает сумму или количество калорий, комментарий и дату."""
        now = dt.datetime.now()
        date_format = '%d.%m.%Y'
        if date is None:
            date = now.date()
        if date != now.date():
            moment = dt.datetime.strptime(date, date_format)
            date = moment.date()
        self.amount = amount
        self.comment = comment
        self.date = date


class Calculator:
    """Родительский класс. Принимает лимит,
    суммирует записи за конкретные даты."""

    def __init__(self, limit: float):
        self.limit = limit
        self.records = []
        self.now = dt.datetime.now()

    def add_record(self, record: list) -> None:
        """Сохраняет новую запись о приёме пищи."""
        self.records.append(record)

    def get_today_stats(self) -> float:
        """Получаем статистику за сегодня."""
        today_record = 0
        for record in self.records:
            if record.date == self.now.date():
                today_record += record.amount
        return today_record

    def get_week_stats(self) -> float:
        """Получаем статистику за последние 7 дней."""
        seven_days_record = 0
        seven_day = self.now.date() - dt.timedelta(days=7)
        for record in self.records:
            if seven_day < record.date <= self.now.date():
                seven_days_record += record.amount
        return round(seven_days_record, 2)


class CaloriesCalculator(Calculator):
    """Калькулятор калорий."""

    def get_calories_remained(self) -> str:
        """Определяет, сколько ещё калорий можно получить за сегодня."""
        remain_limit_kcal = self.limit - self.get_today_stats()
        if remain_limit_kcal > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remain_limit_kcal} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """Калькулятор денег."""

    RUB_RATE = 1
    USD_RATE = 74.05
    EURO_RATE = 90.15

    def get_today_cash_remained(self, currency: str = 'rub') -> str:
        """Получаем остаток денег на сегодня."""
        currency_info = {'rub': (self.RUB_RATE, 'руб'),
                         'usd': (self.USD_RATE, 'USD'),
                         'eur': (self.EURO_RATE, 'Euro')}
        if currency not in currency_info.keys():
            return 'Калькулятор пока не знает такой валюты'

        rate, title = currency_info[currency]
        remain_cash = self.limit - self.get_today_stats()
        if (currency != 'rub' and remain_cash != 0):
            remain_cash /= rate
        remain_cash = round(remain_cash, 2)

        if remain_cash == 0:
            return 'Денег нет, держись'
        if remain_cash > 0:
            return f'На сегодня осталось {remain_cash} {title}'
        remain_cash = abs(remain_cash)
        return (f'Денег нет, держись: твой долг - {remain_cash} {title}')
