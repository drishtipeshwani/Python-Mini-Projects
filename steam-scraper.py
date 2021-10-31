from bs4 import BeautifulSoup
import requests

def main():
	type = "Free"

	print(f'\nSearching for {type.upper()} games...\n')

	response = requests.get('https://store.steampowered.com/')
	soup = BeautifulSoup(response.text, 'lxml')
	games = soup.find_all('a', class_='tab_item')


	# clearning the contents of the file before writing to it
	open('info.txt', 'w').close()

	for game in games:
		game_name = game.find('div', class_='tab_item_name').text
		game_tags = game.find('div', class_='tab_item_top_tags').text
		game_price = game.find('div', class_='discount_final_price')
		more_info = game['href']

		if (game_price == None):
			continue
		else:
			game_price = game_price.text

		if type == "Free":
			if "Free" in game_price:
				print_game_info(game_name, game_price, more_info, game_tags)
		else:
			print('Please type f to know about free games and p to know about paid games')
			exit(0)
	print('File Saved as info.txt')	

def print_game_info(game_name, game_price, more_info, game_tags):
	with open('info.txt', 'a') as f:
		f.write(game_name)
		f.write(f'\nPrice: {game_price}\n')
		f.write(f'Tags: {game_tags}\n')
		f.write(f'More Info: {more_info}\n\n')

main()
