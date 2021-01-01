''' Duckworth liews method claculator for target score estimation and par score table production'''
import resource_demo as rd
import test_im_rs as pst
score=S=0
overs=O=50
R1=R2=100
'''-------------------------------------------------------------------------------------------'''
def get_team1_score():
    global S
    S=int(input("innings end team1 score: "))
def put_team1_score():
    return S
def get_overs_at_start():
    global O
    O=int(input("innings start team1 overs: "))
def put_overs_at_start():
    return O
def get_wicket_lost():
    return int(input())
'''-------------------------------------------------------------------------------------------'''
def interuption_1(s1,ovr,wlst):
    global R1,R2
    wl=10-wlst
    print("s1: ",s1)
    print("Enter over played yet: ")
    ovr_ply=int(input())
    print("Enter overs lost : ")
    ovr_lst=int(input())
    ovr_rst=ovr-ovr_lst
    ovr_lft=ovr-ovr_ply
    R1=rd.resource(ovr,0)
    print("R1: ",R1)
    ovr=ovr-ovr_lst
    if ovr_ply>=45:#resource lost at end of innings(cut short)
        r1=rd.resource(ovr_lft,wl)#resources func call
        r2=0
        print("ovr_lft: ",ovr_lft)
        print("r1: ",r1)
        R1=R1-r1+r2
        print("R1: ",R1)
        #ovr=ovr_ply
    else:       #resourse lost in middle of innings(interupted)
        wl=10-wl
        r1=rd.resource(ovr_lft,wl)
        print("r1: ",r1)
        ovr_lft_rst=ovr_rst-ovr_ply
        r2=rd.resource(ovr_lft_rst,wl)#resources func call
        print("r2: ",r2)
        R1=R1-r1+r2
        print("R1: ",R1)
        print("\n\t once again interupted?(y/n): ")
        ans=input()
        while(ans is "y" or ans=="Y"):
            print("Enter over played yet: ")
            ovr_ply=int(input())
            print("Enter overs lost : ")
            ovr_lst=int(input()) 
            ovr=ovr_rst-ovr_lst
            ovr_lft=ovr_lft_rst-ovr_ply
            ovr_lft_rst=ovr_lft-ovr_lst
            print("ovr",ovr)
            r1=rd.resource(ovr_lft,wl)#resources func call
            print("r1: ",r1)
            r2=rd.resource(ovr_lft_rst,wl)#resources func call
            print("r2: ",r2)
            R1=R1-r1+r2
            print("\n\t once again interupted?(y/n): ")
            ans=input()   
    print("R1: ",R1)        
    R2=rd.resource(ovr,0)
    print("R2: ",R2)
    S2=target_score(R1,R2)
    print("\n\tSCORE FOR TEAM 2: ",S2)
    pst.parscore(s1,0,0,ovr_lst,ovr,R1,R2)#parscore for future overs(always for team 2)
'''-------------------------------------------------------------------------------------------'''
def target_score(R1,R2):
    s1=put_team1_score()
    print("s1: ",s1)
    if R1>R2:
        return int(s1*R2/R1)
    elif R1==R2:
        return s1
    else:
        G50=245
        return int(s1+G50*(R2-R1)/100)        
'''-------------------------------------------------------------------------------------------'''
def interuption_2(ovr,wl):
    global R2
    s1=put_team1_score()
    if s1==0:
        return
    print("Enter over played yet: ")
    ovr_ply=int(input())
    print("Enter overs lost : ")
    ovr_lst=int(input())
    ovr_rst=ovr-ovr_lst
    ovr_lft=ovr-ovr_ply
    R2=rd.resource(ovr,0)
    ovr=ovr-ovr_lst
    print("R2: ",R2)
    if ovr_ply==0:#resource lost at start of innings(delayed)
        print("ovr_rst: ",ovr_rst)
        print("wl: ",wl)
        r1=rd.resource(ovr_rst,wl)#resource func call
        R2=r1
    elif ovr_ply>=45:#resource lost at end of innings(cut short)
        r1=rd.resource(ovr_lft,wl)#resources func call
        print("ovr_lft: ",ovr_lft)
        print("wl: ",wl)
        print("r1: ",r1)
        R2=R2-r1
    else:       #resource lost in middle of innings(interupted)
        r1=rd.resource(ovr_lft,wl)
        print("r1: ",r1)
        ovr_lft_rst=ovr_rst-ovr_ply
        r2=rd.resource(ovr_lft_rst,wl)#resources func call
        print("r2: ",r2)
        R2=R2-r1+r2
        print("R2: ",R2)
        print("\n\t once again interupted?(y/n): ")
        ans=input()
        while(ans is "y" or ans=="Y"):
            ovr=ovr_lft_rst
            print("Enter over played yet: ")
            ovr_ply=int(input())
            print("Enter overs lost : ")
            ovr_lst=int(input())
            print("Enter Team2 wickets lost: ")
            wl=get_wicket_lost()
            ovr_lft=ovr-ovr_ply
            ovr_lft_rst=ovr_lft-ovr_lst
            if ovr_lft==ovr_lft_rst:
                break
            r1=rd.resource(ovr_lft,wl)#resources func call
            print("r1: ",r1)
            r2=rd.resource(ovr_lft_rst,wl)#resources func call
            print("r2: ",r2)
            R2=R2-r1+r2
            print("\n\t once again interupted?(y/n): ")
            ans=input()
    print("R2: ",R2)
    S2=target_score(R1,R2)        
    print("\n\tSCORE FOR TEAM 2: ",S2)
    pst.parscore(s1,ovr_ply,wl,ovr_lst,ovr,R1,R2)#parscore for future overs(always for team 2) 
'''-------------------------------------------------------------------------------------------'''                         
def innings2(o):
    global R2
    print("\n\tAny innterruption(Y,N) in inings 2: ")
    ans=input()
    if ans=="Y" or ans=="y":
        print("Enter Team2 wickets lost: ")
        w=get_wicket_lost()
        interuption_2(o,w) #cal. updated resources for interrupted innings
    else:
        R2=rd.resource(O,0)#cal. resources for team 1 uninterupted innings
        s2=target_score(100,R2)
        print("\n\tSCORE FOR TEAM 2: ",s2)
'''------------------------------------------------------------------------------------------'''
def innings1():
    global R1
    get_team1_score()
    s=put_team1_score()
    get_overs_at_start()
    o=put_overs_at_start()
    print("\n\tAny innterruption(Y,N) in inings1(if any): ")
    ans=input()
    if ans=="Y" or ans=="y":
        print("Enter Team1 wickets lost: ")
        w=get_wicket_lost()
        print("s: ",s)
        interuption_1(s,o,w)  #cal. updated resources for interrupted innings 
    else:
        print("o:",o)
        R1=rd.resource(o,0)#cal. resources for team 1 uninterupted innings
        print("R1: ",R1)
        innings2(o)
'''------------------------------------------------------------------------------------------'''        
innings1()    
    

        
    
    
