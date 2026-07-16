def scope_check():
     def do_local():
          test = "do local value"
     def doNonLocal():
         test = "do non local"
     def do_global ():
          test = "do gobal vlaue"
     test= "default value"
     do_local()
     print("value of test shown here ---  "+test  )


scope_check()