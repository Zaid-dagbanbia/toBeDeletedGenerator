
import tkinter
import unicodecsv as csv
import tkinter.messagebox


def read_csv(filename):
    with open(filename,'rb',) as f:
        
         reader = csv.DictReader(f)
         return list(reader)


#Define function to select unique entm
        
def get_unique_entm(data):
    unique_products = []
    for data_point in data:
        number = data_point['Number']
        year = data_point['Year']
        unique_products.append((number,year))
    return unique_products

#Reading old csv
oldweek = read_csv('oldEntm.csv')

#Reading new csv
newweek = read_csv('newEntm.csv')

#Unique new entm
unique_new = get_unique_entm(newweek)

#unique old entm
unique_old = get_unique_entm(oldweek)

deletedEntm = []
for entm in unique_old:
    if entm not in unique_new:
        deletedEntm.append(entm)
        



def tobeDeleted():
    with open("tobeDeleted.csv", "w") as out_file:
        print("The total entm to be deleted : " + str(len(deletedEntm)))
        # creating a simple alert box
        tkinter.messagebox.showinfo("Alert Message", "tobeDeleted.csv file is generated!")
        for i in range(len(deletedEntm)):
            ntmValue = deletedEntm[i][0]
            ntmYear  = deletedEntm[i][1]
            outString = " "
            outString += ntmValue + "," + ntmYear + "," + "CN"
            outString += "\n"
            out_file.write(outString)





# creating basic window
#window = Tk()
window = tkinter.Tk()
window.geometry("312x324") # size of the window width:- 500, height:- 375
window.resizable(1, 1) # this prevents from resizing the window
window.title("Enforment Detector")
tkinter.Button(window, text = "Generate ToBeDeleted Entm List",fg = "red", command = tobeDeleted).pack()


window.mainloop()
