class Mobile:
    def __init__(self,Model,Camera,Storage,FaceUnlock):
        self.Model = Model
        self.Camera = Camera
        self.Storage = Storage
        self.FaceUnlock = FaceUnlock
    def makecall(self,number):
        return 'calling...{}'.format(number)

M1 = Mobile('iphone 12 pro','64 MP','128 GB','YES')
print(M1)
print(M1.Model)
print(M1.Camera)
print(M1.Storage)
print(M1.FaceUnlock)
print(M1.makecall(8096248582))

M2 = Mobile('iphone 12 ','14 MP','64 GB','No')
print(M2)
print(M2.Model)
print(M2.Camera)
print(M2.Storage)
print(M2.FaceUnlock)
print(M2.makecall(8096248582))


