
<template>
    <div class="input-background">

          <div class="input-information">

          </div>


            <div class="input-information">
                <h1>id</h1>
                <input v-model="id">
                
                <div :on-click="getInformationApi()"></div>
       {{data}}

                <!-- <div v-if='partidas != []' class="data"> -->
                <!---->
                <!-- <div v-for="partida in partidas" :key="partida.id"> -->
                <!--   {{partida.id}} -->
                <!---->
                <!-- </div> -->
    
            <!-- </div> -->
<!---->
    </div>
  
  </div>

</template>

<script>
export default {
    data() {
        return {
          id: "",
          data: {},

        }
    },

    methods: {

        getInformationApi(){

          

          fetch("http://valorant-LB-655622502.us-east-1.elb.amazonaws.com:8002/competitivo/" + this.id)
          .then(data => data.json())

          .then(x => {

          console.log(x);
          this.data = x;
        })
        .catch(err => {
        console.log(err)
          this.data = {}
        })
    }
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

.input-information{
    background-color: white;
    display: inline-block;
    margin: 50px;
    padding: 80px;
    border-radius: 20px;
    
}

.input-information h1{
    margin: 20px;
}

.input-information input{
    height: 40px;
    outline: none;
    font-size: 20px;
    border-radius: 10px;
    background-color: rgb(237,237,237);
    font-family: monospace;
    
}

.input-information button{
    background-color: rgb(255,70,84);
    outline: none;
    border: none;
    height: 60px;
    width: 60px;
    border-radius: 20px;
}

.input-background{
    background-image: url("https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8b62399a54833858/640299e77af6422f7a2488e0/030723_VALORANT_2023_EP6-2_G_KO_Banner.jpg");
    height: 600px;
    padding: 100px;

}

.data {

display: grid;
padding: auto;

}

</style>
