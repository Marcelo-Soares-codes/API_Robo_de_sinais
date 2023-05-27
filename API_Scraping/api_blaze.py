import requests

class DoubleApi():
    def __init__(self):
        self.url = "https://blaze.com/api/roulette_games"
        self.last_numbers = []
        self.last_colors = []
    """    self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.data = self.response.json()

        else:
            print(f"Certifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
            self.data = {}"""
    
    def wait_complete(self):
        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] != "complete":
                                break
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] == "complete":
                                return self.response.json()
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] == "complete":
                                return self.response.json()
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break

    def wait_rolling(self):
        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] != "rolling":
                                break
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] == "rolling" or self.response.json()["status"] == "complete":
                                return self.response.json()
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

    def wait_id(self):
        id_01 = ""
        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    id_01 = self.response.json()["id"]
                    while True:
                        self.response = requests.get(self.url+"/current")
                        if self.response.status_code == 200:
                            if id_01 != self.response.json()["id"]:
                                id_01 = self.response.json()["id"]
                                break
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
                     
            except:
                pass

        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    id_01 = self.response.json()["id"]
                    while True:
                        self.response = requests.get(self.url+"/current")
                        if self.response.status_code == 200:
                            if id_01 != self.response.json()["id"]:
                                id_01 = self.response.json()["id"]
                                break
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

    def last_number_current(self):
        while True: 
            try:
                self. response = requests.get(self.url+"/current")
                self.data = self.response.json()
                
            except:
                self. response = requests.get(self.url+"/current")
                self.data = self.response.json()

            if self.data["status"] == "rolling":
                if self.response.status_code == 200:
                    return self.data["roll"]
                else:
                    print(f"Não foi possivel coletar o ultimo numero que saiu! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
    
    def transform_color(self, color):
        if color == 2:
            return "black"
        if color == 1:
            return "red"
        if color == 0:
            return "white"

    def last_color_current(self):
        while True: 
            try:
                self. response = requests.get(self.url+"/current")
                self.data = self.response.json()
            except:
                self. response = requests.get(self.url+"/current")
                self.data = self.response.json()
            if self.data["status"] == "rolling":
                if self.response.status_code == 200:
                    return self.transform_color(self.data["color"])
                
            else:
                print(f"Não foi possivel coletar o ultimo numero que saiu! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
    
    def limit_lists(self, num, color):  # Limita as ultimas "pedras" que sairam a 10 e retorna os ultimos 10 numero e as ultimas 10 cores
        if len(self.last_numbers) >= 10:
            self.last_numbers.pop(0)
        if len(self.last_colors) >= 10:
            self.last_colors.pop(0)
        self.last_numbers.append(num)
        self.last_colors.append(color)
        return self.last_numbers, self.last_colors
    

class CrashApi():
    def __init__(self):
        self.url = "https://blaze.com/api/crash_games/"
        self.last_points = []
        self.last_color = []

    def wait_crash(self):
        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] != "complete":
                                break
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

        while True:
            try:
                self.response = requests.get(self.url+"/current")
                if self.response.status_code == 200:
                    if self.response.json()["status"] == "complete":
                                return self.response.json()
                else:
                    print(f"Não foi possivel aguardar um resultado! \nCertifique-se de que está conectado à internet ou faça uma busca para saber o motivo do código recebido: {self.response.status_code}")
                    break
            except:
                pass

    def last_crashes(self):
        crashes = []
        self.response = requests.get(self.url+"/current")
        if self.response.status_code == 200:
            for item in self.response.json():
                if float(item["crash_point"]) == 0:
                    crashes.append("1.00")
                else:
                    crashes.append(item["crash_point"])
        return crashes
    
    def last_crash_current(self):
        self.response = requests.get(self.url+"/current")
        if self.response.status_code == 200:
            if self.response.json()["status"] == "complete":          
                crash_point = self.response.json()["crash_point"]
                if float(crash_point) == 0:
                    crash_point = "1.00"

                return crash_point
        
        return "0"
    
    def last_color_current(self):
        self.response = requests.get(self.url+"/current")
        if self.response.status_code == 200:
            if self.response.json()["status"] == "complete":          
                crash_point = self.response.json()["crash_point"]
                if float(crash_point) >= 2:
                    return "green"
                
        return "black"
        
        
    def limit_list_crashes(self, crash, color):
        if len(self.last_points) >= 10:
            self.last_points.pop(0)

        self.last_points.append(crash)
        
        if len(self.last_color) >= 10:
            self.last_color.pop(0)

        self.last_color.append(color)
        return self.last_points, self.last_color
                      
              

