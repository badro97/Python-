
# 맨몸운동 프로그램 
# 2020-7-21  ..ver.1
# 죄수운동법 - https://www.youtube.com/watch?v=Z0Z8_lVFkjk

import sys
import random
import time
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication
from testUI import Ui_MainWindow


class mainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.push_up_reps = []
        self.card_deck = []
        self.burp_reps = []
        

        self.start_day = datetime.strptime("2020-7-21", "%Y-%m-%d") # 운동 시작일 입력
        self.d_today = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), "%Y-%m-%d")


        self.s = ["월", "화", "수", "목", "금", "토", "일"]
        self.h = ["상체", "하체", "전신", "휴식"]
        
        self.log_text(self.s[datetime.today().weekday()] + "요일")
        self.log_text("운동 " + str((self.d_today - self.start_day).days + 1) + "일 째")
        self.log_text(" ")
        self.log_text(self.h[(self.d_today - self.start_day).days % 4])
        self.log_text(" ")
        
        
        self.WOCheck()
        
        
        
    def WOCheck(self):
        if self.h[(self.d_today - self.start_day).days % 4] == "상체":
            self.log_text("푸쉬업\n1세트 최대 횟수를 입력하세요")
            self.input_button.clicked.connect(self.push_up)
            self.switch = 1
            # 풀업 추가하기
            
        elif self.h[(self.d_today - self.start_day).days % 4] == "하체":
            self.log_text("Deck of pain rep\n")
            self.log_text("J, Q, K, Joker = 10\nA = 11")
            self.deck()
            self.switch = 2
        
        elif self.h[(self.d_today - self.start_day).days % 4] == "전신":
            self.log_text("버피테스트")
            self.log_text("\n최대 가능 횟수를 입력하세요")
            self.input_button.clicked.connect(self.burpee)
            self.switch = 3
        
        elif self.h[(self.d_today - self.start_day).days % 4] == "휴식":
            self.log_text("휴 . 식")
        
        
    def log_text(self, msg):
        self.text.append(msg)


    def go(self):  
        if self.switch == 1:   # 상체
            self.text.clear()
            self.log_text("\n\n")
            self.log_text(str(self.push_up_reps.pop()) + " 개")
 

        elif self.switch == 2: # 하체
            self.text.clear()
            self.log_text("\n")
            self.log_text(str(self.card_deck.pop()) + "\n\n" + str(len(self.card_deck)) + " reps 남음")
            self.log_text("\n♥, ◆ = Squat\n♧(R), ♤(L) = Lunge")
            
        else:                  # 전신
            self.text.clear()
            self.log_text("\n")
            self.log_text(str(self.burp_reps.pop()) + " 개")
            self.log_text("\n3 걸음 걷고 바로 다음 set go!")
        
        
    def push_up(self):
        num = self.edit.toPlainText()
        cnt = 0
        try:
            n = int(num)
        except:
            print("error")
            
        for i in range(1, n +1):
            if i % 2 == 0: # 짝수 세트
                cnt += 1
                self.push_up_reps.append(cnt)
            else:          # 홀수 세트
                self.push_up_reps.append(n - cnt)
        
        self.push_up_reps.reverse()
        while self.push_up_reps:
            self.go_button.clicked.connect(self.go)
            break
    
    
    def deck(self):
        shape = '♥◆♤♧'
        num = []
        for i in range(2, 11):
            num.append(i)
        for k in 'JQKA':
            num.append(k)

        for shapes in shape:
            for nums in num:
                self.card_deck.append((shapes, nums))

        self.card_deck.append(('Joker', '★'))
        self.card_deck.append(('Joker', '☆'))
            
        random.shuffle(self.card_deck)
        while self.card_deck:
            self.go_button.clicked.connect(self.go)
            break
        
        
    def burpee(self):
        num = self.edit.toPlainText()
        try:
            n = int(num)
        except:
            print("error")
            
        for i in range(1, n + 1):
            self.burp_reps.append(i)
            if i == n:
                for j in range(n - 1, 0, -1):
                    self.burp_reps.append(j)
                    
        while self.burp_reps:
            self.go_button.clicked.connect(self.go)
            break   
        """
        초보자 15분
        중급자 12분
        상급자 10분
        """
        
        
app = QApplication(sys.argv)
main_window = mainWindow()
main_window.show()
app.exec_()
