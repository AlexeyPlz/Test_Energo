<template>
  <header>
    <div class="menu">
      <router-link :to="{ name: 'TaskOne'}">
        <div class="menu-part">Расчёт квадратичного уравнения</div>
      </router-link>
      <router-link :to="{ name: 'TaskTwo'}">
        <div class="menu-part">Получить цвет объекта</div>
      </router-link>
    </div>
  </header>
  <main>
    <router-view/>
  </main>
</template>

<style>
* {
  margin:0;
  padding: 0;
  box-sizing: border-box;
}
header {
  background-color: rgb(252, 148, 62);
  border-bottom: 2px solid black;
  padding: 15px;
}
.menu {
  text-align: center;
}
.menu-part {
  color: black;
  font-size: large;
  display: inline-block;
  padding-inline: 10px;
}
</style>
