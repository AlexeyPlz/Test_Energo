<template>
  <div v-if="posts.lenght > 0">
    <div>
      <h3>Список постов</h3>
      <post-item v-for="post in posts" :key="post.id" :post="post" @delete="$emit('delete', post)"/>
    </div>
  </div>
  <div v-else>
    <h3>Постов нет</h3>
  </div>
</template>

<script>
import postItem from '@/components/PostItem'

export default {
  components: {
    postItem
  },
  props: {
    posts: {
      type: Array,
      required: true
    }
  }
}
</script>
