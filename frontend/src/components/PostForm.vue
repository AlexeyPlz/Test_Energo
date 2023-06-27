<template>
  <form @submit.prevent>
    <h4>Создать пост</h4>
    <my-input placeholder="Название" v-model="post.title"/>
    <my-input placeholder="Описание" v-model="post.body"/>
    <my-button @click="createPost">Создать</my-button>
  </form>
</template>

<script>
import MyButton from '@/components/UI/MyButton'
import MyInput from '@/components/UI/MyInput'

export default {
  components: {
    MyButton,
    MyInput
  },
  data () {
    return {
      post: {
        title: '',
        body: ''
      }
    }
  },
  methods: {
    createPost () {
      this.post.id = Date.now()
      this.$emit('create', this.post)
      this.post = {
        title: '',
        body: ''
      }
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>
