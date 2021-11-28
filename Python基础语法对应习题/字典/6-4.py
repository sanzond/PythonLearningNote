key_word = {
	"list":"a type of data structure", 
	"dic":"a type of data structure",
	"int()":"transfer data from string to int",
	"str()":"transfer data from int to str",
	"for":"try element in the object"
	}

for key,value in key_word.items():
	print(key + " : " + value)


key_word.update({"int":"a type of data type"})
key_word.update({"str":"a type of data type"})
key_word.update({"float":"a type of data type"})
key_word.update({"double":"a type of data type"})
key_word.update({"long long":"a type of data type"})

for key,value in key_word.items():
	print(key + " : " + value)