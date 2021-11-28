names = ["Eric", "Bob", "Jobs"]
for name in names:
	if name != "Jobs":
		print("I want to invite " + name + " to join in my party")
	else:
		print("Jobs can not join in the party")

		names[2] = "Tim"
		print("I want to invite " + names[2] + "to join in my party")