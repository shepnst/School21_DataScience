
from random import randint
from telegram import Bot

import logging
import time
logging.basicConfig(level=logging.INFO, filename='analytics.log',
                    format="%(asctime)s  %(message)s")
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
TELEGRAM_TOKEN = '8038878948:AAG6UNav9aHjOOOKtejjJf7C3-RrWV0CYR8'
CHAT_ID = 1241979752
bot = Bot(token=TELEGRAM_TOKEN)


def to_bot(mes):
    bot.send_message(chat_id=CHAT_ID, text=mes)


class Research:
    def __init__(self, path):
        self.path = path
        self.data = self.file_reader()
        self.calculate = self.Calculations(self.data)

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as file:
            lines = file.readlines()
        result = []
        if len(lines) < 2:
            raise ValueError('number of line should be greater than 2')
        if has_header and len(lines[0].strip().split(',')) != 2:
            raise ValueError('there should be TWO headers')
        start_ind = 0
        if has_header == True:
            start_ind = 1
        for i in range(start_ind, len(lines)):
            temp = []
            temp.append(str(lines[i][0]))
            temp.append(str(lines[i][2]))
            if temp != ['0', '1'] and temp != ['1', '0']:
                raise ValueError('the file should contain only 0 and 1')
            result.append(list(map(int, lines[i].strip().split(','))))
        logger.info("The data were read")
        to_bot(f'{time.asctime(time.localtime())}, "The data were read"')
        return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self, data):
            heads = 0
            tails = 0
            res = []
            for i in data:
                if i[0] == 1:
                    heads += 1
                if i[1] == 1:
                    tails += 1
            res.append(heads)
            res.append(tails)

            logger.info("Calculating the counts of heads and tails")
            to_bot(
                f'{time.asctime(time.localtime())}, "Calculating the counts of heads and tails"')
            return res

        def fractions(self, h_t):
            res = []
            for value in h_t:
                res.append(value/sum(h_t)*100)

            logger.info("Calculating the fractions of heads and tails")
            to_bot(
                f'{time.asctime(time.localtime())}, "Calculating the fractions of heads and tails"')
            return res


class Analytics(Research.Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, num_predict):
        res = []
        rand = {0: [0, 1], 1: [1, 0]}
        for i in range(num_predict):
            res.append(rand[randint(0, 1)])

        logger.info("Prediction of values")
        to_bot(f'{time.asctime(time.localtime())}, "Prediction of values"')
        return res

    def predict_last(self):

        logger.info("Prediction of the las value")
        to_bot(f'{time.asctime(time.localtime())}, "Prediction of the las value"')
        return self.data[-1]

    def save_file(self, data, path, ext='txt'):
        with open(path+'.'+ext, 'w') as file:
            file.write(data)

        logger.info("The report text was save to report.txt")
        to_bot(
            f'{time.asctime(time.localtime())}, "The report text was save to report.txt"')
