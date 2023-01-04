<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Instagram Account</title>
    <link rel="stylesheet" href="/static/assets/css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
<style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
html,body{
  display: grid;
  height: 100%;
  place-items: center;
  background: #664AFF;
}
::selection{
  color: #fff;
  background: #664AFF;
}
.search-box{
  position: relative;
  height: 60px;
  width: 60px;
  border-radius: 50%;
  box-shadow: 5px 5px 30px rgba(0,0,0,.2);
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.search-box.active{
  width: 350px;
}
.search-box input{
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 50px;
  background: #fff;
  outline: none;
  padding: 0 60px 0 20px;
  font-size: 18px;
  opacity: 0;
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.search-box input.active{
  opacity: 1;
}
.search-box input::placeholder{
  color: #a6a6a6;
}
.search-box .search-icon{
  position: absolute;
  right: 0px;
  top: 50%;
  transform: translateY(-50%);
  height: 60px;
  width: 60px;
  background: #fff;
  border-radius: 50%;
  text-align: center;
  line-height: 60px;
  font-size: 22px;
  color: #664AFF;
  cursor: pointer;
  z-index: 1;
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.search-box .search-icon.active{
  right: 5px;
  height: 50px;
  line-height: 50px;
  width: 50px;
  font-size: 20px;
  background: #664AFF;
  color: #fff;
  transform: translateY(-50%) rotate(360deg);
}
.search-box .cancel-icon{
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 25px;
  color: #fff;
  cursor: pointer;
  transition: all 0.5s 0.2s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.search-box .cancel-icon.active{
  right: -40px;
  transform: translateY(-50%) rotate(360deg);
}
.search-box .search-data{
  text-align: center;
  padding-top: 7px;
  color: #fff;
  font-size: 18px;
  word-wrap: break-word;
}
.search-box .search-data.active{
  display: none;
}
</style>  
</head>
  <body class="bg-primary">
    <form id="myForm">
    <div class="search-box">
      <input required id="USERNAME" type="text" placeholder="Search Account..">
      <div type="submit" class="search-icon"><i type="submit" class="fas fa-search"></i>
    </form>
      </div>
<div class="cancel-icon">
        <i class="fas fa-times"></i>
      </div>
<div class="search-data">
</div>
</div>
<script>
      const searchBox = document.querySelector(".search-box");
      const searchBtn = document.querySelector(".search-icon");
      const cancelBtn = document.querySelector(".cancel-icon");
      const searchInput = document.querySelector("input");
      const searchData = document.querySelector(".search-data");
      searchBtn.onclick =()=>{
        searchBox.classList.add("active");
        searchBtn.classList.add("active");
        searchInput.classList.add("active");
        cancelBtn.classList.add("active");

        if(searchInput.value != ""){
            type="submit"
        }else{
          searchData.textContent = "";
        }
      }
      cancelBtn.onclick =()=>{
        searchBox.classList.remove("active");
        searchBtn.classList.remove("active");
        searchInput.classList.remove("active");
        cancelBtn.classList.remove("active");
        searchData.classList.toggle("active");
        searchInput.value = "";
      }
    </script>

<script>
    document.getElementById('myForm').addEventListener('submit', function(event) {
      event.preventDefault(); // prevent form from being submitted
  
      // get value of input with ID "name"
      var USERNAME = document.getElementById('USERNAME').value;
  
      // set action of form to "google.com/name"
      this.action = "/download/" + USERNAME;
  
      // submit form
      this.submit();
    });
  </script>

  </body>
</html>