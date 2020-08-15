import math
def add_time(a,b,c=None):
    
    
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    a = a.split(" ")
    ans = []
    b = [int(b.split(':')[0]),int(b.split(':')[1])]
    if (a[1]=='PM'):
        a = [int(a[0].split(':')[0])+12,int(a[0].split(':')[1])]
    else :
        a = [int(a[0].split(':')[0]),int(a[0].split(':')[1])]
    
    ans = [a[0]+b[0],a[1]+b[1]]
    if(ans[1]>=60):
        ans[0] += 1
        ans[1] -= 60
    
    count = math.floor(ans[0]/24)

    if(ans[0]>=24):
        ans[0] %= 24

    if(ans[0]>=12):
        clock = 'PM'
    else:
        clock = 'AM'

    if ans[0]==0 :
        ans[0] = 12

    if ans[0]>12 :
        ans[0] -= 12

    ans[0] = str(ans[0])

    if(ans[1]>10):
        ans[1] = str(ans[1])
    else:
        ans[1] = '0'+str(ans[1])
    
    answer = ':'.join(ans)+' '+clock

    if c:
        c = c.capitalize()
        d = days.index(c)+count
        d %=7
        answer += ', '+days[d]
    
    if count==0 :
        return answer
    elif count==1:
        return answer+' (next day)'
    else:
        return answer+' ('+str(count)+' days later)'
