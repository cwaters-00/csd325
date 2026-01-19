
import csv
from datetime import datetime

from matplotlib import pyplot as plt
import sys

def plot_temps(temperatures, dates, temp_type, color):
    """Generate and display a graph for high or low temps"""
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(dates, temperatures, c=color, alpha=0.8)
    
    
    #formatting of plot
    ax.set_title(f"Daily {temp_type} Temperatures-2018", fontsize=26)
    ax.set_xlabel('',fontsize=18)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)",fontsize=18)
    ax.tick_params(axis='both', which='major', labelsize=13)
    
    plt.show()


def get_weather_data(filename):
    """read CSV file and extra dates and their associated temperatures"""
    dates,  highs, lows = [],[],[]
    try:
    
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            #date, TMAX, and, TMIN are the associated columns
            date_index = header_row.index('DATE')
            tmax_index = header_row.index('TMAX')
            tmin_index = header_row.index('TMIN')
            
            for row in reader:
                try:
                    current_date = datetime.strptime(row[date_index], "%m/%d/%y")
                    high = int(row[tmax_index])
                    low = int(row[tmin_index])
                except ValueError:
                    print(f"missing data for date{row[date_index]}. now skipping row.")
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    return dates, highs, lows

def main():
    """main function and loop"""
    print("welcome to sitka weather visualizer version 2")
    instructions = "Enter 'highs' for high temperatures and 'lows' for low temperatures, or 'exit' to exit"
    print(instructions)
    
   #load data at beginning of program
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = get_weather_data(filename)
    
    while True:
        choice = input("\nEnter your choice (highs/lows/exit): ").strip().lower()
        if choice == 'highs':
            print("Displaying high temperatures---")
            plot_temps(dates, highs,  "High",'red')
        elif choice == 'lows':
            print("Displaying low temperatures---")
            plot_temps(dates, lows, "Low",'cyan')
        elif choice == 'exit':
            print("Exiting. Until next time!---")
            sys.exit(0)
        else:
            print(f"Invalid input: '{choice}'. Please choose from 'highs', 'lows', 'exit'.")
            print(instructions)
            
            
if __name__ == '__main__':
    main()

    