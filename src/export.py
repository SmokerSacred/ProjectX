import pandas as pd
from pathlib import Path

def convert_to_excel(df, file_name):
  
    input_path = Path(file_name)
    output_path = input_path.with_name(input_path.stem + "_processed" + input_path.suffix)

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:  
        df.to_excel(writer, index=False)

    

    return output_path


def style_excel(duplicates, prefilled)