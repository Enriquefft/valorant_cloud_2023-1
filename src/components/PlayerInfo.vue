<template>
    <div class="input-background">
        <center>
            <div class="input-information">
                <h1>Username</h1>
                <input v-model="username">
                <h1>{{username}}</h1>
                
                <h1>Tagname</h1>
                <input v-model="tagline">
                <h1>{{tagline}}</h1>

                <center><button :on-click="getInformationApi()">
                    ➜
                </button></center>
    
            </div>
        </center>

    </div>
    
    <div v-if="information === true">
        <h1>{{ username }} #{{tagline }} </h1>


    </div>
    
   
  

</template>

<script>
export default {
    data() {
        return {
            data_api_player : "",
            information_bool : false,
            username : "",
            tagline : "",
            puuid : "",
            region : "",
            account_level : "",
            id : ""
        }
    },

    methods: {
        getInformationApi(){

            var newUsername =  "";
            for (var i = 0; i < this.username.length; i++) {
                if(this.username[i] === " "){
                     newUsername = newUsername + '%';
                }
                else{
                    newUsername = newUsername + this.username[i] ; 
                }

                console.log(newUsername);               
                     
            }

            fetch("https://api.henrikdev.xyz/valorant/v1/account/" +  newUsername + "/" + this.tagline )
                .then(info => info.json()).then(info => {
                    info.status === 200;

                    this.data_api_player = info.data;
                    
                    this.puuid = info.data.puuid;
                    this.region = info.data.region;
                    this.account_level = info.data.account_level;

                    this.information_bool = true;

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

</style>