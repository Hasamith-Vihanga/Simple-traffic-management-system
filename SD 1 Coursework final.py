import csv
from datetime import datetime #Imported csv and datetime

def validate_date_input():
    while True:
        try:
            day=int(input("Please enter the day of the survey in the format DD: "))
            if 1<=day<=31:
                break
            else:
                print("Out of range- Values must be in the range of 1 to 31")
        except ValueError:
            print("Enter valid integer")
    while True:
        try:
            month=int(input("Please enter the month of the survey in the format MM: "))
            if 1<=month<=12:
                break
            else:
                print("Out of range- Values must be in the range of 1 to 12")
        except ValueError:
                print("Enter valid integer")
        
            
    while True:
        try:
            year=int(input("Please enter the year of the survey in the format YYYY: "))
            if 2000<=year<=2024:
                    break
            else:
                print("Please enter the year with in the range of 2000 to 2024")
        except ValueError:
            print("Enter valid integer")
                
                
            
    return day,month,year
        
        
        
        
        
      
def loadData(day,month,year):
    file1=f"traffic_data{day:02d}{month:02d}{year}.csv"

  

    if not FileNotFoundError:
        print(f"Loading from {file1}")

    with open("results.txt","a") as file:
        file.write(f"data file selected is {file1}\n")

    try:
        with open(file1, newline='' ) as csvfile:
            reader=csv.DictReader(csvfile)
            record=list(reader)
            return record
    except FileNotFoundError:
            print("No data file for the selected date")
            return[] 

#Task B:Processed outcomes

#Initializing counter variables 

def process_csv_data(record):
    total_vehicles=0
    total_trucks=0
    total_twowheeled=0
    total_busses=0
    total_electric_vehicles=0
    total_over_speeding=0
    raining_hours=0
    total_bicycles=0
    total_busses_to_north=0
    scooters_elm_avenue_rabbit_road=0
    total_vehicles_elm_avenue_rabbit_road=0
    total_vehicles_hanley_highway_westway=0
    no_turning_vehicles=0
    rainlist = []
    timelist=[]
    elm_avenue_hour_by_hour_vehicle_count=[]
    hanley_highway_hour_by_hour_vehicle_count=[]
    hours_lst=[]
    
    
    
    
    
    

#To track headers of csv file to variables
    for row in record:
        junction_name=row["JunctionName"]
        time=row["timeOfDay"]
        weather=row["Weather_Conditions"]
        vehicle_speed=row["VehicleSpeed"]
        type_of_vehicle=row["VehicleType"]
        hour=time.split(":")[0]
        electric=row["elctricHybrid"]
        junction_speed=row["JunctionSpeedLimit"]
        direction_in=row["travel_Direction_in"]
        direction_out=row["travel_Direction_out"]
        
        
        
#To increase counter variables and calculate data       

        if type_of_vehicle=="Truck":
            total_trucks+=1
        if type_of_vehicle in ["Motorbike","Bike","Scooter"]:
            total_twowheeled+=1
        if vehicle_speed>junction_speed:
            total_over_speeding+=1
        if type_of_vehicle=="Bicycle":
            total_bicycles+=1
        if electric=="TRUE":
            total_electric_vehicles+=1
        if junction_name=="Elm Avenue/Rabbit Road" and direction_in=="N" and type_of_vehicle=="Buss":
            total_busses_to_north+=1
        if junction_name=="Elm Avenue/Rabbit Road":
            total_vehicles_elm_avenue_rabbit_road+=1
        if junction_name=="Hanley Highway/Westway":
            total_vehicles_hanley_highway_westway+=1
        if junction_name=="Elm Avenue/Rabbit Road" and type_of_vehicle=="Scooter":
            scooters_elm_avenue_rabbit_road+=1
        if direction_in==direction_out:
            no_turning_vehicles+=1
        if weather=="Heavy Rain" or weather=="Light Rain":
            raintime = datetime.strptime(time,'%H:%M:%S').time()
            rainhour = raintime.hour
            if rainhour not in rainlist:
                raining_hours+=1
                rainlist.append(rainhour)
        t=datetime.strptime(row['timeOfDay'], "%H:%M:%S")
        hour=t.hour   #Extracting the hour
        if hour not in hours_lst:
            hours_lst.append(hour)
            #Initializing the traffic counts o to zero for hour
            elm_avenue_hour_by_hour_vehicle_count.append(0)
            hanley_highway_hour_by_hour_vehicle_count.append(0)
        #Finding the index number and increment vehicle count for the appropriate junction            
        index_no=hours_lst.index(hour)
        if junction_name=="Elm Avenue/Rabbit Road":
            elm_avenue_hour_by_hour_vehicle_count[index_no]+=1
        elif junction_name=="Hanley Highway/Westway":
            hanley_highway_hour_by_hour_vehicle_count[index_no]+=1
        total_vehicles+=1
        
        truck_percentage=(total_trucks/total_vehicles)*100

        average_bicycles_per_hour=total_bicycles/24

        scooter_percentage_elm_avenue_rabbit_road=(scooters_elm_avenue_rabbit_road)/total_vehicles_elm_avenue_rabbit_road*100
    max_elm_avenue=max(elm_avenue_hour_by_hour_vehicle_count)
    max_hanley_highway=max(hanley_highway_hour_by_hour_vehicle_count)
    
    maximum_frequency=max(max_elm_avenue,max_hanley_highway)
    

    
    
    
