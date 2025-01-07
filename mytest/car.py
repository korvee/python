class Car:
    speed =0
    started = False
    def __init__(self,started = False,speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print('the car has started')
    
    def increaseSpeed(self,delta):
        if self.started:
            self.speed = self.speed + delta
            print('''the car's speed has increased to''',self.speed)
        else:
            print('you need to start the car first')
    # 仅在将Car作为脚本运行时，__name__为main，而作为模块使用时为模块名
    # 所以直接运行当前文件才会执行if内的代码        
    if __name__ == '__main__':
        print('as script run')