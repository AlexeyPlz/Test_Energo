<template>
  <div class="main-block">
    <div class="task-block">
      <div class="task-data">
        <form @submit.prevent>
          <h2 class="row">Получить цвет объекта</h2>
          <div class="row">
            <h4>Дано 100 объектов трёх цветов.</h4>
            <h4>Синих сильно больше зеленых, а зеленых чуть больше красных.</h4>
            <h4>Выберете номер объекта от 1 до 100.</h4>
            <h4>Вам вернётся его цвет с определенной вероятностью.</h4>
          </div>
          <div class="row">
            <input type="number" v-model="number"/>
          </div>
          <div class="row">
            <button @click="sendData">Получить цвет</button>
          </div>
        </form>
        <div class="row"><strong>Цвет объекта: </strong>{{ color }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      number: 0,
      color: 'Цвет не известен'
    }
  },
  methods: {
    async sendData () {
      if (this.number < 1 || this.number > 100) { alert('На правильный номер объекта') }
      const response = await axios
        .get(
          `${process.env.VUE_APP_SERVER_URL}colored_objects/`,
          { params: { number: this.number } }
        ).then(
          (response) => { return response.data }
        )
      this.color = response.color
    }
  }
}
</script>

<style scoped>
.main-block {
  background-image: url('@/assets/images/back_task_one.png');
  background-repeat: round;
  height: 100vh;
}
.task-block {
  background-color: rgb(255, 255, 255);
  margin-left: 35%;
  margin-right: 35%;
}
.row {
  padding: 5px;
}
.task-data {
  text-align: center;
  align-items: center;
  padding: 5px 0 5px 0;
}
</style>
