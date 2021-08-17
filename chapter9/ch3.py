import csv

list_of_lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("anwser.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=",")
    for an_list in list_of_lists:
        writer.writerow(an_list)
