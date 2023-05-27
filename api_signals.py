import concurrent.futures
from datetime import datetime as dt
import random
import math

class Signals_Double():
        
    def check_patterns(self, patterns, last_numbers, last_colors):

        # Verifica se last_colors é uma lista não vazia
        if not isinstance(last_colors, list) or not last_colors:
            self.last_colors = []
        else:
            self.last_colors = last_colors

        # Verifica se last_numbers é uma lista não vazia
        if not isinstance(last_numbers, list) or not last_numbers:
            self.last_numbers = []
        else:
            self.last_numbers = last_numbers

        try:
            self.black_patterns = patterns["black"]
        except KeyError:
            self.black_patterns = []
        
        try:
            self.red_patterns = patterns["red"]
        except KeyError:
            self.red_patterns = []

        def check_black_patterns():
            for pattern in self.black_patterns:
                pattern_size = len(last_colors) - len(pattern)
                cut_colors = last_colors[pattern_size:]
                cut_numbers = last_numbers[pattern_size:]
                new_last_results = []

                for position, item in enumerate(pattern):
                    if item.isnumeric():
                        try:
                            new_last_results.append(str(cut_numbers[position]))
                        except:
                            pass
                    else:
                        try:
                            new_last_results.append(str(cut_colors[position]))
                        except:
                            pass

                if new_last_results == pattern:
                    return {"signal":True, "signal_color": "black", "pattern": pattern, "last_results":{"last_numbers": last_numbers, "last_colors":last_colors}}
           
            return {"signal":False, "signal_color": None, "pattern": None, "last_results":{"last_numbers": last_numbers, "last_colors":last_colors}}
        
        def check_red_patterns():
            for pattern in self.red_patterns:
                pattern_size = len(last_colors) - len(pattern)
                cut_colors = last_colors[pattern_size:]
                cut_numbers = last_numbers[pattern_size:]
                new_last_results = []

                for position, item in enumerate(pattern):
                    if item.isnumeric():
                        try:
                            new_last_results.append(str(cut_numbers[position]))
                        except:
                            pass
                    else:
                        try:
                            new_last_results.append(str(cut_colors[position]))
                        except:
                            pass
                            
                if new_last_results == pattern:
                    return {"signal":True, "signal_color": "red", "pattern": pattern, "last_results":{"last_numbers": last_numbers, "last_colors":last_colors}}
                
            return {"signal":False, "signal_color": None, "pattern": None, "last_results":{"last_numbers": last_numbers, "last_colors":last_colors}}

        executor = concurrent.futures.ThreadPoolExecutor()
        
        black_pattern =  executor.submit(check_black_patterns)
        red_pattern = executor.submit(check_red_patterns)
        
        result_black_pattern = black_pattern.result()
        result_red_pattern = red_pattern.result()
        if result_black_pattern["signal"]:
            return result_black_pattern
        
        elif result_red_pattern["signal"]:
            return result_red_pattern
        
        else:
            return {"signal":False, "signal_color": None, "pattern": None, "last_results":{"last_numbers": last_numbers, "last_colors":last_colors}}

    def check_victory(self, signal_color, victory_white, last_colors, martingale, max_martingale):
        last_color = last_colors[len(last_colors)- 1]
        if str(last_color) == str(signal_color):
            return {"victory": True, "loss": False, "max_martingale": max_martingale, "signal_color": signal_color, "last_color":last_color}
        
        elif str(last_color) == "white":

            if victory_white:
                return {"victory": True, "loss": False, "max_martingale": max_martingale, "signal_color": signal_color, "last_color":last_color}
            
            else:
                return {"victory": False, "loss": False, "max_martingale": max_martingale, "signal_color": signal_color, "last_color":last_color}
        else:
            if martingale >= max_martingale:
                return {"victory": False, "loss": True, "max_martingale": max_martingale, "signal_color": signal_color, "last_colors":last_colors, "last_color":last_color}
            
            else:
                return {"victory": False, "loss": False, "max_martingale": max_martingale, "signal_color": signal_color, "last_colors":last_colors, "last_color":last_color}
            
class Signals_Crash():
    def check_pattern(self, patterns, last_numbers, last_colors):
        last_number = last_numbers[len(last_numbers)-1]
        last_color = last_colors[len(last_colors)-1]
        # Verifica se last_colors é uma lista não vazia
        if not isinstance(last_colors, list) or not last_colors:
            self.last_colors = []
        else:
            self.last_colors = last_colors
            
        # Verifica se last_numbers é uma lista não vazia
        if not isinstance(last_numbers, list) or not last_numbers:
            self.last_numbers = []
        else:
            self.last_numbers = last_numbers
        
        for pattern in patterns:
            pattern_size = len(last_numbers) - len(pattern)
            cut_colors = last_colors[pattern_size:]
            cut_numbers = last_numbers[pattern_size:]
            new_last_results = []

            for position, item in enumerate(pattern):
                if item.isnumeric():
                    try:
                        new_last_results.append(str(cut_numbers[position]))
                    except:
                        pass
                else:
                    try:
                        new_last_results.append(str(cut_colors[position]))
                    except:
                        pass

            if new_last_results == pattern:
                return {"signal": True, "pattern": pattern, "last_results":{"last_numbers": last_numbers, "last_colors": last_colors, "last_number": last_number, "last_color": last_color}}

        return {"signal": False, "pattern": None, "last_results":{"last_numbers": last_numbers, "last_colors": last_colors, "last_number": last_number, "last_color": last_color}}
    
    def check_victory(self, crash_point, last_number, martingale, max_martingale):
        if float(last_number) > float(crash_point):  
            return {"victory": True, "loss": False, "max_martingale": max_martingale, "crash_point": crash_point, "last_number":last_number}
        
        elif martingale >= max_martingale:
                return {"victory": False, "loss": True, "max_martingale": max_martingale, "crash_point": crash_point, "last_number":last_number}
        
        return {"victory": False, "loss": False, "max_martingale": max_martingale, "crash_point": crash_point, "last_number":last_number}

