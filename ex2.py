class microwave:

    def __init__(self, time, foodType, mode):

        self.time = time
        self.foodType = foodType
        self.mode = mode
        self.grill = bool

    def cookFoodType(self):

        if self.foodType == 'chicken':
            self.time = 10
        elif self.foodType == 'meat':
            self.time = 20
        elif self.foodType == 'soup':
            self.time = 15

        return self.time

    def cookmode(self):

        if self.mode == 'boil':
            self.mode = 100
        if self.mode == 'fry':
            self.mode = 200
        if self.mode == 'bake':
            self.mode = 300

        return self.mode

    def cookGrill(self):

        if self.foodType == 'chicken':
            self.grill = True
        elif self.foodType == 'meat':
            self.grill = True

        return self.grill
