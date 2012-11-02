from time import time
i = 0
cs = False
prompt = "A lot of things remind me of my father who passed" ## away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down. At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well.A lot of things remind me of my father who passed away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down. At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well."


def counter():
	i = 0 
	print prompt
	raw_input(">> Press ENTER to begin")
	begin_time = time()
	inp = raw_input()
	end_time = time()
	final_time = (end_time - begin_time) / 60
	return final_time, inp


def wpm(time, line):
	words = line.split()
	word_length = len(words)
	words_per_m = word_length / time
	return words_per_m


def wordcheck(inp):
	prompts = prompt.split()
	inputs = inp.split()
	errorcount = 0
	pairs = zip(inputs, prompts)
	for pair in pairs:
		(inputted, accepted) = pair
		if inputted != accepted:
			errorcount += 1
	return errorcount

tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
print("You total time was: %r minutes")% tm
print("with an average of: %r words per minute")% words_per_minute
errorcount = wordcheck(line)
print("with %r spelling errors") % errorcount
