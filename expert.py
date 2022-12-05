from experta import *
import os

def input_validation(question):
        while True:
            data = input(question)
            if not data:
                print("Sorry, you must enter an answer.")
                continue
            else:
                if data.lower() not in ('no', 'low', 'high'):
                    print("Not an appropriate choice.")
                else:
                    break
        return data

class SongConsult(KnowledgeEngine):
    def __init__(self, song_map, if_unmatched, get_song_desc):
        self.song_map = song_map
        self.if_unmatched = if_unmatched
        self.get_song_desc = get_song_desc

        KnowledgeEngine.__init__(self)

    #code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        os.system('cls')
        print("########### Welcome to the song recommender Bot ##################")
        print("\nAnswer the following questions to find a perfect song that matches your energy rn. (Answer with high, low or no)")
        yield Fact(action = "get_song")

    #defines the facts, the input data from user
    @Rule(Fact(action = "get_song"), NOT(Fact(danceability = W())), salience = 1)
    def feature_0(self):
        self.declare(Fact(danceability = input_validation("How much Danceable is the song you're looking for: ")))

    @Rule(Fact(action = "get_song"), NOT(Fact(energy = W())), salience = 1)
    def feature_1(self):
        self.declare(Fact(energy = input_validation("How much Energy are you're looking for: ")))

    @Rule(Fact(action = "get_song"), NOT(Fact(happiness = W())), salience = 1)
    def feature_2(self):
        self.declare(Fact(happiness = input_validation("How Happy are you right now: ")))

    @Rule(Fact(action = "get_song"), NOT(Fact(popularity = W())), salience = 1)
    def feature_3(self):
        self.declare(Fact(popularity = input_validation("How popular do you want to be the song: ")))

    @Rule(Fact(action = "get_song"), NOT(Fact(how_old = W())), salience = 1)
    def SYMP_4(self):
        self.declare(Fact(how_old = input_validation("How old do you want to be the song: ")))


    #defines the rules, restrictions applied to the facts for checking for each song match
    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_0(self):
        self.declare(Fact(song = "Forever"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "low"),
        Fact(how_old = "high"),

    )
    def song_1(self):
        self.declare(Fact(song = "Dont_you_wanna_play"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "no"),
        Fact(how_old = "low"),

    )
    def song_2(self):
        self.declare(Fact(song = "I_wont_let_you_walk_away"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_3(self):
        self.declare(Fact(song = "I_can_be_somebody"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "low"),
        Fact(how_old = "high"),

    )
    def song_4(self):
        self.declare(Fact(song = "These_are_the_times"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_5(self):
        self.declare(Fact(song = "Solo_dance_club_mix"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "high"),
        Fact(how_old = "no"),

    )
    def song_6(self):
        self.declare(Fact(song = "We_found_love"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "high"),
        Fact(how_old = "low"),

    )
    def song_7(self):
        self.declare(Fact(song = "Born_to_be_yours"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "low"),
        Fact(happiness = "no"),
        Fact(popularity = "high"),
        Fact(how_old = "high"),

    )
    def song_8(self):
        self.declare(Fact(song = "Be_kind_with_halsey"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "no"),
        Fact(how_old = "low"),

    )
    def song_9(self):
        self.declare(Fact(song = "Anywhere_for_you"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "high"),
        Fact(energy = "high"),
        Fact(happiness = "low"),
        Fact(popularity = "high"),
        Fact(how_old = "no"),
 
    )
    def song_10(self):
        self.declare(Fact(song = "Pompeii"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "high"),
        Fact(popularity = "low"),
        Fact(how_old = "no"),

    )
    def song_11(self):
        self.declare(Fact(song = "Silhouettes_radio_edit"))

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "low"),
        Fact(happiness = "no"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_12(self):
        self.declare(Fact(song = "Stranger_things"))
    
    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "low"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_13(self):
        self.declare(Fact(song = "What_do_you_love"))
        
    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = "no"),
        Fact(energy = "high"),
        Fact(happiness = "no"),
        Fact(popularity = "low"),
        Fact(how_old = "low"),

    )
    def song_14(self):
        self.declare(Fact(song = "Shelter"))      
        
        

    #check if user's input matches any song in the knowledge base
    @Rule(Fact(action = "get_song"), Fact(song = MATCH.song), salience =- 998)
    def song(self, song):
        song_DESC = self.get_song_desc(song)
        os.system('cls')
        print(f"Your perfect song is: {song}\n")
        print(f"Description: {song_DESC}\n")
        print("-----------------------------------------------")

    @Rule(
        Fact(action = "get_song"),
        Fact(danceability = MATCH.danceability),
        Fact(energy = MATCH.energy),
        Fact(happiness = MATCH.happiness),
        Fact(popularity = MATCH.popularity),
        Fact(how_old = MATCH.how_old),
        NOT(Fact(song = MATCH.song)),
        salience =- 999
    )

    def not_matched(self, danceability,energy, happiness,popularity,how_old):
        os.system('cls')
        print("\nThe bot did not find a song that match your search.")
        lis = [danceability, energy, happiness, popularity, how_old]
        max_count, max_song = 0, ""
        for key, val in self.song_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and (lis[j] == "high" or lis[j] == "low" or lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_song = val
        if max_song != "":
            self.if_unmatched(max_song)