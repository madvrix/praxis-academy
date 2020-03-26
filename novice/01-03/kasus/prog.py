runtime=0
class hy:
    def __init__(self,runtime):
        if runtime==0:
            print("Hai apa kabar")
    def hm(self,runtime):
        print("Ada yang bisa saya bantu?")
        for x in range(10):
            print(".")
        runtime=1
        hy(runtime).metu(runtime)
    def metu(self,runtime):
        print('oke sampai jumpa')

hy(runtime).hm(runtime)