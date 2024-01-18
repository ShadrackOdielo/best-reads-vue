<template>
  <div class="modal">
    <h2>{{ book.title }}</h2>
    <p>{{ book.author }}</p>
    <p>{{ book.description }}</p>
    <button @click="closeModal">Close</button>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
  },
  methods: {
    closeModal() {
      this.$emit('close-details-modal');
    },
  },
};
</script>

<style scoped>
/* Add your styling here */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 20px;
  z-index: 1000;
}
</style>
