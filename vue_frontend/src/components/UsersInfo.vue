<template>
    <div class="input-background">

          <div class="input-information">

      <div v-for="user in users">
        {{user.usuario}} | {{user.correo}} | {{user.edad}} | {{user.sexo}}
      </div>


          </div>


            <div class="input-information">
                <h1>Username</h1>
                <input v-model="usuario">
                
                <div :on-click="getInformationApi()"></div>

                <div v-if='id != undefined' class="data">

                  <p>correo: {{correo}}</p>
                  <p>edad: {{edad}}</p>
                  <p>sexo: {{sexo}}</p>

                </div>
    
            </div>

    </div>
  

</template>

<script>
export default {
    data() {
        return {
          id: "",
          usuario: "",
          correo: "",
          contrasena: "",
          sexo: "",
          edad: "",

          users: [],

        }
    },

    methods: {

        getInformationApi(){

          fetch("http://valorant-LB-655622502.us-east-1.elb.amazonaws.com:8001/usuario/" + this.usuario)
          .then(data => data.json())

          .then(x => {

          // console.log(x);
          this.id = x.id;
          this.correo = x.correo
          this.sexo = x.sexo
          this.edad = x.edad
        })
        .catch(err => {
        // console.log(err)
          this.id = undefined
          this.correo = undefined
          this.sexo = undefined
          this.edad = undefined
        })
          fetch("http://valorant-LB-655622502.us-east-1.elb.amazonaws.com:8001/usuarios")
          .then(data => data.json())

          .then(data => {
          this.users = data

        })
        .catch(err => {
        // console.log(err)
          this.users = []
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
