import sqlite3
def resource(ovr_lft,wlt):
   conn = sqlite3.connect('c:/RR.db')
   cursor=conn.cursor()
   cursor=conn.execute("SELECT * from rpr_obo where overs_left=?",(ovr_lft,))
   ans=cursor.fetchone()
   j=-1
   for i in ans:
      j+=1
      if j==(wlt+1):
         break
   conn.close()
   return i
