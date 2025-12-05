import pandas

df = pandas.read_json("coding_quotes/quotes.json")

quotes = df[df["rating"] >= 4.5]

quote = quotes.sample().iloc[0]
message = f"Hey Coder!\n\n{quote.author} once said,\n{quote.text}"
print(message)