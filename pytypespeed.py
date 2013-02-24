from time import time
i = 0
cs = False
prompt = "A lot of things remind me of my father who passed away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down." ##At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well.A lot of things remind me of my father who passed away when I was 24. Driving on certain back roads he showed me. Stopping at certain stores he always used to go to. Eating at his favorite places. More and more of these places are fading away too though. The roads keep getting built up more and more. The shops and restaurants are closing down. At first it was heart breaking that my father wasn't in this world anymore. But slowly the things that remind me of him are leaving this world as well."


def counter():
	i = 0 
	print prompt
	raw_input(">> Press ENTER to begin")
	begin_time = time()
	inp = raw_input("\n")
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
	
	idx = 0
	for inp in inputs:
		if inp != prompts[idx]:
			errorcount += 1
			if inp == prompts[idx + 1]:
				idx += 2
			elif inp != prompts[idx - 1]:
				idx += 1
		else:
			idx += 1
<<<<<<< HEAD

	words_left = len(prompts) - len(inputs)
	correct = float(len(prompts)) - float(errorcount)
	percentage = (((float(correct) / float(len(prompts))) - float(words_left) / float(len(prompts))) * 100)
=======
	correct = float(len(prompts)) - float(errorcount)
	percentage = ((float(correct) / float(len(prompts))) * 100)
>>>>>>> 6ede4ccec69478f2c623aed14d39acbc88a624c2
	
	return percentage


tm, line = counter()
tm = round(tm, 2)
words_per_minute = wpm(tm, line)
words_per_minute = round(words_per_minute, 2)
print("You total time was: %r minutes")% tm
print("with an average of: %r words per minute")% words_per_minute
percentage = wordcheck(line)
percentager = round(percentage, 2)
print("with an accuracy of: %r %% accuracy") % percentager
<<<<<<< HEAD

=======
>>>>>>> 6ede4ccec69478f2c623aed14d39acbc88a624c2
