from dataclasses import dataclass

@dataclass
class PlayerData():
	name: str = "__blank__"
	field: str = "__blank__"
	start_capital: int = 1
	end_mo_rev: int = 0
	ATR: float = (end_mo_rev*12)/(start_capital)
	difficulty: int = int(ATR)
@dataclass
class GameData():
	month: int = 1
	cash: int = 0
	mo_costs: int = 500
	customers: int = 0
	price: int = 0
	prod_progress: int = 0

loop = True

print("\nWelcome to The Founder Sim, a practical educational game that teaches you all there is to know about running a company in the AI era!")

plr1 = PlayerData()
plr1.name = input("\n- What is your name Captain? -  ")
plr1.field = input("\n\n- What field are you interested in changing forever? - ")
plr1.start_capital = int(input("\n- What's your starting capital? - "))
plr1.end_mo_rev = int(input("\n- What is your monthly revenue goal? - "))
plr1.ATR = (plr1.end_mo_rev*12)/plr1.start_capital
#difficulty is just showing the tier of ROI you are in
plr1.difficulty = int(plr1.ATR)

#i can just summarize the basic game boilerplate by using the override default value from when i call an instance
game1 = GameData(cash=plr1.start_capital)



print("\n\n..loading the sim...")
print("loaded. good luck on your journey!\n\n")

def show_cmd_handle(plr,game):
	print(commands_showcase)
def bank_stat_handle(plr,game):
	print(f"\nBank Statement as of Month {game.month}\nAccount Holder: {plr.name}\nAccount Balance: {game.cash}\nRecurring Monthly Expenses: {game.mo_costs}")
def prod_prog_handle(plr,game):
	print(f"\nProduct Report\nFidelized Customers: {game.customers}\nProduct Price Point: {game.price}\nProduct Development Progress: {game.prod_progress}")

CMD = {
"show-cmd":show_cmd_handle,"bank-stat":bank_stat_handle,"prod-prog":prod_prog_handle,"exit":None
}
commands_showcase = "\n{These are your commands available: ["+"];[".join(CMD)+"]}"

while loop:
	cmd_key = input("- Type your cmd: ")
	if cmd_key=="exit":
		break
	CMD[cmd_key](plr1,game1)

