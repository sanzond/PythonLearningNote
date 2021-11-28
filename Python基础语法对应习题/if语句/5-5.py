alien_colors = ["green", "yellow", "red"]

for alien_color in alien_colors:
	if alien_color == "green":
		print("You get 5 points")
	elif alien_color != "green":
		print("You get 10 points")
	else:
		print("You get 20 points")