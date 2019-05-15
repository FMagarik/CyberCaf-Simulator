from random import random
from random import randint

tf = 100000

def printCols(row):
	print("{: >10} | {: >10} | {: >10} | {: >10} | {: >10} | {: >10} | {: >10} | {: >10}".format(*row))

def perc(v):
	return(str(v) + '%')

def sim(d, l):
	t = tpll = npl = npd = npa15 = stol = stod = sec = stsl = stsd = 0
	tcd = [0] * d
	tcl = [0] * l

	def ia():
		return randint(5, 15)

	def tal():
		return randint(70, 110)

	def tad():
		return randint(15, 60)

	def esTiempoLibre():
		return random() <= 0.5562

	def format(v):
		return int(round(v))

	while True:
		t = tpll
		tpll = t + ia()

		if esTiempoLibre():
			i = tcl.index(min(tcl))
			if tcl[i] <= t:
				stol += t - tcl[i]
				tcl[i] = t + tal()
			else:
				sec += tcl[i] - t
				tcl[i] += tal()
			stsl += tcl[i] - t
			npl += 1
		else:
			i = tcd.index(min(tcd))
			if tcd[i] - t > 15:
				npa15 += 1
			else:
				if tcd[i] <= t:
					stod += t - tcd[i]
					tcd[i] = t + tad()
				else:
					sec += tcd[i] - t
					tcd[i] += tad()
				stsd += tcd[i] - t
				npd += 1

		if t > tf:
			ptod = format(100 * stod / (d * t))
			ptol = format(100 * stol / (l * t))
			ppa15 = format(100 * npa15 / (npa15 + npl + npd))
			ppsd = format(stsd / npd)
			ppsl = format(stsl / npl)
			pec = format(sec / (npl + npd))
			return [d, l, perc(ptod), perc(ptol), perc(ppa15), ppsd, ppsl, pec]

def simPCs(max):
	printCols(['d', 'l', 'ptod', 'ptol', 'ppa15', 'ppsd', 'ppsl', 'pec'])
	d = 1
	while d < max:
		l = max - d
		res = sim(d, l)
		printCols(res)
		d += 1
	print()

simPCs(9)