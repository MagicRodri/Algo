a,b,c,d,e,f,g,h = range(8)

N = [
	{b,c,d,e,f},	#a
	{c,e},		#b
	{d},		#c
	{e},		#d
	{f},		#e
	{c,g,h},	#f
	{f,h},		#g
	{f,g}		#h
]

N ={
	'a':set('bcdef'),
	'b':set('ce'),
	'c':set('d'),
	'd':set('e'),
	'e':set('f'),
	'f':set('cgh'),
	'g':set('fh'),
	'h':set('fg')
}