#Return to a dictionary
    details={
               "total_vehicles":total_vehicles,
               "total_trucks":total_trucks,
               "total_twowheeled":total_twowheeled,
               "total_busses":total_busses,
               "total_electric_vehicles":total_electric_vehicles,
               "total_over_speeding":total_over_speeding,
               "no_turning_vehicles":no_turning_vehicles,
               "raining_hours":raining_hours,
               "total_bicycles":total_bicycles,
               "total_busses_to_north":total_busses_to_north,
               "scooters_elm_avenue_rabbit_road":scooters_elm_avenue_rabbit_road,
               "total_vehicles_hanley_highway_westway":total_vehicles_hanley_highway_westway,
               "total_vehicles_elm_avenue_rabbit_road":total_vehicles_elm_avenue_rabbit_road,
               "truck_percentage":truck_percentage,
               "average_bicycles_per_hour":average_bicycles_per_hour,
               "scooter_percentage_elm_avenue_rabbit_road":scooter_percentage_elm_avenue_rabbit_road
               
        }
    return (hours_lst,elm_avenue_hour_by_hour_vehicle_count,hanley_highway_hour_by_hour_vehicle_count,maximum_frequency,details)
    
       
#To print calculated data to the user              
def printing_data(results):
    print(f"The total number of vehicles recorded for this day {results['total_vehicles']}")
    print(f"The total number of trucks recorded for this date {results['total_trucks']}")
    print(f"{results['total_electric_vehicles']} electric vehicles recorded for this date")
    print(f"{results['total_twowheeled']} two-wheeled vehicles recorded for this date")
    print(f"{results['total_over_speeding']} over speedings recorded")
    print(f"Total number of busses leaving Elm Avenue/Rabbit Road heading north {results['total_busses_to_north']}")
    print(f"The total number of vehicles through both junctions without turning left or right:{results['no_turning_vehicles']}")
    print(f"Total vehicles through Elm Avenue/Rabbit Road:{results['total_vehicles_elm_avenue_rabbit_road']}")
    print(f"Total vehicles through Hanley Highway/Westway:{results['total_vehicles_hanley_highway_westway']}")
    print(f"The percentage of total vehicles recorded that are trucks for this date is {round(results['truck_percentage'])}%")
    print(f"{round(results['scooter_percentage_elm_avenue_rabbit_road'])}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters")
    print(f"The number of hours rain for this day: {results['raining_hours']}")
    print("Saved data successfully to the 'results.txt'")
    
    
#Task C: Saving to text file
    
