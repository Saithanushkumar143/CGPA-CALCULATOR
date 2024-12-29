from tkinter import *
from tkinter import simpledialog, messagebox


char_to_num = {'s': 10, 'a': 9, 'b': 8, 'c': 7, 'd': 6, 'e': 5, 'f': 0}


r = Tk()
r.withdraw()


j = simpledialog.askinteger("Input", "Enter the number of Subjects:", minvalue=1)
if not j:
    messagebox.showerror("Error", "Number of Subjects is required!")
    r.destroy()
    exit()

r.deiconify()  
r.title("CGPA Calculator")


def clear_all():
    for entry1,entry2 in entries:
        entry1.delete(0,END)
        entry2.delete(0,END)
        result.set("Result will appear here.")

def calculate_sums():
    try:
        total_sum = 0
        total_credits = 0
        results = []
        
        for i in range(j):  
            val1 = entries[i][0].get().strip().lower()  
            val2 = entries[i][1].get().strip().lower()
            
            
            num1 = char_to_num.get(val1)  
            num2 = char_to_num.get(val2)  
            

            if num1 is None:
                try:
                    num1 = float(val1)
                except ValueError:
                    result.set(f"Invalid input in Subject {i + 1}: {val1}")
                    return
            
            if num2 is None:
                try:
                    num2 = float(val2)
                except ValueError:
                    result.set(f"Invalid input in Subject {i + 1}: {val2}")
                    return
            
           
            set_sum = num1 * num2
            total_sum += set_sum
            total_credits += num2
            
       
        if total_credits == 0:
            result.set("Total credits cannot be zero.")
            return
        
       
        average_cgpa = total_sum / total_credits
        def review():
            if average_cgpa >= 9 :
                return "Congratulations bro ,party🎉🎉"
            elif average_cgpa >=8 and average_cgpa <9:
                return "Well done,Keep working hard 🫣🫣"
            elif average_cgpa >= 7 and average_cgpa<8:
                return "Need to work hard darling 💪💪"
            elif average_cgpa >=5 and average_cgpa<7:
                return "Need to concentrate on Studies"
            else:
                return "I'm Sorry \n You have Failed in the exam"
        results.append(f"Average CGPA: {average_cgpa:.2f} \n{review()}")
        result.set("\n".join(results))
    except Exception as e:
        result.set(f"Error: {str(e)}")

        
        

heading = Label(r, text="CGPA CALCULATOR", font=("Arial", 16), bg="pink", fg="dark blue")
heading.grid(row=0, column=0, columnspan=3, pady=10)


entries = []
for i in range(j):  
    Label(r, text=f"SUBJECT {i + 1}:").grid(row=i + 4, column=0, pady=5)
    entry1 = Entry(r, width=10, bg="gold", fg="navy blue")
    entry1.grid(row=i + 4, column=1, pady=5)
    entry2 = Entry(r, width=10, bg="gold", fg="navy blue")
    entry2.grid(row=i + 4, column=2, pady=5)
    entries.append((entry1, entry2))


result = StringVar()
result.set("Result will appear here.")

Label(r, text = "GRADE").grid(row=1, column=1, pady=5)
Label(r, text = "CREDITS").grid(row=1,column=2, pady=5)
Label(r, textvariable=result,bg="white",fg = "black").grid(row=j + 5, column=0, columnspan=3, pady=10)


Button(r, text="Calculate", command=calculate_sums, bg="navy blue", fg="gold").grid(row=j + 6, column=0, columnspan=3, pady=10)
Button(r,text="Clear",command=clear_all, bg="navy blue", fg="gold").grid(row=j+6,column=2,columnspan=3,pady=10)


r.mainloop()
