import csv

class CSVConverter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)

    def write_data(self, rows):
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    def convert(self):
        try:
            rows = self.read_data()
            if not rows:
                print("⚠️ Input file is empty.")
            else:
                self.write_data(rows)
                print(f"✅  len :  {len(rows)} columns '{self.input_file}'  Readed in '{self.output_file}' ")
                print(f"📌  columns  {rows[0] if rows else 'nothing'}")
        except FileNotFoundError:
            print(f"❌  error:  '{self.input_file}' not found")
            print("Error only Happend")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
  # in here we can replsce our input file name and out put file name - this I use only for my files i choice them
    converter = CSVConverter("car_data_raw.txt", "iranian_cars_final.csv")
    converter.convert()
