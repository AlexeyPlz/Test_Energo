<template>
  <div class="main-block">
    <div class="task-block">
      <div class="task-data">
        <form @submit.prevent>
          <h2 class="row">Решить квадратичное уравнение</h2>
          <div class="row">
            <label for="value_a"><strong>Значение A: </strong></label>
            <input id="value_a" class="input" type="number" v-model="equation.value_a"/>
          </div>
          <div class="row">
            <label for="value_b"><strong>Значение B: </strong></label>
            <input id="value_b" class="input" type="number" v-model="equation.value_b"/>
          </div>
          <div class="row">
            <label for="value_c"><strong>Значение C: </strong></label>
            <input id="value_c" class="input" type="number" v-model="equation.value_c"/>
          </div>
          <div class="row">
            <button @click="sendData">Получить решение</button>
          </div>
        </form>
        <div class="row"><strong>Значение X1: </strong>{{ result.value_x1 }}</div>
        <div class="row"><strong>Значение X2: </strong>{{ result.value_x2 }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      equation: {
        value_a: 0,
        value_b: 0,
        value_c: 0
      },
      result: {
        value_x1: 'Нет решения',
        value_x2: 'Нет решения'
      }
    }
  },
  methods: {
    async sendData () {
      if (this.equation.value_a === 0) { alert('Значение А не может быть равно 0') }
      const response = await axios
        .post(
          `${process.env.VUE_APP_SERVER_URL}quadratic_equations/`,
          { value_a: this.equation.value_a, value_b: this.equation.value_b, value_c: this.equation.value_c },
          { headers: { 'Content-Type': 'application/json' } }
        ).then(
          (response) => { return response.data }
        )
      this.result = {
        value_x1: response.value_x1 ? response.value_x1 : 'Нет решения',
        value_x2: response.value_x2 ? response.value_x2 : 'Нет решения'
      }
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
