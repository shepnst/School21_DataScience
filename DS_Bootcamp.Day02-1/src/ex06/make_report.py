from config import *
from analytics import Research, Analytics


def main():
    r = Research(path)
    content = r.file_reader()
    num_obs = len(content)
    counts = r.calculate.counts(content)
    heads = counts[0]
    tails = counts[1]

    fractions_head = r.calculate.fractions(counts)[0]
    fractions_tails = r.calculate.fractions(counts)[1]
    analytics = Analytics(content)
    predict = analytics.predict_random(steps)
    heads_pred, tails_pred = tuple(sum(elem) for elem in zip(*predict))
    answer = report_text.format(
        num_obs, tails, heads,
        fractions_tails, fractions_head,
        steps, tails_pred, heads_pred)
    Analytics(r).save_file(answer, report_file)


if __name__ == '__main__':
    main()
