def move_symbol_to_end(symbol, symbol_list):
    for i, character in enumerate(symbol_list):
        if character == symbol[0]:
            symbol_list.append(symbol_list.pop(i))

if __name__ == "__main__":
    symbol_list = ["L","F","A","B","F","C","F","O","F","U","F","R","F","S","E"]
    symbol = ["F"]
    print(f"Moving symbol {symbol} to end.\nList before modification:\n{symbol_list}")
    move_symbol_to_end(symbol, symbol_list)
    print(f"List after modification:\n{symbol_list}")