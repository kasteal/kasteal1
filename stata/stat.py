from scipy.stats import kstest
import pandas as p


a = p.read_csv('data.csv')
n = len(a["Data"])
a = p.DataFrame(data={'Data': a['Data']})['Data']

s, p = kstest(a, (a.mean(), a.std()), 'norm')
if p > 0.05:
    print('Норм пацан')
else:
    print('Он ненормальный, он псих')
