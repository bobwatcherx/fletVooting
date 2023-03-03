from flet import *


def main(page:Page):

	banana = Text(0,size=30,weight="bold")
	watermelon = Text(0,size=30,weight="bold")



	def bananacounter(e):
		page.pubsub.send_all("banana")
		page.update()

	def watermeloncounter(e):
		page.pubsub.send_all("watermelon")
		page.update()


	def on_listen_you_choices(result):
		# AND IF YOU CHOICES BANANA THEN ADD 1 INCREMENT TO VALUE BANANA
		if result == "banana":
			# ADD INCREMENT
			banana.value +=1
			page.update()
		if result == "watermelon":
			# ADD INCREMENT
			watermelon.value +=1
			page.update()	


	page.pubsub.subscribe(on_listen_you_choices)

	page.add(
	Column([
		Row([Text("You Choices",
			size=30,weight="bold"
			)],alignment="center"),

		Row([
		Container(
			bgcolor="red200",
			padding=10,
			content=Column([
				Text("banana",size=30,weight="bold"),
				banana
				])
			),
		Container(
			bgcolor="blue200",
			padding=10,
			content=Column([
				Text("watermelon",size=30,weight="bold"),
				watermelon

				])
			),
			]),

		# CREATE BUTTON
		Row([
			ElevatedButton("i choices banana",
				bgcolor="red200",color="white",
				on_click=bananacounter
				),
			ElevatedButton("i choices watermelon",
				bgcolor="blue200",color="white",
				on_click=watermeloncounter
				),
			])



		])

		)

# ADD SUPPORT FOR WEB 

flet.app(target=main,port=8000,view=WEB_BROWSER)