#To write calculated data to text file in append mode
def writing_data(results):
    with open("results.txt","a") as file:
        file.write(f"The total number of vehicles recorded for this day {results['total_vehicles']}\n")
        file.write(f"The total number of trucks recorded for this date {results['total_trucks']}\n")
        file.write(f"{results['total_electric_vehicles']} electric vehicles recorded for this date\n")
        file.write(f"{results['total_twowheeled']} two-wheeled vehicles recorded for this date\n")
        file.write(f"total number of busses leaving Elm Avenue/Rabbit Road heading north {results['total_busses_to_north']}\n")
        file.write(f"{results['no_turning_vehicles']} vehicles driven through both junctions without turning right or left\n")
        file.write(f"Total vehicles through Elm Avenue/Rabbit Road:{results['total_vehicles_elm_avenue_rabbit_road']}\n")
        file.write(f"Total vehicles through Hanley Highway/Westway:{results['total_vehicles_hanley_highway_westway']}\n")
        file.write(f"The percentage of total vehicles recorded that are trucks for this date is {round(results['truck_percentage'])}%\n")
        file.write(f"{round(results['scooter_percentage_elm_avenue_rabbit_road'])}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters\n")
        file.write(f"Raining hours for this day: {results['raining_hours']}\n")
       


#Task D: Histogram Dispaly
import tkinter as tk

def histogram_draw(hours_lst,elm_avenue_hour_by_hour_vehicle_count,hanley_highway_hour_by_hour_vehicle_count,maximum_frequency,day,month,year):
    root=tk.Tk()
    root.geometry("1300x700")
    root.title("Histogram")

    canvas=tk.Canvas(root,width=1300,height=700,bg="white")
    canvas.pack()
    canvas.create_text(650,30,text=f"Histogram of vehicle frequency hour by hour on {day}/{month}/{year}",font=30)
    #Adding legends to both junctions
    canvas.create_rectangle(40,50,55,65,fill="yellow")
    canvas.create_rectangle(40,70,55,85,fill="pink")
    #Labeling junction next to legends
    canvas.create_text(140,57,text="Elm Avenue/Rabbit Road")
    canvas.create_text(140,77,text="Hanley Highway/Westway")

    line=canvas.create_line(35,665,1235,665)
    
#Initializing dimensions to draw the histogram    
    margin=35
    canvas_width=1300
    canvas_height=700
    bar_width=15
    space_between_categories=(canvas_width-2*margin)/24
    space_between_bars=6
    maximum_height=canvas_height-2*margin-100
    
    
    
    for i in hours_lst:
        # Calculating dimensions of bar by bar
        x_start=margin+i*space_between_categories
        bar1_x1=x_start
        bar1_x2=bar1_x1+bar_width
        bar2_x1=bar1_x2+space_between_bars
        bar2_x2=bar2_x1+bar_width
        y_bottom=canvas_height-margin
        #Calculating the height of bars         
        bar1_height=(elm_avenue_hour_by_hour_vehicle_count[i]/maximum_frequency)*maximum_height
        bar2_height=(hanley_highway_hour_by_hour_vehicle_count[i]/maximum_frequency)*maximum_height
        #Drawing bars        
        canvas.create_rectangle(bar1_x1,y_bottom-bar1_height,bar1_x2,y_bottom,fill="yellow")
        canvas.create_rectangle(bar2_x1,y_bottom-bar2_height,bar2_x2,y_bottom,fill="pink")
        #Labeling the values       
        canvas.create_text(bar1_x1+bar_width/2,y_bottom-bar1_height-15,text=str(elm_avenue_hour_by_hour_vehicle_count[i]))
        canvas.create_text(bar2_x1+bar_width/2,y_bottom-bar2_height-15,text=str(hanley_highway_hour_by_hour_vehicle_count[i]))
        #Labeling hours        
        canvas.create_text(bar1_x1+15+bar_width/2,y_bottom+15,text=hours_lst[i],fill="black")

    root.mainloop()
    

#Task E: Code Loops to Handle multiple csv files
#To loop whole program or stop program
def main():
    while True:
        day,month,year=validate_date_input()
        record=loadData(day,month,year)
        if record:
            hours_lst,elm_avenue_hour_by_hour_vehicle_count,hanley_highway_hour_by_hour_vehicle_count,maximum_frequency,details=process_csv_data(record)
            printing_data(details)
            writing_data(details)
            histogram_draw(hours_lst,elm_avenue_hour_by_hour_vehicle_count,hanley_highway_hour_by_hour_vehicle_count,maximum_frequency,day,month,year)
        else:
            print("No data file found")
            
        
    
        repeat_program=input("Want to run program again (Y/N) ").strip().upper()
        if repeat_program=="Y":
            continue
            
        elif repeat_program=="N":
            print("Program ended")
            break
        else:
            print("Please enter Y or N")

# Run the program
if __name__ == "__main__":
    main()
