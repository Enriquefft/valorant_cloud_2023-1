<template>
   
  <div class="valorant-part">
    <img src="./icons/valorant-font.png">

    

  </div>
   
  
  <div class="info-valorant-part">

    <center>
      <img src="https://media0.giphy.com/media/TQOTjlzMHRmoqF27CC/giphy.gif?cid=ecf05e478p6jw9gynh2hcqqi6402gal3kzrs3uabsefah0zv&rid=giphy.gif&ct=g">
      <h1>WHO WE ARE?</h1>
    </center> 
    
    <h3>
      We are a team that is in charge of giving information<br> about Valorant.
    </h3>
    
    

  </div>

  <div class="info-valorant-part">

    <center>
      <img src="https://media3.giphy.com/media/m95Dpc3iqbUUfThHpb/giphy.gif?cid=ecf05e474o60rfs02ud4795h86jq2zg6xdwwbghsfe2js9rt&rid=giphy.gif&ct=g">
      <h1>WE WANT...</h1>      
    </center>  

    <h3>
      We want you to be able to enjoy our game using <br> different agents and weapons to create a tactical <br> team using your creativity a lot.

    </h3>
    
    

  </div>

  


  <div class="gekko-part">
    <center><img src="https://staticc.sportskeeda.com/editor/2023/03/28e35-16781392976745-1920.jpg"
      >
    
        <h1 class="subtitulo-blanco" style="display:inline-block">Nuevo Agente 2023</h1>
    
    
      </center> 
      <br>

  </div>
  
 

  
</template>

<script>
export default {

}
</script>

<style>


@import url('https://fonts.googleapis.com/css2?family=Anton&family=Kanit:ital,wght@0,400;0,800;1,900&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Kanit:ital,wght@0,200;0,400;0,800;1,900&display=swap');

body{
  
  font-family: 'Anton', sans-serif;
  font-family: 'Kanit', sans-serif;
}

h1{
  margin: 0;
}

.subtitulo-blanco{
  color: white;
  font-size: 50px;
  font-weight: 200px;
  font-size: 50px;
}


.gekko-part{
  background-color: rgb(199,244,89);
}

.gekko-part img{
  height : 500px;
  display: inline-block;
}

.valorant-part{
  background-image: url("https://media.giphy.com/media/yQQMjKgLhRc9Y8stQV/giphy.gif");
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  height:500px ;
  margin: 0;
  display:flex;
  justify-content: center;
  align-items: center;
}

.valorant-part h1{
  margin: 1px;
}


.info-valorant-part{
  height:500px ;
  margin: 60px;
  background-color: rgb(255,70,84);
  display: inline-block;
  border-radius: 20px;
  
}

.info-valorant-part h1{
  color: rgb(15,25,34);  
  font-size: 50px;
  font-weight: 400px;
  font-size: 50px;
  display: flex;
  margin: 10px;
  
}

.info-valorant-part h3{
  margin: 20px;
}

.info-valorant-part img{
  border-radius: 20px 20px 0 0;
}




</style>