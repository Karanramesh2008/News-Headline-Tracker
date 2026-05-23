import scraper
def show_headlines(head: list, title: str = "Latest Headlines"):
    print('='*30,title,'='*30)
    if not head:
        print("No headlines found")
        return
    for i,a in enumerate(head,start=1):
        print(f"{i}. {a}.")
    pass




