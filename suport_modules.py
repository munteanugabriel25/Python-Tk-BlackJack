#! python3
import random
import tkinter as tk
from tkinter import ttk


class Credit:
    def __init__(self, credit):
        self.credit = credit
        self.bet = 0
    
    def buy_credit(self, amount):
        self.credit += amount
        
    def win_hand(self):
        self.credit += self.bet*2
        self.bet = 0
        
    def lose_hand(self):
        self.bet = 0
        
    def tie_hand(self):
        self.credit += self.bet
        self.bet = 0
        
    def get_credit(self):
        return self.credit
    
    def double_bet(self):
        self.make_bet(self.credit)
        return self.bet
    
    def bett_all(self):
        self.bet = self.credit
        self.credit=0
    
    def make_bet(self, amount):
        self.credit -= amount
        self.bet = amount

    
class Card:
    def __init__(self, value, suit, game_value):
        self.value = value
        self.suit = suit
        self.game_value = game_value
        
        
class DeckCards:
    all_cards = []
    suits = ["Diamond","Heart","Club","Pike"]
    
    def __init__(self):
        """Creating all combinations of cards"""
        self.card_pack =[]
        for num in range(2,15):
            for suit in self.suits:
                if num <= 9:
                    self.all_cards.append(Card(num,suit,num))
                else:
                    self.all_cards.append(Card(num,suit, 10))
    
    def shuffle(self):
        """For each game, this function is accesed. It creates a new pack of cards and then shuffle it."""
        self.card_pack = self.all_cards.copy()
        random.shuffle(self.card_pack)
        
    def deal(self):
        """This function pick last card from card pack and return it"""
        
        if len(self.card_pack) >= 2:
            self.card_pack.pop()
            return  self.card_pack.pop()
        
        


class Hand:
    """This is the Class for player hand and dealer hand"""
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.total = 0
        self.aces = 0
        
            
    def add_card(self,card):
        self.cards.append(card)
        self.calculate_total(card)
        return card.value, card.suit, len(self.cards), self.dealer  # with this info the main module place a card on table. Checking if dealer attribute is true or not and also by sending the no or picked card
    
        
    def show_hidden_card(self): # this function shows dealer hidden card when his turn starts
        if self.dealer:
            return self.cards[1].value, self.cards[1].suit
    
    def get_limit(self):
        if self.dealer:
            return 17
        else:
            return 21
    
    def get_total(self):
        return self.total
    
    def __repr__(self):
        return Hand()
        
    def calculate_total(self,card):
        """ from here aces total are defined"""
        if card.value == 11:
            self.aces += 1
        if card.value < 10:
            self.total += card.value
        else:
            self.total += 10
        if self.total > self.get_limit() and self.aces != 0:
            self.aces -= 1
            self.total -= 9
        if self.dealer:
            player= "dealer"
        else:
            player= "player"
        print( player+ "  Total is :"+ str(self.total))
        print(self.busted())
        
    
    def reset_hand(self): # from here afther a game is over dealer and player attributes are reseted.
        self.cards = []
        self.total = 0
        self.aces = 0
        
    def busted(self): # if one player have a total higher than 21 then he is busted
        if self.total > 21:
            return True
        else:
            return False
        
    def black_jack(self):
        if self.total == 21:
            return True
        else:
            return False
        
class CreditWindow:
    def __init__(self,root):
        self.root = root
        self.create_window()

    def create_window(self):
        self.window= tk.Toplevel(self.root)
        self.window.geometry("200x200+500+500")
        self.display_window()
    
    def display_window(self):
        self.credit_value= tk.IntVar()
        frame = tk.Frame(self.window, width=200, height=200, bd=0)
        
        self.confirm_icon = tk.PhotoImage(file="Images\\confirm_credit_button.png")
        self.cancel_icon = tk.PhotoImage(file="Images\\cancel_credit_button.png")
        self.confirm_over_icon = tk.PhotoImage(file="Images\\confirm_credit_over_button.png")
        self.cancel_over_icon = tk.PhotoImage(file="Images\\cancel_credit_over_button.png")
        self.amount_entry = tk.Entry(frame, width=90,)
        self.canvas = tk.Canvas(frame, width=200, height=200, bd=0, highlightthickness=0, )
        self.confirm_btn_label= tk.Label(frame, width=82, height=28, text ="confirm", image=self.confirm_icon, anchor="nw", bd=0)
        self.cancel_btn_label= tk.Label(frame, width=82, height=28, text="cancel", image=self.cancel_icon, anchor="nw", bd=0)
       
        
        self.amount_entry = ttk.Entry(frame, width=13)
        self.canvas.create_window(105, 74, window=self.amount_entry, anchor="nw")
        self.canvas.create_text(10, 70, text="Enter amount ", font=("Futura Medium Condensed BT", 15), fill="#6D6E70", anchor="nw")
        self.canvas.create_text(66, 23, text="Buy Credit ", font=("Futura Medium Condensed BT", 17), fill="#6D6E70", anchor="nw")
        self.canvas.create_window(8, 110, window=self.confirm_btn_label, anchor="nw")
        self.canvas.create_window(108, 110, window=self.cancel_btn_label, anchor="nw")
        
        
        self.confirm_btn_label.bind("<Enter>", self.mouse_in)
        self.cancel_btn_label.bind("<Enter>", self.mouse_in)
        self.confirm_btn_label.bind("<Leave>", self.mouse_out)
        self.cancel_btn_label.bind("<Leave>", self.mouse_out)

        self.confirm_btn_label.bind("<Button-1>", self.confirm)
        self.cancel_btn_label.bind("<Button-1>", self.close)
        
        frame.place(x=0, y=0, anchor="nw")
        self.canvas.place(x=0, y=0, anchor="nw")
    
    def show_message(self, message,close=False):
        self.canvas.create_text(100,160 , text=message, font=("Futura Medium Condensed BT", 14), fill="#6D6E70", anchor="center", tags="message")
        self.canvas.after(1000, lambda : self.canvas.delete("message"))
        if close:
            self.canvas.after(1500, lambda :self.close(event=None)) #when action completed automatically close credit window
        
    def mouse_out(self, event):
        event_dict= {"confirm": self.confirm_icon,
                     "cancel": self.cancel_icon}
        
        if event.widget.cget("text") in event_dict.keys():
            name = event_dict[event.widget.cget("text")]
            event.widget.configure(image=name)
    
        
    def mouse_in(self, event):
        event_dict = {"confirm": self.confirm_over_icon,
                      "cancel": self.cancel_over_icon}
        if event.widget.cget("text") in event_dict.keys():
            name = event_dict[event.widget.cget("text")]
            event.widget.configure(image=name)
            
    def confirm(self,event):
        """checking if amount is only numbers and then returns to main window de amount"""
        try:
            value= int(self.amount_entry.get())
            self.amount_entry.delete(0, tk.END)
            self.show_message("Done, credit added!", close=True)
            self.credit_value.set(value)
        
        except ValueError: # if amount can not be represented as an INT the the entry widget contect is cleared
            self.amount_entry.delete(0, tk.END)
            self.show_message("           Error!\nEnter numeric value!")
            
    def update_credit(self):
        pass
    
    def close(self,event):
        self.window.destroy()
        
        