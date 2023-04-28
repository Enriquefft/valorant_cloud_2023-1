<template>
    
  <center>
    <div class="info-agent" v-for="item in data_api.data" :key="item">
    <img :src="item.displayIcon" >

    <a href="http://localhost:5173/"><h1 >{{ item.displayName }}</h1></a>
  </div>
  </center>

  
</template>

<script>
export default {

  data() {
    return {
      data_api : fetch("https://valorant-api.com/v1/agents?isPlayableCharacter=true")
      .then(info => info.json())
      .then(info => this.data_api = info),

      

                 

      
    }
  },
  methods: {

    
    
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Kanit:ital,wght@0,400;0,800;1,900&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Kanit:ital,wght@0,200;0,400;0,800;1,900&display=swap');

body{
  
  font-family: 'Anton', sans-serif;
  font-family: 'Kanit', sans-serif;
}

.info-agent{
  display:inline-flex;
  background-color: rgb(255,70,84);
  margin: 10px;
  width: 300px;
  border-radius:20px ;
  
}

.info-agent a{
  text-decoration: none;
  color:white
  
}

.info-agent img{
  border-radius: 20px;
  height: 100px;
  width: 100px;
}

</style>