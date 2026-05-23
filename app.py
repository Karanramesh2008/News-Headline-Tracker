import threading
import time
import scraper
import storage
import display
headlines=[]
v='1.0.1'
def auto_refresh():
    global headlines
    while True:
        headlines=scraper.get_headlines()
        time.sleep(30)

def main():
    global headlines
    t=threading.Thread(target=auto_refresh,daemon=True)
    t.start()

    time.sleep(4)
    while True:
        try:
            print("="*45) 
            print("\tNews Tracker")
            print("="*45,'\n')
            print("1. View Headlines")
            print("2. Search Headlines")
            print("3. Save a Headlines")
            print("4. View Saved Headlines")
            print("5. Delete from Saved")
            print("6. Quit\n")
            
            i=int(input("Enter your Choice: "))
            if i==1:
                display.show_headlines(headlines)
            elif i==2:
                d=input("Enter the keyword to search: ")
                x=scraper.search(headlines,d)
                display.show_headlines(x,"Searched Headlines")
            elif i==3:
                d=input("Enter the headline to save: ")
                s=scraper.search(headlines,d)
                if not s:
                    print("No headlines found")
                    return
                if len(s)>1:
                    display.show_headlines(s)
                    xd=int(input("Enter the number to save: "))-1
                    storage.save_headlines(s[xd])
                if len(s)==1:
                    storage.save_headlines(s[0])

            elif i==4:
                w=storage.load_headlines()
                display.show_headlines(w,"Saved Headlines")
            elif i==5:
                d=input("Enter the headline to delete: ")
                w=storage.load_headlines()
                s=scraper.search(w,d)
                if not s:
                    print("No headlines found")
                    return
                if len(s)>1:
                    display.show_headlines(s)
                    xd=int(input("Enter the number to delete: "))-1
                    storage.delete_headlines(s[xd])
                if len(s)==1:
                    storage.delete_headlines(s[0])
            elif i==6:
                print("Thank you for using our App")
                print(f"Version: {v}")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please Enter Valid Choice.")

if __name__=="__main__":
    main()