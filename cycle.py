class cycle():
    def __init__(self,min_,max_,step=1):
        self.now = min_
        self.min_ = min_
        self.max_ = max_
        self.step = 1
        self.const = 0
    def add(self):
        if self.now==self.max_:
            self.now = self.min_
            return self.min_
        self.now += 1
        return self.now
    def decrease(self,v):
        self.now -= v
    def structure(self):
        return [self.now,self.min_,self.max_,self.step]
    def __str__(self):
        if self.result()>=0:
            return str(self.result())
        else:
            return "0"
    def result(self):
        return self.now+self.const