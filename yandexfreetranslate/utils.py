def smartsplit(t, s, e):
	"""
	smartsplit(text, start_position, end_position)
	Splits a string into parts according to the number of characters.
	If there is a space between the start and end positions, split before a space, the word will not end in the middle.
	If there are no spaces in the specified range, divide as is, by the finite number of characters.
	"""
	t = t.replace("\r\n", "\n").replace("\r", "\n")
	if(e >= len(t)): return [t]
	l = []
	tmp=""
	i=0
	for sim in t:
		i = i + 1
		tmp = tmp + sim
		if(i<s): continue
		if(i==e):
			l.append(tmp)
			tmp=""
			i=0
			continue
		if((i > s and i < e) and (sim == chr(160) or sim == chr(9) or sim == chr(10) or sim == chr(32))):
			l.append(tmp)
			tmp=""
			i=0
			continue
	if(len(tmp)>0): l.append(tmp)
	return l
