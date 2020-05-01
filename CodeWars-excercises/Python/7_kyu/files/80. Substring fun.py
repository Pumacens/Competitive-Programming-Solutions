def nth_char(words):
	return ''.join(words[i][i] for i in range(len(words)))


# def nth_char(words):
#     return ''.join(w[i] for i,w in enumerate(words))