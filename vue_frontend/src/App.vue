import { RouterLink } from 'vue-router';
<template>
  
  <div class="nav-menu">      
    <img src="./components/icons/valorant-icon.png">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/agents">Agents</RouterLink>  
    <RouterLink to="/users">Users</RouterLink>      
    <RouterLink to="/players">Players</RouterLink>      
    <RouterLink to="/matches">Matches</RouterLink>      

  </div>
    

  <RouterView />
</template>

<script>
export default {

}
</script>

<style>

body{
  margin: 0;
}

.nav-menu{
  background-color: rgb(17,17,17);
  margin: 0;
  height: 60px;
  display: flex;
  align-content: center;
  align-items: center;

  
  font-family: 'Kanit', sans-serif;
}

.nav-menu img{
  height: 30px;
  margin: 10px;

}

.nav-menu a{
  color: white;
  text-decoration: none;
  margin: 10px;
}



</style>
