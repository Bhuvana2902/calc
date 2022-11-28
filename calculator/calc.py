from flask import Flask,render_template,request
app=Flask(__name__)
@app.route(‘/’)
def welcome():
  return render_template(‘calculator.html’)
@app.route(‘/’,methods=’post’)
def result():
  var1=request.form.get(“var_1” ,type=int, default=0)
  var2=request.form.get(“var1_2”,type=int, default=0)
  operation=request.form.get(“operation”)
  if(operation==’Addition’):
   result=var1+var2
  if(operation==’Subtraction’):
   result=var1-var2
  if(operation==’Multiplication’):
   result=var1*var2
  if(operation==’Division’):
   if(var1==0 and var2==0):
    result=0
   else:
     result=var1/var2
  else: 
   result=0
  entry=result
  return render_template(‘calculator.html’,entry=entry)

if(__name__==__main__):
  app.run(debug=True)
