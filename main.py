# Press the green button in the gutter to run the script.
import pandas as pd
from ReadSquares import *
from ReadHaberman import *

haberman_path = "haberman.data"
squares_path = "squares.txt"
if __name__ == '__main__':
    print(f'{"hello world!"}')
    # haberman_df = pd.read_csv(haberman_path)
    haberman_df = dfFromCSV(haberman_path)
    print(haberman_df)
    # print("\n\n")
    # squares_df = pd.DataFrame(read(squares_path), columns=["x", "y", "label"])
    # print(squares_df)
    # print("\n\n")
    # print(dfFromSquares(squares_path))
