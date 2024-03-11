function validate(){
  //Считаем значения из полей name и email в переменные x и y
  var x=document.forms['form']['name'].value;
  var y=document.forms['form']['phone'].value;
  var z=document.forms['form']['dop'].value;
      
    if (x.length==0){
      document.getElementById('namef').innerHTML='*данное поле обязательно для заполнения';
      return false;
      }
      if (y.length==0){
      document.getElementById('phone').innerHTML='*данное поле обязательно для заполнения';
      return false;
      }
      if (z.length==0){
        document.getElementById('dop').innerHTML='*данное поле обязательно для заполнения';
        return false;
      }
       plus=m.indexOf("+");
       if (plus<1){
       document.getElementById('phone').innerHTML='*телефон введен не верно';
       return false;
       }}

       function submitForm(){
        var d = document.getElementById("name");
        var h = d.value;
        var g = document.getElementById("phone");
        var k = g.value;
        var f = document.getElementById("dop");
        var v = f.value;
        alert(h);
        alert(k);
        alert(v);
        localStorage.setItem('name', h);
        localStorage.setItem('phone', k);
        localStorage.setItem('dop', v);
      }  
