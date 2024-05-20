def slice():
   Str:str='''hello, dearr 
   how are you?'''
   extracteditem1=Str[0:3]
   extracteditem2=Str[3:7]
   extracteditem3=Str[7:11]
   extracteditem4=Str[11:15]
   extracteditem5=Str[15:19]
   extracteditem6=Str[19:23]
   extracteditem7=Str[23:len(Str)]
   extracteditem:tuple={
      "originalstr":Str,
      "extracteditem1":extracteditem1,
       "extracteditem2":extracteditem2,
         "extracteditem3":extracteditem3,
           "extracteditem4":extracteditem4, 
           "extracteditem5":extracteditem5, 
           "extracteditem6":extracteditem6, "extracteditem6":extracteditem7
   }
   print(extracteditem)
slice()
