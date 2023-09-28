import sys
from PIL import Image
import numpy as np
import builtins




from PIL import Image
import numpy as np

class Solution:

    def str2bits(self,key):
        dic={'!': 0, '@': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27, 'A': 28, 'B': 29, 'C': 30, 'D': 31, 'E': 32, 'F': 33, 'G': 34, 'H': 35, 'I': 36, 'J': 37, 'K': 38, 'L': 39, 'M': 40, 'N': 41, 'O': 42, 'P': 43, 'Q': 44, 'R': 45, 'S': 46, 'T': 47, 'U': 48, 'V': 49, 'W': 50, 'X': 51, 'Y': 52, 'Z': 53, '0': 54, '1': 55, '2': 56, '3': 57, '4': 58, '5': 59, '6': 60, '7': 61, '8': 62, '9': 63}
        res=[]
        for i in key:
            t=dic[i]
            for j in range(6):
                res.append(t&1)
                t>>=1
        return res
    
    def channel_avg(self,n,x,y):
        vec=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        r=0
        g=0
        b=0
        for i in vec:
            xx=x+i[0]
            yy=y+i[1]
            r+=n[xx][yy][0]
            g+=n[xx][yy][1]
            b+=n[xx][yy][2]

        ret=(r//8,g//8,b//8)
        dr=0
        dg=0
        db=0
        for i in vec:
            xx=x+i[0]
            yy=y+i[1]
            dr+=(n[xx][yy][0]-ret[0])**2
            dg+=(n[xx][yy][1]-ret[1])**2
            db+=(n[xx][yy][2]-ret[2])**2
        dr+=(n[x][y][0]-ret[0])**2
        dg+=(n[x][y][1]-ret[1])**2
        db+=(n[x][y][2]-ret[2])**2
        from math import sqrt
        dr=sqrt(dr/9)
        dg=sqrt(dg/9)
        db=sqrt(db/9)
        return ret,(dr,dg,db)

    
    def Encrypt(self, img, key) :
        key=key.ljust(10,"!")
        img = Image.open(img)
        m=np.asarray(img)
        import random
        r = random.Random(678)
        stream=self.str2bits(key)
        #print(stream)
        #print(len(stream))
        n=np.copy(m)
        #self.s=stream
        for t in range(1):
            for i in stream:
                x=r.randint(0,1023)
                y=r.randint(0,1023)
                avg,dx=self.channel_avg(n,x,y)
                #print(n[x][y][0]-avg[0],n[x][y][1]-avg[1],n[x][y][2]-avg[2])
                if(i):
                    n[x][y][0]=255
                    n[x][y][1]=255
                    n[x][y][2]=255
                else:
                    n[x][y][0]=0
                    n[x][y][1]=0
                    n[x][y][2]=0
                
        img=Image.fromarray(n)
        return img
    
    def bits2str(self,stream):
        rdic='!@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        res=0
        #print(stream)
        for i in stream:
            res*=2
            res+=i
        return rdic[res]

    def Decrypt(self,img):
        img = Image.open(img)
        n=np.asarray(img)
        import random
        r = random.Random(678)
        res=[]
        prob=[0]*60
        for i in range(60):
            x=r.randint(0,1023)
            y=r.randint(0,1023)
            avg,dx=self.channel_avg(n,x,y)
            #print("%.2f,%.2f,%.2f,%d"%(n[x][y][0]/0x80,n[x][y][1]/0x80,n[x][y][2]/0x80,self.s[i%60]))#,dx)
            res.append(int((n[x][y][0]/128+n[x][y][1]/128+n[x][y][2]/128)//3))
        #print([res[i]==self.s[i] for i in range(60)])
        key=''
        for i in range(0,60,6):
            key+=self.bits2str(res[i:i+6][::-1])
        return key





def print(*args, **kwargs):
    pass

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv)!=2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    secret = s.Decrypt(img)
    print = builtins.print
    print(secret)
    

