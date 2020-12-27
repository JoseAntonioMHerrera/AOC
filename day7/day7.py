def lineBagParser(line):
	words =  line.split('contain')
	outermost_bag = words[0].replace(" ","").split("bag")[0]
	shiny_gold = True if "shiny gold" in words[1] else False
	contents = words[1].replace(" ","")
	inside_bags = []
	quantity_inside_bags= {}
	if ',' in contents:
		inside_bags = contents.split(',')
		for i in range(len(inside_bags)):
			number_and_color = inside_bags[i].split("bag")
			inside_bags[i] = number_and_color[0][1:]
			quantity_inside_bags[inside_bags[i]] = int(number_and_color[0][:1])
	elif 'noother' not in contents:
		number_and_color = contents.split("bag")[0]
		inside_bags = [number_and_color[1:]]
		quantity_inside_bags[inside_bags[0]] = int(number_and_color[:1])
	
	return {'outermost_bag':outermost_bag,'shiny_gold':shiny_gold,'inside_bags':inside_bags,'quantity':quantity_inside_bags}

def lookForShiny(inside_bags,visited_bags, bag_dict):
	for bag in inside_bags:
		if bag not in visited_bags:
			if bag_dict[bag]['shiny'] == 1:
				return 1
			else:
				visited_bags.append(bag)
				if lookForShiny(bag_dict[bag]['bags'],visited_bags,bag_dict) == 1:
					return 1
	return 0

def luggageChecking(bags_list, index_bags_list, bag_dict):
	if index_bags_list == len(bags_list):
		return bag_dict
	else:
		bag_line_parsed = lineBagParser(bags_list[index_bags_list])
		bag_dict[bag_line_parsed['outermost_bag']] = {'shiny':0,'bags':bag_line_parsed['inside_bags'],'bags_quantity':bag_line_parsed['quantity']}
		if bag_line_parsed['shiny_gold'] == True:
			bag_dict[bag_line_parsed['outermost_bag']]['shiny'] = 1
		bag_dict = luggageChecking(bags_list,index_bags_list+1,bag_dict)
		shiny_found = lookForShiny(bag_line_parsed['inside_bags'],[bag_line_parsed['outermost_bag']],bag_dict)
		if shiny_found == 1 and bag_dict[bag_line_parsed['outermost_bag']]['shiny'] == 0:
			bag_dict[bag_line_parsed['outermost_bag']]['shiny'] = shiny_found
	return bag_dict

def countBagsInsideShinyGoldOne(inside_bags,current_bag,bag_dict):
	total_bags = 0
	if(len(inside_bags) == 0):
		return 1
	else:
		for bag in inside_bags:
			bag_content = countBagsInsideShinyGoldOne(bag_dict[bag]['bags'],bag,bag_dict)
			if bag_content == 1:
				total_bags += bag_content*bag_dict[current_bag]['bags_quantity'][bag]
			else:
				total_bags += bag_dict[current_bag]['bags_quantity'][bag] + bag_content*bag_dict[current_bag]['bags_quantity'][bag]
		return total_bags

f = open("input.txt", "r")
bag_dict = luggageChecking(f.readlines(), 0, {})
sum = 0
for key in bag_dict.keys():
	sum += bag_dict[key]['shiny']
print("Number: " + str(sum))
print(len(bag_dict.keys()))
howMuchBagsCanEndureAnEarthTextile = countBagsInsideShinyGoldOne(bag_dict['shinygold']['bags'],"shinygold",bag_dict)
print("The final question: " + str(howMuchBagsCanEndureAnEarthTextile))