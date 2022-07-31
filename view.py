from tkinter import *

root = Tk()
root.title("메모장")
root.geometry("640x480+300+100")
root.resizable(True, True)

# root 안의 frame
frame = Frame(root)
frame.pack(fill="both", expand=True)

# frame 안의 스크롤바
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# frame 안의 텍스트 입력창과 스크롤바 기능 추가
# (yscrollcommand = scrollbar.set 안하면 스크롤이 계속 제자리로 돌아감.)
txt = Text(frame, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

# root 안의 메뉴
menubar = Menu(root)

# 메뉴 기능
def opening():
    with open("memo.txt", "r", encoding="utf8") as memo_file:
        txt.insert(END, memo_file.read()) # 여기서 한참 헤맸네

    
def saving():
    with open("memo.txt", "w", encoding="utf8") as memo_file:
        memo_file.write(txt.get("1.0", END))
        txt.delete("1.0", END)

# 메뉴 파일
menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="열기", command=opening)
menu_file.add_command(label="저장", command=saving)
menu_file.add_command(label="끝내기", command=root.quit)

menubar.add_cascade(label="파일", menu=menu_file)
menubar.add_cascade(label="편집")
menubar.add_cascade(label="서식")
menubar.add_cascade(label="보기")
menubar.add_cascade(label="도움말")


scrollbar.config(command=txt.yview) # 스크롤바와 txt 내용물 연동
root.config(menu=menubar) 
root.mainloop()
