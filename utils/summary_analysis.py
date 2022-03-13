import statistics as st
import pandas as pd
import numpy as np


def analysis(data):
	_analysis = {}

	_analysis['unique'] = set(data)
	_analysis['count'] = len(data)
	_analysis['sum'] = sum(data)
	_analysis['mean'] = _analysis['sum'] / _analysis['count']
	_analysis['median'] = st.median(data)
	_analysis['mode'] = st.mode(data)
	_analysis['g_mean'] = st.geometric_mean(data)
	_analysis['variance'] = st.variance(data)
	_analysis['stdev'] = st.stdev(data)
	_analysis['sterr'] = _analysis['stdev'] / np.sqrt( _analysis['count'] )
	_analysis['min'] = min(data)
	_analysis['max'] = max(data)
	_analysis['range'] = _analysis['max'] - _analysis['min']
	data_series = pd.Series(data)
	_analysis['lqua'], _analysis['uqua'] = data_series.quantile([.25, .75])
	_analysis['rqua'] = abs(_analysis['uqua'] - _analysis['lqua'])
	_analysis['skewness'] = data_series.skew()
	_analysis['kurtosis'] = data_series.kurtosis()
	_analysis['cvar'] = _analysis['stdev'] / _analysis['mean']

	return _analysis

def print_analysis(obj):
	print('\
Количество = {d[count]}\n\
Среднее значение = {d[mean]}\n\
Медиана = {d[median]}\n\
Мода = {d[mode]}\n\
Геометрическое среднее = {d[g_mean]}\n\
Дисперсия = {d[variance]}\n\
Стандартное отклонение = {d[stdev]}\n\
Стандартное ошибка = {d[sterr]}\n\
Минимальное значение = {d[min]}\n\
Максимальное значение = {d[max]}\n\
Размах = {d[range]}\n\
Первый квартиль = {d[lqua]}\n\
Третий квартиль = {d[uqua]}\n\
Межквартильный размах = {d[rqua]}\n\
Ассиметрия = {d[skewness]}\n\
Куртосис = {d[kurtosis]}\n\
Коэффициент вариации = {d[cvar]}\n\
Сумма = {d[sum]}\n\
	'.format(d=obj)
	)