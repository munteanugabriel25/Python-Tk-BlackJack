import tkinter as tk
from suport_modules import DeckCards
from suport_modules import Hand
from sound_module import Sound
from suport_modules import Credit
from suport_modules import CreditWindow
import os


# player cards position (1-376*322 , 2-446*322, 3-516*322, 4-586*322)
# dealer cards position (1-376*156 , 2-446*156, 3-516*322, 4-586*322)

class GUI:
    dealer_slots_position = {0: (446, 156), 1: (516, 156), 2: (582, 156), 3: (602, 188), 4: (622, 220),
                             5: (642, 252)}  # this are x, y coordinates for DEALER cards on table
    player_slots_position = {0: (446, 322), 1: (516, 322), 2: (582, 285), 3: (602, 314), 4: (622, 346),
                             5: (642, 378)}  # this are x, y coordinates for PLAYER cards on table
    player_split_slots_position = {0: (446, 322), 1: (516, 322), 2: (582, 285), 3: (602, 314), 4: (622, 346), 5: (
    642, 378)}  # this are x, y coordinates for PLAYER cards on table when chooses to play SPLIT
    player_slots = []
    dealer_slots = []
    
    def __init__(self, player_hand, dealer_hand, deck_card, sound, player_credit):
        self.deck_card = deck_card
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
        self.sound = sound
        self.player_credit = player_credit
        self.root = tk.Tk()
        self.root.geometry("1000x700")
        self.create_menu_bar()
        self.create_game_table()
        
        self.create_table_slots()
        self.root.mainloop()
    
    def create_game_table(self):
        self.bet_info = tk.StringVar()
        self.bet_info.set(self.bet_value.get())
        frame = tk.Frame(self.root, width=1000, height=550, bd=0)
        self.background_table_image = tk.PhotoImage(file="Images\\table_design.gif")
        self.pop_message_icon = tk.PhotoImage(file="Images\\message_pop_icon.png")
        self.chip_ontable_icon = tk.PhotoImage(file="Images\\chip_on-tablet_icon.png")
        self.winner_message_icon = tk.PhotoImage(file="Images\\winner_icon.png")
        
        self.game_table_canvas = tk.Canvas(frame, width=1000, height=550, bd=0, highlightthickness=0)
        self.game_table_canvas.create_image(0, 0, image=self.background_table_image, anchor="nw")
        self.game_table_canvas.create_text(50, 50, text=self.bet_info.get(), anchor="ne",
                                           font=("Futura Medium Condensed BT", 17), fill="white")
        
        frame.place(x=0, y=0, anchor="nw")
        self.game_table_canvas.place(x=0, y=0, anchor="nw")
    
    def create_menu_bar(self):
        self.bet_value = tk.IntVar()
        self.bet_value.set(0)
        self.bet_placed = tk.BooleanVar()
        self.bet_placed.set(False)
        self.double_bet = tk.BooleanVar()
        self.double_bet.set(False)
        self.player_name = tk.StringVar()
        
        self.frame = tk.Frame(self.root, width=1000, height=150, bd=0)
        
        self.background_menu_image = tk.PhotoImage(file="Images\\menu_design.gif")
        
        self.black_chip = tk.PhotoImage(file="Images\\black_chip.gif")
        self.black_chip_over = tk.PhotoImage(file="Images\\black_chip_over.gif")
        self.red_chip = tk.PhotoImage(file="Images\\red_chip.gif")
        self.red_chip_over = tk.PhotoImage(file="Images\\red_chip_over.gif")
        self.yellow_chip = tk.PhotoImage(file="Images\\yellow_chip.gif")
        self.yellow_chip_over = tk.PhotoImage(file="Images\\yellow_chip_over.gif")
        self.blue_chip = tk.PhotoImage(file="Images\\blue_chip.gif")
        self.blue_chip_over = tk.PhotoImage(file="Images\\blue_chip_over.gif")
        self.green_chip = tk.PhotoImage(file="Images\\green_chip.gif")
        self.green_chip_over = tk.PhotoImage(file="Images\\green_chip_over.gif")
        
        self.bet_all_button = tk.PhotoImage(file="Images\\bet_all_button.gif")
        self.bet_all_over_button = tk.PhotoImage(file="Images\\bet_all_over_button.gif")
        self.reset_bet_button = tk.PhotoImage(file="Images\\reset_bet_button.gif")
        self.reset_bet_over_button = tk.PhotoImage(file="Images\\reset_bet_over_button.gif")
        self.place_bet_button = tk.PhotoImage(file="Images\\place_bet_button.gif")
        self.place_bet_over_button = tk.PhotoImage(file="Images\\place_bet_over_button.gif")
        
        self.hit_button = tk.PhotoImage(file="Images\\hit_button.gif")
        self.hit_over_button = tk.PhotoImage(file="Images\\hit_over_button.gif")
        self.stand_button = tk.PhotoImage(file="Images\\stand_button.gif")
        self.stand_over_button = tk.PhotoImage(file="Images\\stand_over_button.gif")
        self.split_button = tk.PhotoImage(file="Images\\split_button.gif")
        self.split_over_button = tk.PhotoImage(file="Images\\split_over_button.gif")
        self.double_button = tk.PhotoImage(file="Images\\double_button.gif")
        self.double_over_button = tk.PhotoImage(file="Images\\double_over_button.gif")
        
        self.buy_credit_button = tk.PhotoImage(file="Images\\buy_credit_button.png")
        self.buy_credit_over_button = tk.PhotoImage(file="Images\\buy_credit_over_button.png")
        self.withdraw_credit_button = tk.PhotoImage(file="Images\\withdraw_credit_button.png")
        self.withdraw_credit_over_button = tk.PhotoImage(file="Images\\withdraw_credit_over_button.png")
        
        self.sound_button = tk.PhotoImage(file="Images\\sound_button.png")
        self.sound_over_button = tk.PhotoImage(file="Images\\sound_over_button.png")
        self.mute_sound_button = tk.PhotoImage(file="Images\\mute_sound_button.png")
        self.settings_button = tk.PhotoImage(file="Images\\settings_button.png")
        self.settings_over_button = tk.PhotoImage(file="Images\\settings_over_button.png")
        self.quit_button = tk.PhotoImage(file="Images\\quit_button.png")
        self.quit_over_button = tk.PhotoImage(file="Images\\quit_over_button.png")
        self.user_button = tk.PhotoImage(file="Images\\user_button.png")
        self.user_over_button = tk.PhotoImage(file="Images\\user_over_button.png")
        
        self.menu_canvas = tk.Canvas(self.frame, width=1000, height=150, bd=0, highlightthickness=0)
        self.black_chip_label = tk.Label(self.frame, width=43, height=46, text="black_chip", image=self.black_chip,
                                         bd=0)
        self.red_chip_label = tk.Label(self.frame, width=43, height=46, text="red_chip", image=self.red_chip, bd=0)
        self.yellow_chip_label = tk.Label(self.frame, width=43, height=46, text="yellow_chip", image=self.yellow_chip,
                                          bd=0)
        self.blue_chip_label = tk.Label(self.frame, width=43, height=46, text="blue_chip", image=self.blue_chip, bd=0)
        self.green_chip_label = tk.Label(self.frame, width=43, height=46, text="green_chip", image=self.green_chip,
                                         bd=0)
        
        self.bett_all_label = tk.Label(self.frame, width=82, height=28, text="bet_all", image=self.bet_all_button, bd=0)
        self.reset_bet_label = tk.Label(self.frame, width=82, height=28, text="reset_bet", image=self.reset_bet_button,
                                        bd=0)
        self.place_bet_label = tk.Label(self.frame, width=82, height=28, text="place_bet", image=self.place_bet_button,
                                        bd=0)
        
        self.hit_bet_label = tk.Label(self.frame, width=82, height=28, text="hit_bet", image=self.hit_button, bd=0)
        self.stand_bet_label = tk.Label(self.frame, width=82, height=28, text="stand_bet", image=self.stand_button,
                                        bd=0)
        self.split_bet_label = tk.Label(self.frame, width=82, height=28, text="split_bet", image=self.split_button,
                                        bd=0)
        self.double_bet_label = tk.Label(self.frame, width=82, height=28, text="double_bet", image=self.double_button,
                                         bd=0)
        
        self.buy_credit_label = tk.Label(self.frame, width=82, height=28, text="buy_credit",
                                         image=self.buy_credit_button, bd=0)
        self.withdraw_credit_label = tk.Label(self.frame, width=82, height=28, text="withdraw_credit",
                                              image=self.withdraw_credit_button, bd=0)
        
        self.mute_label = tk.Label(self.frame, width=26, height=26, text="mute", image=self.sound_button, bd=0)
        self.settings_label = tk.Label(self.frame, width=26, height=26, text="settings", image=self.settings_button,
                                       bd=0)
        self.quit_label = tk.Label(self.frame, width=26, height=26, text="quit", image=self.quit_button, bd=0)
        self.user_label = tk.Label(self.frame, width=26, height=26, text="user", image=self.user_button, bd=0)
        
        self.menu_canvas.create_image(0, 0, image=self.background_menu_image, anchor="nw")
        self.menu_canvas.create_window(727, 30, window=self.black_chip_label, anchor="nw")
        self.menu_canvas.create_window(837, 30, window=self.red_chip_label, anchor="nw")
        self.menu_canvas.create_window(947, 30, window=self.yellow_chip_label, anchor="nw")
        self.menu_canvas.create_window(891, 51, window=self.blue_chip_label, anchor="nw")
        self.menu_canvas.create_window(781, 51, window=self.green_chip_label, anchor="nw")
        self.menu_canvas.create_window(911, 113, window=self.bett_all_label, anchor="nw")
        self.menu_canvas.create_window(816, 113, window=self.reset_bet_label, anchor="nw")
        self.menu_canvas.create_window(721, 113, window=self.place_bet_label, anchor="nw")
        
        self.menu_canvas.create_window(353, 66, window=self.hit_bet_label, anchor="nw")
        self.menu_canvas.create_window(442, 66, window=self.stand_bet_label, anchor="nw")
        self.menu_canvas.create_window(529, 66, window=self.split_bet_label, anchor="nw")
        self.menu_canvas.create_window(614, 66, window=self.double_bet_label, anchor="nw")
        
        self.menu_canvas.create_window(24, 113, window=self.buy_credit_label, anchor="nw")
        self.menu_canvas.create_window(214, 113, window=self.withdraw_credit_label, anchor="nw")
        
        self.menu_canvas.create_window(24, 30, window=self.mute_label, anchor="nw")
        self.menu_canvas.create_window(64, 30, window=self.settings_label, anchor="nw")
        self.menu_canvas.create_window(104, 30, window=self.quit_label, anchor="nw")
        self.menu_canvas.create_window(144, 30, window=self.user_label, anchor="nw")
        
        self.canvas_bet_text = self.menu_canvas.create_text(679, 114, text=self.bet_value.get(), anchor="ne",
                                                            font=("Futura Medium Condensed BT", 17), fill="white")
        self.credit_balance_text = self.menu_canvas.create_text(525, 114, text=self.player_credit.get_credit(),
                                                                anchor="ne", font=("Futura Medium Condensed BT", 17),
                                                                fill="white")
        
        self.frame.place(x=0, y=550, anchor="nw")
        self.menu_canvas.place(x=0, y=0, anchor="nw")
        
        self.black_chip_label.bind("<Enter>", self.mouse_over)
        self.red_chip_label.bind("<Enter>", self.mouse_over)
        self.yellow_chip_label.bind("<Enter>", self.mouse_over)
        self.blue_chip_label.bind("<Enter>", self.mouse_over)
        self.green_chip_label.bind("<Enter>", self.mouse_over)
        
        self.bett_all_label.bind("<Enter>", self.mouse_over)
        self.reset_bet_label.bind("<Enter>", self.mouse_over)
        self.place_bet_label.bind("<Enter>", self.mouse_over)
        
        self.hit_bet_label.bind("<Enter>", self.mouse_over)
        self.stand_bet_label.bind("<Enter>", self.mouse_over)
        self.split_bet_label.bind("<Enter>", self.mouse_over)
        self.double_bet_label.bind("<Enter>", self.mouse_over)
        
        self.buy_credit_label.bind("<Enter>", self.mouse_over)
        self.withdraw_credit_label.bind("<Enter>", self.mouse_over)
        
        self.mute_label.bind("<Enter>", self.mouse_over)
        self.settings_label.bind("<Enter>", self.mouse_over)
        self.quit_label.bind("<Enter>", self.mouse_over)
        self.user_label.bind("<Enter>", self.mouse_over)
        
        self.black_chip_label.bind("<Leave>", self.mouse_out)
        self.red_chip_label.bind("<Leave>", self.mouse_out)
        self.yellow_chip_label.bind("<Leave>", self.mouse_out)
        self.blue_chip_label.bind("<Leave>", self.mouse_out)
        self.green_chip_label.bind("<Leave>", self.mouse_out)
        
        self.bett_all_label.bind("<Leave>", self.mouse_out)
        self.reset_bet_label.bind("<Leave>", self.mouse_out)
        self.place_bet_label.bind("<Leave>", self.mouse_out)
        
        self.hit_bet_label.bind("<Leave>", self.mouse_out)
        self.stand_bet_label.bind("<Leave>", self.mouse_out)
        self.split_bet_label.bind("<Leave>", self.mouse_out)
        self.double_bet_label.bind("<Leave>", self.mouse_out)
        
        self.buy_credit_label.bind("<Leave>", self.mouse_out)
        self.withdraw_credit_label.bind("<Leave>", self.mouse_out)
        
        self.mute_label.bind("<Leave>", self.mouse_out)
        self.settings_label.bind("<Leave>", self.mouse_out)
        self.quit_label.bind("<Leave>", self.mouse_out)
        self.user_label.bind("<Leave>", self.mouse_out)
        
        self.black_chip_label.bind("<Button-1>", self.set_bet_amount)
        self.red_chip_label.bind("<Button-1>", self.set_bet_amount)
        self.yellow_chip_label.bind("<Button-1>", self.set_bet_amount)
        self.blue_chip_label.bind("<Button-1>", self.set_bet_amount)
        self.green_chip_label.bind("<Button-1>", self.set_bet_amount)
        
        self.place_bet_label.bind("<Button-1>", self.make_bet)
        self.reset_bet_label.bind("<Button-1>", self.reset_bet_amount)
        self.bett_all_label.bind("<Button-1>", self.bet_all_amount)
        self.double_bet_label.bind("<Button-1>", self.double_action)
        
        self.hit_bet_label.bind("<Button-1>", self.hit_action)
        self.stand_bet_label.bind("<Button-1>", self.stand_action)
        
        self.mute_label.bind("<Button-1>", self.mute_unmute_sound)
        # self.settings_label.bind("<Leave>", self.mouse_out)
        self.quit_label.bind("<Button-1>", self.quit)
        # self.user_label.bind("<Leave>", self.mouse_out)
        self.buy_credit_label.bind("<Button-1>", self.buy_credit)
        self.withdraw_credit_label.bind("<Button-1>", self.withdraw_credit)
    
    def create_table_slots(self):
        """with this function all player and dealer slots  are created. Each time a card is placed on the table a slot image file path will be changed with
        picked up card."""
        
        for slot in range(
                6):  # this creates image class for all slots. With this object we will change cards on table for player and dealer
            slot = tk.PhotoImage(file="")
            self.player_slots.append(slot)
        for slot in range(
                6):  # this creates image class for all slots. With this object we will change cards on table for player and dealer
            slot = tk.PhotoImage(file="")
            self.dealer_slots.append(slot)
        
        for index, image_slot in enumerate(
                self.player_slots):  # from here empty images are placed on the game table design
            # print(index)
            self.game_table_canvas.create_image(self.player_slots_position[index][0],
                                                self.player_slots_position[index][1], image=image_slot, anchor="nw",
                                                tags="slot")
        
        for index, image_slot in enumerate(
                self.dealer_slots):  # from here empty images are placed on the game table design
            self.game_table_canvas.create_image(self.dealer_slots_position[index][0],
                                                self.dealer_slots_position[index][1], image=image_slot, anchor="nw",
                                                tags="slot")
    
    def reset_table_slots(self, event=None):
        "afther game ending, before starting another game all slots should be cleared for card images"
        self.game_table_canvas.delete("slot")
        self.player_slots.clear()
        self.dealer_slots.clear()
    
    def mouse_over(self, event):
        """function for mouse over binding for all labels """
        event_dict = {"black_chip": self.black_chip_over, "red_chip": self.red_chip_over,
                      "yellow_chip": self.yellow_chip_over, "blue_chip": self.blue_chip_over,
                      "green_chip": self.green_chip_over, "bet_all": self.bet_all_over_button,
                      "reset_bet": self.reset_bet_over_button,
                      "place_bet": self.place_bet_over_button, "hit_bet": self.hit_over_button,
                      "split_bet": self.split_over_button, "double_bet": self.double_over_button,
                      "stand_bet": self.stand_over_button,
                      "buy_credit": self.buy_credit_over_button, "withdraw_credit": self.withdraw_credit_over_button,
                      "mute": self.sound_over_button, "settings": self.settings_over_button,
                      "quit": self.quit_over_button, "user": self.user_over_button}
        
        if event.widget.cget("text") in event_dict.keys():
            name = event_dict[event.widget.cget("text")]
            event.widget.configure(image=name)
    
    def mouse_out(self, event):
        """function for mouse out binding for all labels """
        event_dict = {"black_chip": self.black_chip, "red_chip": self.red_chip, "yellow_chip": self.yellow_chip,
                      "blue_chip": self.blue_chip, "green_chip": self.green_chip, "bet_all": self.bet_all_button,
                      "reset_bet": self.reset_bet_button,
                      "place_bet": self.place_bet_button, "hit_bet": self.hit_button, "split_bet": self.split_button,
                      "double_bet": self.double_button, "stand_bet": self.stand_button,
                      "buy_credit": self.buy_credit_button, "withdraw_credit": self.withdraw_credit_button,
                      "mute": self.sound_button, "settings": self.settings_button, "quit": self.quit_button,
                      "user": self.user_button}
        if event.widget.cget("text") in event_dict.keys():
            name = event_dict[event.widget.cget("text")]
            event.widget.configure(image=name)
    
    def set_bet_amount(self, event):
        """from here bet amount is setted by clicking on chip widget from main window"""
        chip_values = {"black_chip": 5, "red_chip": 10, "yellow_chip": 25, "blue_chip": 50, "green_chip": 100}
        dict_key = event.widget.cget("text")
        value = chip_values[dict_key]
        self.bet_value.set(self.bet_value.get() + value)
        self.menu_canvas.itemconfig(self.canvas_bet_text, text=self.bet_value.get())
    
    def reset_bet_amount(self, event=None):
        """from here bet amount is reseted to amount of 0"""
        self.bet_value.set(0)
        self.menu_canvas.itemconfig(self.canvas_bet_text, text=self.bet_value.get())
    
    def show_winner_message(self, message):
        """after each ending hand on table, this message is shown with info about winner and lose/win amount"""
        self.game_table_canvas.create_image(385, 230, image=self.winner_message_icon, anchor="nw",
                                            tags="winner-message")
        self.game_table_canvas.create_text(435, 239, text=message, anchor="nw", font=("Futura Medium Condensed BT", 16),
                                           fill="white", tags="winner-message")
        self.game_table_canvas.after(2500, lambda: self.game_table_canvas.delete("winner-message"))
    
    def show_dealer_message(self, message):
        """ this function shows a dealer message info on main window"""
        self.game_table_canvas.create_image(600, 10, image=self.pop_message_icon, anchor="nw", tags="dealer-message")
        self.game_table_canvas.create_text(610, 12, text=message, font=("Futura Medium Condensed BT", 15),
                                           fill="black", anchor="nw", tags="dealer-message")
        self.game_table_canvas.after(1500, lambda: self.game_table_canvas.delete("dealer-message"))
    
    def bet_all_amount(self, event):
        self.bet_value.set(self.player_credit.double_bet())
        self.menu_canvas.itemconfig(self.canvas_bet_text, text=self.bet_value.get())
        
    def make_bet(self, event):
        """from here the bet is placed. Also check's if a bet is allready made"""
        if not self.bet_placed.get():  # if a bet has not been made, you can bet another amount
            self.deck_card.shuffle()
            if self.bet_value.get() != 0:  # check if the bet is higher than 0
                if self.bet_value.get() <= self.player_credit.get_credit():  # check if the bet is lower or equal than player total amount
                    self.sound.play_sound("chips")
                    message = "Bet placed! \nDealling cards."
                    self.bet_placed.set(True)
                    self.show_dealer_message(message)  # a message from dealer is showed that every thing is fine
                    self.game_table_canvas.create_image(699, 243, image=self.chip_ontable_icon, anchor="nw",
                                                        tags="chips-on-table")  # a set of chips (a picture) is placed on the game table
                    self.player_credit.make_bet(self.bet_value.get())
                    self.update_credit()
                    self.reset_bet_amount()  # bet amount is reseted from main menu window
                    self.first_hand()  # start to hand out cards
                else:
                    message = "Insufficient funds\n for this bet."
                    self.sound.play_sound("error")
                    self.show_dealer_message(message)
            else:
                message = "You can't bet 0$"
                self.sound.play_sound("error")
                self.show_dealer_message(message)
        
        else:  # if a bet has been made, you can't change it
            message = "You can't make \n another bet."
            self.sound.play_sound("error")
            self.show_dealer_message(message)
    
    def place_cards_on_table(self,
                             info):  # info consists into a tuple with following info : card value, suit, hand lenght, dealer True/False
        """This function place cards on table depending some parameters like dealer, hand lenght """
        picture_name = str(info[0]) + "." + str(info[1]) + ".png"
        cards_folder = "Images\\Cards"
        card_position = info[2] - 1
        if not info[3]:  # if it's a player card
            self.player_slots[card_position].configure(file=os.path.join(cards_folder, picture_name))
        else:  # if it's a dealer card
            if info[2] == 2:  # if it's dealer second card, dont show it's value. Place a card face down.
                self.dealer_slots[card_position].configure(file="Images\\card_black.png")
            else:
                self.dealer_slots[card_position].configure(file=os.path.join(cards_folder, picture_name))
    
    def first_hand(self):
        """what happens next when a bet is placed from player."""
        self.double_bet.set(True)
        self.game_table_canvas.after(1000, lambda: self.sound.play_sound("dealing-cards"))
        self.game_table_canvas.after(1000, lambda: self.place_cards_on_table(
            self.player_hand.add_card(self.deck_card.deal())))  # time delay according to sound effect
        self.game_table_canvas.after(1600, lambda: self.place_cards_on_table(
            self.dealer_hand.add_card(self.deck_card.deal())))  # time delay according to sound effect
        self.game_table_canvas.after(2000, lambda: self.place_cards_on_table(
            self.player_hand.add_card(self.deck_card.deal())))  # time delay according to sound effect
        self.game_table_canvas.after(2300, lambda: self.place_cards_on_table(
            self.dealer_hand.add_card(self.deck_card.deal())))  # time delay according to sound effect
    
    def hit_action(self, event):
        """what happens when player choose to hit a new card"""
        
        if self.bet_placed.get() and not self.player_hand.busted():  # check if a bet is placed and if player hand si not busted
            self.game_table_canvas.after(500, lambda: self.place_cards_on_table(
                self.player_hand.add_card(self.deck_card.deal())))  # time delay according to sound effect
            message = "Player asked for\n another card."
            self.show_dealer_message(message)
            self.sound.play_sound("card-flip")
            self.game_table_canvas.after(1400, lambda: self.check_player_busted())
        
        
        else:
            message = "Action not \n allowed."
            self.sound.play_sound("error")
            self.show_dealer_message(message)
    
    def stand_action(self, event):
        if self.bet_placed.get() and not self.player_hand.busted():  # check if a bet is placed and if player hand si not busted
            message = "Player choosed to \n stay."
            self.show_dealer_message(message)
            self.show_hidden_card()  # it is showed the dealer hidden card
            self.dealer_turn()  # dealer starts to deal card from him self
        else:
            message = "Action not \n allowed."
            self.sound.play_sound("error")
            self.show_dealer_message(message)
    
    def double_action(self, event):
        """check if player can double his bet"""
        if self.double_bet.get():
            message = "Player choosed to \n double his bet."
            self.show_dealer_message(message)
            self.double_bet.set(False)
            self.player_credit.double_bet()
            self.update_credit()
            self.game_table_canvas.create_image(739, 255, image=self.chip_ontable_icon, anchor="nw",
                                                tags="chips-on-table")  # a set of chips (a picture) is placed on the game table
            self.sound.play_sound("gasp")
        else:
            message = "Action not \n allowed."
            self.sound.play_sound("error")
            self.show_dealer_message(message)
    
    def show_hidden_card(self):
        """from here dealer hidden card is showed on table"""
        value, suit = self.dealer_hand.show_hidden_card()
        picture_name = str(value) + "." + str(suit) + ".png"
        cards_folder = "Images\\Cards"
        self.dealer_slots[1].configure(file=os.path.join(cards_folder, picture_name))
        self.sound.play_sound("card-flip")
    
    def dealer_turn(self):
        """dealer show his card and start dealing playing cards for him until he reaches 17 or is busted"""
        if self.dealer_hand.total < 17:
            self.sound.play_sound("card-flip")
            self.place_cards_on_table(self.dealer_hand.add_card(self.deck_card.deal()))
            self.root.after(1000, self.dealer_turn)
        else:
            self.check_winner()
    
    def check_player_busted(self):
        """after each new player card is checking if he is busted or not"""
        if self.player_hand.busted():  # if player total is higher than 21 points
            self.show_hidden_card()
            self.winner_action(dealer=True)
        elif self.player_hand.black_jack():  # if player have in his hand 21 points
            self.show_hidden_card()
            self.winner_action(player=True)
        elif self.player_hand.black_jack() and self.dealer_hand.black_jack():  # if player and dealer have 21 points in their hands
            self.show_hidden_card()
            self.winner_action(player=True, dealer=True)
    
    def check_winner(self):
        """from here a winner is defined when player choose stand and then a special function is called according to winning player"""
        if self.dealer_hand.busted() and not self.player_hand.busted():  # player is the winner because dealer is busted
            self.winner_action(player=True)
        
        
        elif not self.dealer_hand.busted() and self.player_hand.busted():  # dealer is the winner  because player is busted
            self.show_hidden_card()
            self.winner_action(dealer=True)
        
        elif not self.dealer_hand.busted() and not self.player_hand.busted():  # dealer and player are not busted
            if self.dealer_hand.get_total() > self.player_hand.get_total():  # dealer is the winner
                self.winner_action(dealer=True)
            
            elif self.dealer_hand.get_total() < self.player_hand.get_total():  # player is the winner
                
                self.winner_action(player=True, dealer=False)
            else:  # in this case no one wins, it is a tie
                self.winner_action(player=True, dealer=True)
    
    def winner_action(self, player=False, dealer=False):
        if player and dealer:  # when is a tie player receive his bet amount
            message = " It was a tie and a total \nof " + str(self.player_credit.bet) + " $ \n returned to player."
            self.show_winner_message(message)
            self.player_credit.tie_hand()
            self.update_credit()
        
        elif player and not dealer:  # when player win
            message = "Player won this hand \n and a total of " + str(self.player_credit.bet) + " $"
            self.show_winner_message(message)
            self.player_credit.win_hand()
            self.update_credit()
        
        
        else:  # when house wins
            message = "Player lose this hand \n and a total of " + str(self.player_credit.bet) + " $"
            self.show_winner_message(message)
            self.player_credit.lose_hand()
            self.update_credit()
        self.game_table_canvas.after(3000, self.game_ending)
    
    def update_credit(self):
        self.menu_canvas.itemconfig(self.credit_balance_text, text=self.player_credit.get_credit())
    
    def game_ending(self):
        """afther a winner is declared, this function is called to reset game table. """
        self.player_hand.reset_hand()
        self.dealer_hand.reset_hand()
        self.reset_table_slots()
        self.create_table_slots()
        self.bet_placed.set(False)
        self.double_bet.set(False)
        self.game_table_canvas.delete("chips-on-table")
    
    def mute_unmute_sound(self, event):
        """from here sound effect are shutted down"""
        if self.sound.get_state() == 0:
            self.sound.mute_unmute(7)
            self.sound_button.configure(file="Images\\sound_button.png")
        else:
            self.sound.mute_unmute(0)
            self.sound_button.configure(file="Images\\mute_sound_button.png")
    
    def buy_credit(self,event):
        self.credit_window= CreditWindow(self.root)
        
    
    def withdraw_credit(self,event):
        self.credit_window.close()
        
    
    
    def quit(self, event):
        """from here main window is closed"""
        self.root.destroy()


if __name__ == "__main__":
    deck_card = DeckCards()
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)
    sound = Sound()
    player_credit = Credit(100)
    app = GUI(player_hand, dealer_hand, deck_card, sound, player_credit)
