<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<style scoped>
.btn {
  align-self: flex-end;
  margin-top: 5px;
  padding: 10px 15px;
  background: none;
  color: teal;
  border: 1px solid teal;
}
</style>