class Signals_List():
    def __init__(self):
        self.lists = {"double": [], "crash": []}


    def select_minutes(self, num_minutes):
        if not isinstance(num_minutes, int) or num_minutes < 0:
            num_minutes = 0

        if num_minutes < 0:
            num_minutes = 60

        drawn_minute = sorted(random.sample(range(60), num_minutes))

        return [str(minuto).zfill(2) for minuto in drawn_minute]
     

    def colors(self, num_minutes):
        self.double = []
        self.possible_colors = ["⚫", "🔴"]
        minutes = self.select_minutes(num_minutes)
        for min in minutes:
            self.double.append({"minute": min, "color": random.choice(self.possible_colors), "white": "⚪"})
        
        return self.double

    def main(self, num_doubles, num_crashs, hour): # Deve receber a quantidade de sinais que sera gerado no modo double e crash, assim como a hora atual 

        double = self.colors(num_doubles)
        for item in double:
            item["hour"] = hour
        
        crash = []
        min_crash = self.select_minutes(num_crashs)

        for min in min_crash:
            crash.append({"hour": str(hour).zfill(2), "minute": min, "crash_point": "2.00X"})
        
        self.lists = {"double": double, "crash": crash}
        return self.lists
    
        
class Signals_Branco():
    def __init__(self):
        self.last_white = True

    def check_white(self, last_colors):
        if self.last_white:
            came_white = False
            cont_white = 0
            for color in last_colors:
                if color == "white":
                    came_white = True
                    break
                
                else:
                    cont_white += 1

            if len(last_colors) >= 6:
                if cont_white == 5:
                    self.last_white = False
                    return {"signal": True, "came_white": came_white, "last_white": cont_white, "last_colors": last_colors}

        
        return {"signal": False, "came_white": came_white, "last_white": cont_white, "last_colors": last_colors}

    def generate_times(self, last_colors):
        check_white = self.check_white(last_colors)
        times = []

        if check_white["signal"]:
            min = int(dt.now().strftime('%M'))
            hour = str(dt.now().strftime('%H')).zfill(2)

            for m in range(4):
                times.append({"hour": str(hour).zfill(2), "minute": str(min).zfill(2)})
                min = int(min) + 2

                if min >= 60:
                    min = int(min) - 60
                    hour = int(hour) + 1

                    if hour >= 24:
                        hour -= 24
            
            last_minute = times[len(times) - 1]
            fist_minute = times[0]
            return {"signal": True, "last_white": check_white["last_white"], "last_colors": last_colors, "times": times, "fist_minute": fist_minute, "last_minute": last_minute} 
        
        return {"signal": False, "last_white": check_white["last_white"], "last_colors": last_colors, "times": times} 

    def check_victory(self, last_colors, last_minute):
        last_color = last_colors[len(last_colors) - 1]
        hour = dt.now().strftime('%H')
        min = dt.now().strftime('%M')
        last_min = last_minute["minute"]
        if int(last_min) <= 8:
            if int(min) >= 8:
                min = int(min) - 60
                
        if int(min) >= int(last_min) + 1:
            self.last_white = True
            return {"victory": False, "break": True, "hour": hour, "minute": min, "last_color": last_color}
        
        if str(last_color) == "white":
            return {"victory": True, "break": False, "hour": hour, "minute": min, "last_color": last_color}

        return {"victory": False, "break": False,"hour": None, "minute": None, "last_color": last_color}
    
class Signals_Mines():
    def break_lines(self, mines):
        string_length = len(mines)
        desired_width = math.ceil(math.sqrt(string_length))

        num_lines = math.ceil(string_length / desired_width)
        groups = [mines[i:i+desired_width] for i in range(0, string_length, desired_width)]

        if len(groups[-1]) < desired_width:
            groups[-1] += " " * (desired_width - len(groups[-1]))

        new_string = "\n".join(groups)
        return {"mines": mines, "new_mines": new_string, "num_lines": num_lines}

    def generate_mines(self, size_mines, num_diamonds):
        if size_mines > num_diamonds:
            mines = []
            for n in range(size_mines):
                mines.append("⬛")

            drawn_nums = random.sample(range(size_mines - 1), num_diamonds)

            for position in drawn_nums:
                mines[position] = "💎"
            
            mines = "".join(mines)
            return{"error": None, "size_mines": size_mines, "num_diamonds": num_diamonds ,"position_diamonds": num_diamonds ,"mines": mines}
        
        else:
            return {"error": "Sorry, the size of the minefield is less than or equal to the amount of diamonds in it!"}

    def main(self, size_mines, num_diamonds):
        mines = self.generate_mines(size_mines=size_mines, num_diamonds=num_diamonds)
        if not mines["error"]:
            new_mines = self.break_lines(mines["mines"])
            return {"mines": new_mines["new_mines"], "mines_inline": mines["mines"], "size_mines": size_mines, "num_diamonds": num_diamonds, "position_diamonds": mines["position_diamonds"], "num_lines": new_mines["num_lines"]}
        
        return {"mines": None, "mines_inline": None, "size_mines": size_mines, "num_diamonds": num_diamonds, "position_diamonds": None, "num_lines": None}